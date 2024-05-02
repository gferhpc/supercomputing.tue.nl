# Installation

| Nodes                     |      iDrac0    |   Internal IP   | External IP (DHCP) |
|:--------------------------|:--------------:|:---------------:|:------------------:|
| test-head01               | 172.16.108.11  |       ?         |         ?          |
| test-head02               | 172.16.108.12  |       ?         |         ?          |

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
    - Network & Hostname: Configure Network, Hostname: test-head0X.icts.tue.nl
    
    **User Settings**
    
    - User Creation: ********, Make this user administratorTest

