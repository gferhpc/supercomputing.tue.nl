# Installation

IPs: partially [here](../networking.md)

| Nodes                 |      iDrac0    |  Int. mgmt IP  |   Internal IP  | External IP   |       FKA       |
|:----------------------|:--------------:|:--------------:|:--------------:|:-------------:|:----------------:
| (subnet masks)        |     (/23)      |     (/23)      |     (/16)      |     (/24)     |        -        |
| test-head01           | 172.16.108.11  | 172.16.108.13  | 10.141.255.254 | 131.155.2.51  | hpc-primary     |
| test-head02           | 172.16.108.12  | 172.16.108.14  | 10.141.255.253 | 131.155.2.52  | hpc-secondary   |
| test-vip              |       -        |       -        | 10.141.255.252 | 131.155.2.50  | hpc-cluster     |
| test-login001         | 172.16.108.150 |       -        |       ?        | 131.155.2.53  | tue-login001    |
| test-compute001       | 172.16.108.161 |       -        |       ?        |      ?        | tue-computea001 |
| test-compute002       | 172.16.108.162 |       -        |       ?        |      ?        | tue-computea001 |

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
          - Name: `bond0`  *(Set name to make typing in terminal easy.)*
          - Mode: 802.3ad
          - Add appropriate interfaces
          - IPv4 settings: method: disabled
          - IPv6 settings: method: disabled
       - Add interface:
          - Type: VLAN
          - Name: `tue`
          - Parent interface: `bond0`
          - VLAN id: `131`
          - IPv4 settings: method: manual - then set correct IP address, netmask, and GW.
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

