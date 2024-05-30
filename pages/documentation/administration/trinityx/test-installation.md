# Installation

IPs: partially [here](../networking.md)

| Nodes                 |      iDrac0    |   Internal IP   | External IP (DHCP) |       FKA       |
|:----------------------|:--------------:|:---------------:|:------------------:|:----------------:
| test-head01           | 172.16.108.13  |       ?         |         ?          | hpc-primary     |
| test-head02           | 172.16.108.14  |       ?         |         ?          | hpc-secondary   |
| test-login001         | 172.16.108.150 |       ?         |         ?          | tue-login001    |
| test-compute001       | 172.16.108.161 |       ?         |         ?          | tue-computea001 | 
| test-compute002       | 172.16.108.162 |       ?         |         ?          | tue-computea001 | 

- `test-head01.infra.tue.nl` `172.16.108.11`
- `test-head02.infra.tue.nl` `172.16.108.12`

## Requirements

- Node with at least 2 NIC interfaces (public & internal network)
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
          - Mode: 802.3ad
          - Add appropriate interfaces
          - IPv4 settings: method: disabled
          - IPv6 settings: method: disabled
       - Add interface:
          - Type: VLAN
          - Parent interface: bond0
          - VLAN id: 131
          - IPv4 settings: method: manual - then set correct IP address and GW.
          - DNS servers: `131.155.2.3,131.155.3.3`
          - IPv6 settings: method: disabled
       - Add interface:
          - Type: VLAN
          - Parent interface: bond0
          - VLAN id: 141
          - IPv4 settings: method: manual - ip 10.141.255.25x netmask 16
          - DNS servers: `131.155.2.3,131.155.3.3`
          - IPv6 settings: method: disabled
       - Host Name: test-head0X.icts.tue.nl
    
    **User Settings**
    
    - User Creation: ********, Make this user administratorTest

