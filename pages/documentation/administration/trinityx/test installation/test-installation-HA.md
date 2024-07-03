## HA TrinityX (latest version) Installation on test-head01 and test-head02

### Prepare environment

All as `root@test-head01`:

```shell
dnf -y install git
```

Make sure the DHPC on an interface does not overwrite DNS entries in resolv.conf

```shell
sed -i 's/main]/main]\ndns=none/' /etc/NetworkManager/NetworkManager.conf
```

Clone the TrinityX github repo

```shell
git clone https://github.com/clustervision/trinityX.git /root/trinityX
cd /root/trinityX
```

### Configure environment

```shell
cp site/group_vars/all.yml.example site/group_vars/all.yml
```

Review and edit the contents of the `all.yml` file accordingly, notable settings:

| Setting                      | Value                         | Description                                                 |
|------------------------------|-------------------------------|-------------------------------------------------------------|
| administrator_email          | `hpc-umbrella@tue.nl`         | Email address of the administrator                          |
| project_id                   | `test-umbrella`               | Project ID                                                  |
| ha                           | `true`                        | High Availability                                           |
| trix_ctrl1_ip                | `10.141.255.254`              | IP controller node in Cluster Network                       |
| trix_ctrl1_bmcip             | `172.16.108.13`               | IP controller node in BMC Network                           |
| trix_ctrl1_hostname          | `test-head01`                 | Hostname                                                    |
| trix_ctrl2_ip                | `10.141.255.253`              | IP controller node in Cluster Network                       |
| trix_ctrl2_bmcip             | `172.16.108.12`               | IP controller node in BMC Network                           |
| trix_ctrl2_hostname          | `test-head02`                 | Hostname                                                    |
| xxxxxxxxxxxxxx               | `xxxxxxxxxxx`                 | XXXXXXXX                                                    |
| trix_cluster_net.            | `10.141.0.0`                  | Cluster (Private) Network                                   | 
| trix_cluster_netprefix.      | `16`                          | CIDR of Cluster Network                                     |
| trix_cluster_dhcp_start      | `10.141.128.0`                | Start of DHCP range for nodes                               |
| trix_cluster_dhcp_end        | `10.141.135.255`              | End of DHCP range for nodes                                 |
| trix_external_fqdn           | `test-umbrella-cluster.hpc.tue.nl` | FQDN of the external interface of the cluster          |
| trix_dns_forwarders          | `[131.155.2.3, 131.155.3.3]`  | List of DNS forwarders to use for the cluster.              |
| firewalld_public_interfaces  | `[bond0.131]`                 | List of public interfaces to use for the cluster.           |
| firewalld_trusted_interfaces | `[bond0.141]`                 | List of trusted interfaces to use for the cluster.          |

```shell
cp site/hosts.example site/hosts
```

Review and edit the contents of the `hosts` file accordingly.

```ini
[controllers]
test-head01 ansible_host=10.141.255.254 ansible_connection=local
test-head02 ansible_host=10.141.255.253
```

### Installation

Install dependencies
```shell
cd /root/trinityX
bash prepare.sh
```
Run the ansible-playbook
```shell
cd /root/trinityX/site
ansible-playbook controller.yml
```
