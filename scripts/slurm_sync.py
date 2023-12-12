import json
import re
import subprocess
from typing import Final

CPU_MANUFACTURER_AMD: Final[str] = "AMD"
CPU_MANUFACTURER_INTEL: Final[str] = "Intel"
CPU_FAMILY_EPYC: Final[str] = "EPYC"
CPU_FAMILY_XEON: Final[str] = "Xeon"
GPU_MANUFACTURER_NVIDIA: Final[str] = "NVIDIA"
GPU_FAMILY_AMPERE: Final[str] = "Ampere"
GPU_FAMILY_PASCAL: Final[str] = "Pascal"
GPU_FAMILY_VOLTA: Final[str] = "Volta"
GPU_FAMILY_TESLA: Final[str] = "Tesla"
GPU_FAMILY_TURING: Final[str] = "Turing"


class SLURM:
    sinfo = "{}"

    def __init__(self):
        result = self._run('hpc-primary', 'sinfo --json')
        self.sinfo = json.loads(result)

    def generate(self, filtered_hosts: list[str] = None):
        specifications = {}
        nodes = []
        commands = []

        if filtered_hosts:
            for node in self.sinfo['nodes']:
                if node['name'] in filtered_hosts:
                    nodes.append(node)
            pass
        else:
            nodes = self.sinfo['nodes']

        print("[%d] " % len(nodes), end="")
        for index, node in enumerate(nodes):
            specifications[node['name']] = self.gather_specs(node['address'])
            if command := self.get_feature_commands(node, set(self.get_features_by_specifications(specifications[node['name']]))):
                commands.append(command)
            if command := self.get_extra_commands(node, self.get_extras_by_specification(specifications[node['name']])):
                commands.append(command)

            print(".", end="")

        print("Done!")

        for command in set(commands):
            print(command)

    def gather_specs(self, host: str):
        specifications = {
            'processor': self._get_processor(host),
            'memory': self._get_memory(host),
            'gpu': self._get_gpu(host),
        }

        return specifications

    @staticmethod
    def get_extra_commands(node: dict, extra: str):
        if extra == node['extra']:
            return

        return f'scontrol update NodeName="{node["name"]}" Extra=\'{extra}\''

    @staticmethod
    def get_feature_commands(node: dict, features: set):
        missing_features = features - set(node['features'].split(','))
        category = re.sub(r'^([a-z]+-[a-zA-Z]+)\d+$', '\\1-cat', node['name'])

        if not missing_features:
            return None

        command = f"cmsh -c 'category; roles {category}"

        for feature in missing_features:
            command += f"; append slurmclient features {feature}"

        return command + "; commit'"

    @staticmethod
    def get_features_by_specifications(specifications: dict):
        features = [
            specifications['processor']['manufacturer'].replace(' ', '').lower(),
            specifications['processor']['generation'].replace(' ', '').lower(),
        ]

        if specifications['gpu']:
            # features.append(specifications['gpu']['manufacturer'].replace(' ', '').lower())
            features.append(specifications['gpu']['family'].replace(' ', '').lower())
            features.append(specifications['gpu']['model'].replace(' ', '').lower())

        return features

    @staticmethod
    def get_extras_by_specification(specifications: dict):
        extra = {
            'cpu': specifications['processor']['version'],
            'cpu_frq': specifications['processor']['speed'],
            'mem': specifications['memory']['size'],
        }

        if specifications['gpu']:
            extra['gpu'] = specifications['gpu']['version']

        return json.dumps(extra)

    def _get_processor(self, host: str):
        processor = {
            'version': None,
            "manufacturer": None,
            'family': None,
            'generation': None,
            "model": None,
            "speed": None,
        }

        version = self._run(host, 'dmidecode -s processor-version').splitlines()[0].strip()

        if matches := re.match(r"^AMD EPYC (?P<model>\w+) .+$", version, re.IGNORECASE):
            processor['version'] = f"AMD EPYC %s" % matches.group('model')
            processor["manufacturer"] = CPU_MANUFACTURER_AMD
            processor["family"] = CPU_FAMILY_EPYC
            processor["model"] = matches.group('model')
            processor["speed"] = f"{int(self._run(host, 'dmidecode -s processor-frequency').splitlines()[0].rstrip('MHz')) / 1000:.2f}"
        elif matches := re.match(r"^Intel.+Xeon.+(?P<model>(Bronze|Silver|Gold|Platinum) \w+).+@ (?P<speed>\d+\.\d+).+$", version, re.IGNORECASE):
            processor['version'] = f"Intel Xeon %s" % matches.group('model')
            processor["manufacturer"] = CPU_MANUFACTURER_INTEL
            processor['family'] = CPU_FAMILY_XEON
            processor["model"] = matches.group('model')
            processor["speed"] = matches.group('speed')
        elif matches := re.match(r"^Intel.+Xeon.+CPU\s+(?P<model>[a-z0-9\-]+( v\d+)?).+@ (?P<speed>\d+\.\d+).+$", version, re.IGNORECASE):
            processor['version'] = f"Intel Xeon %s" % matches.group('model')
            processor["manufacturer"] = CPU_MANUFACTURER_INTEL
            processor['family'] = CPU_FAMILY_XEON
            processor["model"] = matches.group('model')
            processor["speed"] = matches.group('speed')
        elif matches := re.match(r"^Intel.+Xeon.+\s+(?P<model>[a-z0-9\-]+( v\d+)?).+CPU @ (?P<speed>\d+\.\d+).+$", version, re.IGNORECASE):
            processor['version'] = f"Intel Xeon %s" % matches.group('model')
            processor["manufacturer"] = CPU_MANUFACTURER_INTEL
            processor['family'] = CPU_FAMILY_XEON
            processor["model"] = matches.group('model')
            processor["speed"] = matches.group('speed')
        else:
            raise Exception('Unable to determine processor (%s)'.format(version))

        if CPU_MANUFACTURER_AMD == processor["manufacturer"]:
            match processor['model'][3]:
                case '1':
                    processor['generation'] = 'Naples'
                case '2':
                    processor['generation'] = 'Rome'
                case '3':
                    processor['generation'] = 'Milan'
                case '4':
                    processor['generation'] = 'Genoa'
                case _:
                    raise Exception('Unknown AMD EPYC generation (%s)'.format(processor['model'][3]))
        elif CPU_MANUFACTURER_INTEL == processor["manufacturer"]:
            if matches := re.match(r"^(Bronze|Silver|Gold|Platinum) [0-9](?P<generation>[0-9])[0-9]{2}[A-Z]?$", processor['model'], re.IGNORECASE):
                match matches.group('generation'):
                    case '1':
                        processor['generation'] = 'Skylake'
                    case '2':
                        processor['generation'] = 'Cascade Lake'
                    case '3':
                        processor['generation'] = 'Ice Lake'
                    case '4':
                        processor['generation'] = 'Sapphire Rapids'
                    case _:
                        raise Exception('Unknown Intel Xeon generation (%s)'.format(matches.group('generation')))
            elif matches := re.match(r"^E5-\w+( v(?P<generation>\d))?$", processor['model'], re.IGNORECASE):
                match matches.group('generation'):
                    case None:
                        processor['generation'] = 'Sandy Bridge'
                    case '2':
                        processor['generation'] = 'Ivy Bridge'
                    case '3':
                        processor['generation'] = 'Haswell'
                    case '4':
                        processor['generation'] = 'Broadwell'
                    case _:
                        raise Exception('Unknown Intel Xeon generation (%s)'.format(matches.group('generation')))
            elif re.match(r"^X5650$", processor['model'], re.IGNORECASE):
                processor['generation'] = 'Westmere'
            else:
                raise Exception('Unable to determine generation (%s)'.format(processor['model']))

        return processor

    def _get_memory(self, host: str):
        size = int(self._run(host, "dmidecode -t memory | egrep '^\sSize: [0-9]+' | awk -F: \'{sum += $2} END {print sum}\'"))

        if size >= 8192:
            size = int(round(size / 1024))

        return {
            'size': str(size),
        }

    def _get_gpu(self, host: str):
        gpu = {
            'version': None,
            "manufacturer": None,
            'family': None,
            'model': None,
        }

        if "gpu" not in host.lower():
            return None

        try:
            nvidia = self._run(host, 'nvidia-smi --query-gpu=name --format=csv,noheader').splitlines()[0].strip()
        except RuntimeError:
            return None

        gpu['version'] = f"NVIDIA %s" % nvidia.replace('NVIDIA ', '')
        if matches := re.match(r"^NVIDIA (?P<model>A[0-9]+)(?P<suffix>.*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_AMPERE
            gpu['model'] = matches.group('model')
        elif matches := re.match(r"^NVIDIA Titan (?P<model>\w+)(?P<suffix> .*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_PASCAL
            gpu['model'] = matches.group('model')
        elif matches := re.match(r"^NVIDIA.*RTX (?P<model>\d+( ti)?)(?P<suffix>.*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_TURING
            gpu['model'] = matches.group('model')
        elif matches := re.match(r"^NVIDIA.*RTX (?P<model>A\d+( ti)?)(?P<suffix>.*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_AMPERE
            gpu['model'] = matches.group('model')
        elif matches := re.match(r"^Quadro RTX (?P<model>\d+)(?P<suffix>.*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_TURING
            gpu['model'] = matches.group('model')
        elif matches := re.match(r"Tesla (?P<model>K\d+)(?P<suffix>.*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_TESLA
            gpu['model'] = matches.group('model')
        elif matches := re.match(r"Tesla (?P<model>V\d+)(?P<suffix>.*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_VOLTA
            gpu['model'] = matches.group('model')
        elif matches := re.match(r"Tesla (?P<model>P\d+)(?P<suffix>.*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_PASCAL
            gpu['model'] = matches.group('model')
        elif matches := re.match(r"Tesla (?P<model>K\d+)(?P<suffix>.*)?$", nvidia, re.IGNORECASE):
            gpu['manufacturer'] = GPU_MANUFACTURER_NVIDIA
            gpu['family'] = GPU_FAMILY_TESLA
            gpu['model'] = matches.group('model')
        else:
            raise RuntimeError('Unable to determine GPU (%s)'.format(nvidia))

        return gpu

    @staticmethod
    def _run(host: str, command: str):
        result = subprocess.run(
            ['ssh', host, command],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            raise RuntimeError('Unable to run command (%s)'.format(command))

        return result.stdout


SLURM().generate()
