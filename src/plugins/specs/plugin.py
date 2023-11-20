import json
import logging
import math
import os
import re

from mkdocs.config import Config
from mkdocs.config.config_options import Type, ListOfItems, DictOfItems
from mkdocs.plugins import BasePlugin


class SpecsPluginConfig(Config):
    enabled: bool = Type(bool, default=True)
    cache_path: str = Type(str, default=".cache")
    extra_nodes: list = ListOfItems(Type(dict), default=[])
    hardware: dict = DictOfItems(Type((str, str)), default={})
    nodes: dict = DictOfItems(Type(dict), default={})
    partitions: dict = DictOfItems(Type(dict), default={})


# Specs plugin
class SpecsPlugin(BasePlugin[SpecsPluginConfig]):
    def on_config(self, config):
        if not self.config.enabled:
            return

        with open(os.path.join(self.config.cache_path, "sinfo.json")) as content:
            data = json.load(content)

        for node in data['nodes'] + self.config.extra_nodes:
            self._register_node(node['hostname'], node['address'])

            if "partitions" in node:
                for partition in node['partitions']:
                    self._register_partition(partition, node['hostname'])

    # Build and render specs index page
    def on_page_markdown(self, markdown, page, config, files):
        if not self.config.enabled:
            return

        if markdown.find('.umbrella-specs') == -1:
            return

        matches = re.finditer(r"(?P<indents> +)?{\s+?\.umbrella-specs\s+?(?P<option>[a-zA-Z0-9\-.,]+)?\s+?}", markdown)
        for match in matches:
            if 'references' == match.group('option'):
                markdown = markdown.replace(
                    match.group(0),
                    self._generate_references()
                )
            else:
                markdown = markdown.replace(
                    match.group(0),
                    self._generate_table(match.group('option').split(','), match.group('indents'))
                )

        return markdown

    def _generate_table(self, options: list, indents: str):
        if indents is None:
            indents = ''

        table = None

        for option in options:
            if option in self.config.nodes:
                if table is None:
                    table = f"{indents}| Type | Threads | Memory | Processor/GPU |\n"
                    table += f"{indents}|-----------------|---------|--------|---------------|\n"

                if str(option).find('login') != -1:
                    table += self._render_node_row(option, indents, f"Login ^({self.config.nodes[option]['address']})^")
                elif str(option).find('storage') != -1:
                    table += self._render_node_row(option, indents, f"Storage ^({option})^")
                else:
                    table += self._render_node_row(option, indents)

            if option in self.config.partitions:
                if table is None:
                    table = f"{indents}| Partition/Nodes | Threads | Memory | Processor/GPU |\n"
                    table += f"{indents}|-----------------|---------|--------|---------------|\n"
                table += f"{indents}| **{option}** | **{self._sum_partition_category_cpu(option)}** | **{self._sum_partition_category_memory(option)}GB** | |\n"
                for category, nodes in dict(self.config.partitions[option]).items():
                    table += self._render_node_row(nodes[0], indents, f"{len(nodes)}x ^({category})^")

        return table

    def _render_node_row(self, hostname: str, indents: str, column: str = None):
        info = self._get_node_info(hostname)
        if info['processor']['SMT']:
            if str(info['processor']['brand']).find('Intel') != -1:
                cpus = f"{info['processor']['cpus']}^HT^"
            else:
                cpus = f"{info['processor']['cpus']}^SMT^"
        else:
            cpus = f"{info['processor']['cpus']}"

        details = f"{info['processor']['sockets']}x {info['processor']['brand']} {info['processor']['model']} @ {info['processor']['speed']}GHz[^{self._get_reference_index(info['processor']['brand'], info['processor']['model'])}]"
        if info['gpu']:
            details += f"<br/>{info['gpu']['cards']}x {info['gpu']['brand']} {info['gpu']['model']}[^{self._get_reference_index(info['gpu']['brand'], info['gpu']['model'])}]"

            if info['gpu']['mig']:
                for profile, count in dict(info['gpu']['mig']).items():
                    details += f" (MIG: {count}x {profile})"

        return f"{indents}| {column} | {cpus} | {info['memory']['size']}GB | {details} |\n"

    def _generate_references(self):
        references = ""

        count = 0

        for name, url in self.config.hardware.items():
            references += f"[^{count}]: [{name}]({url}){{:target=_blank}}\n"
            count = count + 1

        return references

    def _get_node_info(self, hostname: str):
        return self.config.nodes[hostname]

    def _sum_partition_category_cpu(self, partition: str):
        accumulated = 0

        for nodes in dict(self.config.partitions[partition]).values():
            for node in nodes:
                accumulated = accumulated + self.config.nodes[node]['processor']['cpus']

        return accumulated

    def _sum_partition_category_memory(self, partition: str):
        accumulated = 0

        for nodes in dict(self.config.partitions[partition]).values():
            for node in nodes:
                accumulated = accumulated + self.config.nodes[node]['memory']['size']

        return accumulated

    def _register_node(self, hostname: str, address: str):
        self.config.nodes[hostname] = {
            'address': address,
            'processor': self._get_processor_info(hostname),
            'memory': self._get_memory_info(hostname),
            'gpu': self._get_gpu_info(hostname),
        }

    def _register_partition(self, partition: str, hostname: str):
        if partition not in self.config.partitions:
            self.config.partitions[partition] = {}

        matches = re.match(r"^(?P<group>\w+)-(?P<category>(?P<type>[a-z]+)(?P<cat>[A-Z]+))\d+$", hostname)
        if not matches:
            return

        if partition.split('.')[0].split('-')[0] != matches.group('group') and matches.group('group') != 'arch':
            return  # exclude non-department nodes from groups in listing.

        category = matches.group('category')

        if category not in self.config.partitions[partition]:
            self.config.partitions[partition][category] = []

        self.config.partitions[partition][category].append(hostname)

    def _get_gpu_info(self, hostname: str):  # Parses "nvidia-smi -L" output.
        gpu = None

        with open(os.path.join(self.config.cache_path, hostname)) as content:
            for line in content:
                matches = re.match(r"^GPU \d+:( NVIDIA)? (?P<model>.+) \(.+", line, re.IGNORECASE)
                if matches:
                    if gpu is None:
                        gpu = {"brand": "NVIDIA", "model": None, "cards": 0, "mig": None}

                    gpu['cards'] = gpu['cards'] + 1
                    gpu['model'] = matches.group('model')
                matches = re.match(r"^\s+MIG (?P<profile>[a-z0-9.]+)\s+Device", line, re.IGNORECASE)
                if matches:
                    if gpu['mig'] is None:
                        gpu['mig'] = {}

                    if matches.group('profile') not in gpu['mig']:
                        gpu['mig'][matches.group('profile')] = 0

                    gpu['mig'] = {
                        matches.group('profile'): gpu['mig'][matches.group('profile')] + 1
                    }
        return gpu

    def _get_memory_info(self, hostname: str):  # Parses "dmidecode --type=memory" output.
        memory = {
            'type': None,
            'speed': None,  # MT/s
            'size': 0,      # GB
            'modules': 0,
        }

        with open(os.path.join(self.config.cache_path, hostname)) as content:
            for line in content:
                matches = re.match(r"^\s+Type:\s+(\w+)", line)
                if matches and (memory['type'] is None or memory['type'] == "Unknown"):
                    memory['type'] = matches.group(1)

                matches = re.match(r"^\s+Speed:\s+(\d+) MT/s", line)
                if matches:
                    memory['speed'] = matches.group(1)

                matches = re.match(r"^\s+Size:\s+(\d+)\s+(MB|GB|TB)", line)
                if matches:
                    memory['modules'] = memory['modules'] + 1
                    match matches.group(2):
                        case "MB":
                            memory['size'] = int(memory['size'] + (int(matches.group(1)) / 1024))
                        case "GB":
                            memory['size'] = int(memory['size'] + int(matches.group(1)))
                        case "TB":
                            memory['size'] = int(memory['size'] + (int(matches.group(1)) * 1024))
        return memory

    def _get_processor_info(self, hostname: str):  # Parses "lscpu" output.
        processor = {
            "brand": None,
            "model": None,
            "speed": None,  # GHz
            "sockets": 0,
            "cpus": 0,
            "SMT": False,
        }

        with open(os.path.join(self.config.cache_path, hostname)) as content:
            for line in content:
                matches = re.match(r"^CPU\(s\):\s+(\d+)", line)
                if matches:
                    processor["cpus"] = int(matches.group(1))

                matches = re.match(r"^Socket\(s\):\s+(\d+)", line)
                if matches:
                    processor["sockets"] = int(matches.group(1))

                matches = re.match(r"^Thread\(s\) per core:\s+(\d+)", line)
                if matches:
                    processor["SMT"] = int(matches.group(1)) != 1

                matches = re.match(r"^Model name:\s+AMD EPYC (?P<model>\w+) .+$", line, re.IGNORECASE)
                if matches:
                    processor["brand"] = "AMD EPYC™"
                    processor["model"] = matches.group('model')
                    processor["speed"] = float(self._get_processor_speed(hostname))

                    return processor

                matches = re.match(r"^Model name:\s+Intel.+(?P<model>(Bronze|Silver|Gold|Platinum) \w+).+@ (?P<speed>\d+\.\d+).+$", line, re.IGNORECASE)
                if matches:
                    processor["brand"] = "Intel® Xeon®"
                    processor["model"] = matches.group('model')
                    processor["speed"] = float(matches.group('speed'))

                    return processor

                matches = re.match(r"^Model name:\s+Intel.+CPU\s+(?P<model>[a-z0-9\-]+( v\d+)?).+@ (?P<speed>\d+\.\d+).+$", line, re.IGNORECASE)
                if matches:
                    processor["brand"] = "Intel® Xeon®"
                    processor["model"] = matches.group('model')
                    processor["speed"] = float(matches.group('speed'))

                    return processor

                matches = re.match(r"^Model name:\s+Intel.+\s+(?P<model>[a-z0-9\-]+( v\d+)?).+CPU @ (?P<speed>\d+\.\d+).+$", line, re.IGNORECASE)
                if matches:
                    processor["brand"] = "Intel® Xeon®"
                    processor["model"] = matches.group('model')
                    processor["speed"] = float(matches.group('speed'))

                    return processor

        return processor

    def _get_processor_speed(self, hostname: str):
        with open(os.path.join(self.config.cache_path, hostname)) as content:
            for line in content:
                matches = re.match(r"^CPU MHz:\s+(\d+)", line)
                if matches:
                    return f"{math.ceil(int(matches.group(1).split('.')[0]) / 10) / 100:.2f}"

    def _get_reference_index(self, brand: str, model: str):
        return list(self.config.hardware.keys()).index(f"{brand} {model}")


log = logging.getLogger("mkdocs.material.umbrella-specs")
