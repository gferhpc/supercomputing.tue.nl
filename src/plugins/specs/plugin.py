import json, logging, re
from json import JSONDecodeError
from mkdocs.config import Config
from mkdocs.config.config_options import Type, ListOfItems, DictOfItems
from mkdocs.plugins import BasePlugin


class SpecsPluginConfig(Config):
    enabled: bool = Type(bool, default=True)
    sinfo_path: str = Type(str, default="sinfo.json")
    extra_nodes: list = ListOfItems(Type(dict), default=[])
    hardware: dict = DictOfItems(Type((str, str)), default={})
    nodes: dict = DictOfItems(Type(dict), default={})
    partitions: dict = DictOfItems(Type(dict), default={})


# Specs plugin
class SpecsPlugin(BasePlugin[SpecsPluginConfig]):
    def on_config(self, config):
        if not self.config.enabled:
            return

        try:
            with open(self.config.sinfo_path) as content:
                data = json.load(content)
        except (FileNotFoundError, JSONDecodeError):
            log.error("%s not found, disabled plugin as a result.", self.config.sinfo_path)
            self.config.enabled = False
            return

        for node in data['nodes'] + self.config.extra_nodes:
            self._register_node(node)

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
            elif option in self.config.partitions:
                if table is None:
                    table = f"{indents}| Partition/Nodes | Threads | Memory | Processor/GPU |\n"
                    table += f"{indents}|-----------------|---------|--------|---------------|\n"
                table += f"{indents}| **{option}** | **{self._sum_partition_category_cpu(option)}** | **{self._sum_partition_category_memory(option)}GB** | |\n"
                for category, nodes in dict(self.config.partitions[option]).items():
                    table += self._render_node_row(nodes[0], indents, f"{len(nodes)}x ^({category[:-1] + category[-1].upper()})^")
            else:
                log.warning("No configuration found for: %s", option)

        return table if table is not None else ""

    def _render_node_row(self, hostname: str, indents: str, column: str = None):
        node = self._get_node_info(hostname)

        details = f"{round(node['boards'] * node['sockets'])}x {node['extra']['cpu']} @ {node['extra']['cpu_frq']}GHz[^{self._get_reference_index(node['extra']['cpu'])}]"

        if node['threads'] >= 2:
            if 'intel' in node['features']:
                cpus = f"{node['cpus']}^HT^"
            else:
                cpus = f"{node['cpus']}^SMT^"
        else:
            cpus = f"{node['cpus']}"

        if 'gpu' in node['extra'] and 'gres' in node:
            if matches := re.match(r"gpu:((?P<mig_profile>.*):)?(?P<gpu_count>\d+)\(S:.*\)", node['gres'], re.IGNORECASE):
                details += f"<br/>{matches['gpu_count']}x {node['extra']['gpu']}[^{self._get_reference_index(node['extra']['gpu'])}]"
                if matches['mig_profile']:
                    details += f" (MIG: {matches['mig_profile']})"

        return f"{indents}| {column} | {cpus} | {node['extra']['mem']}GB | {details} |\n"

    def _generate_references(self):
        references = ""

        count = 0

        for name, url in self.config.hardware.items():
            references += f"[^{count}]: [{name}]({url}){{:target=_blank}}\n"
            count = count + 1

        return references

    def _get_node_info(self, hostname: str):
        if hostname not in self.config.nodes:
            raise RuntimeError(f"Node {hostname} not found.")

        return self.config.nodes[hostname]

    def _sum_partition_category_cpu(self, partition: str):
        accumulated = 0

        for nodes in dict(self.config.partitions[partition]).values():
            for node in nodes:
                accumulated = accumulated + self.config.nodes[node]['cpus']

        return accumulated

    def _sum_partition_category_memory(self, partition: str):
        accumulated = 0

        for nodes in dict(self.config.partitions[partition]).values():
            for node in nodes:
                accumulated = accumulated + int(self.config.nodes[node]['extra']['mem'])

        return accumulated

    def _register_node(self, node: dict):
        try:
            node['extra'] = json.loads(node['extra'])
            node['features'] = node['features'].split(',') if 'features' in node else []
            self.config.nodes[node['name']] = node
        except (JSONDecodeError, KeyError):
            log.error("Failed to parse node %s extra information.", node['name'])

    def _register_partition(self, partition: str, hostname: str):
        if partition not in self.config.partitions:
            self.config.partitions[partition] = {}

        matches = re.match(r"^(?P<group>\w+)-(?P<category>(?P<type>(compute|gpu|storage|login))(?P<cat>[A-Za-z]+))\d+$", hostname)
        if not matches:
            return

        if partition.split('.')[0].split('-')[0] != matches.group('group') and matches.group('group') != 'arch':
            return  # exclude non-department nodes from groups in listing.

        category = matches.group('category')

        if category not in self.config.partitions[partition]:
            self.config.partitions[partition][category] = []

        self.config.partitions[partition][category].append(hostname)

    def _get_reference_index(self, version: str):
        return list(self.config.hardware.keys()).index(f"{version}")


log = logging.getLogger("mkdocs.material.umbrella-specs")
