# Networking

## VLANs

### Cluster internal

- 1: `default-vlan`
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
        - hpc-vast-mgmt-1: VIP for web interface

VAST:

- Subnet: 172.16.0.0/16 --- VAST internal data
    - Range can be moved, but must be a /16.
- Subnet: 172.17.0.0/16 --- VAST internal Docker
    - Range can be moved, but must be a /16.
- For user-facing data streams: 4 IPs per CNode per pool

### Cluster internal

- Subnet: 10.148.0.0/16 - Umbrella Cluster heartbeat
- Subnet: 10.149.0.0/16 — Umbrella Cluster InfiniBand
- Subnet: 10.150.0.0/16 — Umbrella Cluster Ethernet
    - 10.150.0.1 — first node; nodes number upwards from here
    - 10.150.128–135.x — DHCP pool
    - 10.150.250.1–16 — VAST storage
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

Enter configure mode with

```
configure terminal
```

In configure mode:

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

interface vlan150
   description umbrella-int
```

Exit configure mode with `exit`.

Write configuration to flash with `write memory`.

### Spine

Per spine switch, we reserve the following ports:

* 1-4: VAST
* (5-8: reserved for future VAST)
* 9-10: devices in same rack (breakout to 4x25Gb)
* (11-14: free)
* 15-16: VLTi
* 17-31: leaf switches  (15x)
* 32: uplink to TU/e

In configure mode:

```
! Spanning tree

spanning-tree rstp priority 16384

! VLT
!
! Make sure to substitute the correct mgmt IP addresses below.

default interface range ethernet 1/1/15-1/1/16

interface range ethernet 1/1/15-1/1/16
   description VLTi
   no switchport
   no flowcontrol receive
   no flowcontrol transmit
   no shutdown

vlt-domain 1
   vlt-mac CA:C9:94:8E:33:9A
   ! backup destination 172.16.108.xxx vrf management   ! On spine 1, use mgmt address of spine 2
   ! backup destination 172.16.108.138 vrf management   ! On spine 2, use mgmt address of spine 1
   ! Peer routing is not currently configured.

discovery-interface ethernet 1/1/15-1/1/16
```
VAST: 100 Gbit, VLAN tagged, BPDU guard
```
! eth 1/1/1-1/1/4: VAST

interface range ethernet 1/1/1-1/1/4
   description VAST
   switchport mode trunk
   switchport access vlan 1
   switchport trunk allowed vlan 150
   spanning-tree bpduguard enable
   spanning-tree port type edge
   no shutdown

! eth 1/1/5-1/1/8: unused

default interface range ethernet 1/1/5-1/1/8
```
Links to devices: breakout too 25 Gbit, VLAN untagged, BPDU guard
```
! eth 1/1/9-1/1/10: links to devices  @ 25 Gbit

interface breakout :INTID map 25g-4x

interface ethernet :INTID
   switchport mode access
   switchport access vlan 150
   spanning-tree bpduguard enable
   spanning-tree port type edge
```
Link to leaf switch: 100 Gbit, VLAN tagged, LACP, NO BPDU guard
```
! Links to leaf switches
!
! :PCID  is the port channel ID
! :INTID  is the ethernet interface ID

interface port-channel :PCID
   description leaf-LAG
   switchport mode trunk
   switchport access vlan 1
   switchport trunk allowed vlan 150
   vlt-port-channel :PCID

interface ethernet :INTID
   description leaf-LAG-member
   no switchport
   channel-group :PCID mode active
```
Link to TU/e
```
! Link to TU/e
!
! Not implemented yet.
```
Everything else:
```
! Unused ports
!
! OS10 default on S5232 is shutdown

default interface ethernet :INTID
```

### Leaf

In configure mode:

```
! Links to spine switches

interface port-channel 1
   description spine-LAG
   switchport mode trunk
   switchport access vlan 1
   switchport trunk allowed vlan 150

interface range ethernet 1/1/25-1/1/26
   description spine-LAG-member
   no switchport
   channel-group 1 mode active

! Inter-switch links
! These remain until the spine is operational.

interface range ethernet 1/1/27-1/1/30
   description inter-switch
   switchport mode trunk
   switchport access vlan 1
   switchport trunk allowed vlan 150

! Links to nodes
! Once spine is operational, all ports can become node ports.
! Then: internet range ethernet 1/1/1-1/1/24,1/1/27-1/1/30

interface range ethernet 1/1/1-1/1/24
   description umbrella-node
   switchport mode access
   switchport access vlan 150
   spanning-tree bpduguard enable
   spanning-tree port type edge
```

For M1000e chassis:

```
! Port channel to M1000e chassis switches

interface port-channel 10       ! Use unique port channel ID
   description umbrella-chassis
   switchport mode access
   switchport access vlan 150
   spanning-tree bpduguard enable
   spanning-tree port type edge

interface range ethernet 1/1/1-1/1/4   ! Substitute correct interfaces
   description umbrella-chassis-LAG-member
   no switchport
   channel-group 10 mode active     ! substitute port channel ID

```

On the chassis switch itself:

```
enable  ! Password see KeePass
configure terminal

interface range gigabitethernet 1/0/17-20
   no channel-group
   channel-group 1 mode active

interface port-channel 1
   spanning-tree disable
   spanning-tree portfast

exit
exit
write memory
```
