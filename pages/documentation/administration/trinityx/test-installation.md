# Installation

| Nodes                 |      iDrac0    |  Int. mgmt IP  |   Internal IP  | External IP   |
|:----------------------|:--------------:|:--------------:|:--------------:|:-------------:|
| (subnet masks)        |     (/23)      |     (/23)      |     (/16)      |     (/24)     |
| test-head01           | 172.16.108.11  | 172.16.108.13  | 10.141.255.254 | 131.155.2.51  |
| test-head02           | 172.16.108.12  | 172.16.108.14  | 10.141.255.253 | 131.155.2.52  |
| test-head-vip         |       -        |       -        | 10.141.255.252 | 131.155.2.50  |
| test-login001         | 172.16.108.150 |       -        |       ?        | 131.155.2.53  |
| test-login002         | 172.16.108.x |       -        |       ?        | 131.155.2.x  |
| test-compute001       | 172.16.108.161 |       -        |       ?        |      -        |
| test-compute002       | 172.16.108.162 |       -        |       ?        |      -        |

## Requirements

- [Rocky Linux](https://rockylinux.org){:target=_blank} 8.x
- iDrac access to test-head01 and test-head02

??? example "Configuration"

    **Localization**
    
    - Keyboard: English (US)
    - Language Support: English (United States)
    - Time & Date: Europe/Amsterdam
    
    **Software**
    
    - Software Selection: Minimal Install (Standard)
    
    **System**
    
    - Installation Destination: Local Standard Disks (sda), Storage Configuration: Automatic
    - Network & Hostname:
       - Add interface:
          - Type: bond
          - Connection Name: `bond0`  *(Set name to make typing in terminal easy.)*
          - Mode: 802.3ad
          - Add appropriate interfaces
          - IPv4 settings: method: disabled
          - IPv6 settings: method: disabled
       - Add interface:
          - Type: VLAN
          - Connection Name: `tue`
          - Parent interface: `bond0`
          - VLAN id: `131`
          - IPv4 settings: method: manual - then set correct IP address `131.155.2.5x`, NM: `255.255.255.0`, and GW: `131.155.2.1`.
          - DNS servers: `131.155.2.3,131.155.3.3`
          - IPv6 settings: method: disabled
       - Host Name: `test-head0X.icts.tue.nl`
    
    **User Settings**
    
    - User Creation:
       - Name: `testadmin`
       - Make this user administrator

    **Post-installation**

    ```bash
    dnf -y update

    nmcli conn add \
        type vlan \
        con-name int \
        dev bond0 \
        id 141 \
        ip4 10.141.255.25x/16 \   # Use correct IP!
        ipv6.method disabled
    nmcli conn add \
        type ethernet \
        ifname eno1 \
        con-name mgmt \
        ip4 172.16.108.1x/23 \  # Use correct IP!
        ipv6.method disabled

    dnf -y install lldpd
    systemctl enable --now lldpd
    ```

## TrinityX Installation

### Prepare environment (test-head01 and test-head02)

As `root@test-head0X`:

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
git reset --hard 46538e9ab326c8249d9170be023de7b17bb42e49
```

### Configure environment (test-head01 only)

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
| el8_openhpc_repositories     | `OpenHPC/2/update.2.6.2/EL_8` | Activate latest update to OpenHPC 2.6                       |

```shell
cp site/hosts.example site/hosts
```

Review and edit the contents of the `hosts` file accordingly.

```ini
[controllers]
hpc-head01 ansible_host=10.141.255.254 ansible_connection=local
#hpc-head02 ansible_host=10.141.255.253
```

### Installation (test-head01 only)

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
