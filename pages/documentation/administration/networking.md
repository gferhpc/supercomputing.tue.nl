# Networking

## VLANs

### Cluster internal

- 1: `default-vlan`
- 141: `testcl-int`  test cluster internal
- 150: `umbrella-int`  Umbrella cluster internal

## IP space

### TU/e

- Subnet: 131.155.7.96/27 --- TU/e HPC
    - 131.155.7.96–127
    - 131.155.7.102–126 usable
    - 131.155.7.102 `hpc-head01.icts.tue.nl`
    - 131.155.7.103 `hpc-head02.icts.tue.nl`
    - 131.155.7.104 `hpc-vip.icts.tue.nl`
    - 131.155.7.109 `tue-login002.icts.tue.nl`
- Subnet: 172.16.108.0/23 — Mgmt-Infra-TUe-HPC (VLAN 301)
    - 172.16.108.240–255 — `hpc-vast-mgmt-1..16.infra.tue.nl` (C2402488)

### Cluster internal

- Subnet: 10.148.0.0/16 - Umbrella Cluster heartbeat
- Subnet: 10.149.0.0/16 — Umbrella Cluster InfiniBand
- Subnet: 10.150.0.0/16 — Umbrella Cluster Ethernet
    - 10.150.0.1 — first node; nodes number upwards from here
    - 10.150.128–135.x — DHCP pool
    - 10.150.250.x — VAST storage
    - 10.150.254.x — classical storage nodes
        - 10.150.254.1 — tue-storage001
        - 10.150.254.11 - phys-storage001
        - 10.150.254.21 - arch-storage001
        - 10.150.254.31 - bme-storage001
        - 10.150.254.41 - mech-storage001
        - 10.250.254.51 - mcs-storage001
        - 10.250.254.61 - chem-storage001
        - 10.250.254.62 - chem-storage002
    - 10.150.255.252 — head VIP
    - 10.150.255.253 — head02
    - 10.150.255.254 — head01
- Subnet: 172.x.x.x ??? — VAST internal network

## Switch configurations

### Common

```
terminal monitor  ! Show live logging
```

```
! Management

hostname :HOSTNAME

interface mgmt1/1/1
   no shutdown
   ip address dhcp

snmp-server community public ro

! Spanning tree

spanning-tree mode rstp

! VLANs

interface vlan1
   description default-vlan

interface vlan141
   description testcl-int

interface vlan150
   description umbrella-int
```

### Spine

```
! Spanning tree

spanning-tree rstp priority 16384

! Links to leaf switches

interface port-channel :INTID
   description "leaf LAG"
   switchport mode trunk
   switchport access vlan 1
   switchport trunk allowed vlan 150
   spanning-tree bpduguard disable

interface ethernet :INTID
   description "leaf LAG member"
   no switchport
   channel-group 1 mode active

! Links to nodes

interface ethernet :INTID
   switchport mode access
   switchport access vlan 150
   spanning-tree bpduguard enable

! Unused ports

interface ethernet :INTID
   shutdown
```

### Leaf

```
! Links to spine switches

interface port-channel 1
   description "spine LAG"
   switchport mode trunk
   switchport access vlan 1
   switchport trunk allowed vlan 150
   spanning-tree bpduguard disable

interface range ethernet 1/1/25-1/1/26
   description "spine LAG member"
   no switchport
   channel-group 1 mode active

! Links to nodes

interface range ethernet 1/1/1-1/1/24,1/1/27-1/1/30
   switchport mode access
   switchport access vlan 150
   spanning-tree bpduguard enable
```
