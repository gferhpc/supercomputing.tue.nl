## NO-HA TrinityX (latest version) Installation on test-head01

### Prepare environment

All as `root@test-head01`:

```shell
dnf -y install git screen
```

Use screen to resume after network disconnects

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
| ha                           | `false` (default)             | High Availability; _MUST remain `false` at time of writing_ |
| trix_ctrl1_ip                | `10.141.255.254 `             | IP controller node in Cluster Network                       |
| trix_ctrl1_bmcip             | `172.16.108.13`               | IP controller node in BMC Network                           |
| trix_ctrl1_hostname          | `test-head01`                 | Hostname                                                    |
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
test-head01 ansible_host=127.0.0.1 ansible_connection=local
```

### Installation

Install dependencies
```shell
cd /root/trinityX
bash prepare.sh
```
Run the ansible-playbook (use screen)
```shell
dnf -y install screen
screen
cd /root/trinityX/site
ansible-playbook controller.yml
```

### Configuration

#### Set cluster settings

```shell
luna cluster change -n test-umbrella -c hpc-umbrella@tue.nl
```

#### Configure the BMC(ipmi) network

```shell
luna network change -N 172.16.108.0/23 ipmi
```

### Create a demo user (or not)

```shell
obol user add demo -p demo
obol group addusers admins demo
```

#### Create the basic OSimage (compute)

```shell
ansible-playbook compute-redhat.yml
luna osimage pack compute
```

#### Add [pre.txt](pre.txt){:target=_blank}, [part.txt](part.txt){:target=_blank} and [post.txt](post.txt){:target=_blank} to the part/post of the compute image

```shell
wget https://gitlab.tue.nl/hpclab/website/-/raw/main/pages/documentation/administration/trinityx/pre.txt
wget https://gitlab.tue.nl/hpclab/website/-/raw/main/pages/documentation/administration/trinityx/part.txt
wget https://gitlab.tue.nl/hpclab/website/-/raw/main/pages/documentation/administration/trinityx/post.txt
luna group change -qpre pre.txt compute
luna group change -qpart part.txt compute
luna group change -qpost post.txt compute
```

Authentication via AD

```shell
cat >> /etc/sssd/sssd.conf << EOF

auth_provider = krb5
krb5_server = campus.tue.nl
krb5_kpasswd = campus.tue.nl
krb5_realm = CAMPUS.TUE.NL
cache_credentials = True
EOF
systemctl restart sssd
```

### Delete the Auto-Generated Nodes
```shell
luna node remove node001
luna node remove node002
luna node remove node003
luna node remove node004
```

### Create the Compute Nodes
```shell
luna node add -g compute -if BOOTIF -M 4C:D9:8F:49:7F:8F test-computea001
luna node changeinterface -N ipmi -I 172.16.108.161 test-computea001 BMC
luna node add -g compute -if BOOTIF -M 4C:D9:8F:49:7B:17 test-computea002
luna node changeinterface -N ipmi -I 172.16.108.162 test-computea002 BMC
```

## Disable bmcsetup for group compute when provisioning

```shell
luna group change --setupbmc n compute
```

## Renename bmcsetup compute to trinityx and match the pre.txt settings
```shell
luna bmcsetup rename compute trinityx
luna bmcsetup change -uid 3 -u trinityx -p <PASSWORD> trinityx
```
