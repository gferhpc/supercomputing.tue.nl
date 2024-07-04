# Installation

| Nodes                 |      iDrac0    |  Int. mgmt IP  |   Internal IP/MAC  | External IP  |
|:----------------------|:--------------:|:--------------:|:-----------------:|:-------------:|
| (subnet masks)        |     (/23)      |     (/23)      |     (/16)         |     (/24)     |
| test-head01           | 172.16.108.11  | 172.16.108.13  | 10.141.255.254    | 131.155.2.51  |
| test-head02           | 172.16.108.12  | 172.16.108.14  | 10.141.255.253    | 131.155.2.52  |
| test-head-vip         |       -        |       -        | 10.141.255.252    | 131.155.2.50  |
| test-login001         | 172.16.108.150 |       -        | 50:9A:4C:A5:F3:C0 | 131.155.2.53  |
| test-login002         | 172.16.108.201 |       -        | B4:96:91:71:2C:4C | 131.155.2.x   |
| test-computea001      | 172.16.108.161 |       -        | 4C:D9:8F:49:7F:8F |      -        |
| test-computea002      | 172.16.108.162 |       -        | 4C:D9:8F:49:7B:17 |      -        |

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

    reboot
    ```

## TrinityX Installation

[NO HA Installation](test-installation-NO-HA.md)

[Ha Installation](test-installation-HA.md)