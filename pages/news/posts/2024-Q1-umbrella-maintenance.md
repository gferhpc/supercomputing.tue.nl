---
draft: true
date: 2024-01-20
categories: [Umbrella HPC Cluster]
authors: [a.van.hoof@tue.nl, e.loomeijer@tue.nl, a.c.m.bertens@tue.nl]
---

# 2024-Q1 Umbrella HPC Cluster maintenance completed 

TBD.

<!-- more -->

# Changelog

## Pre Maintenance

### TrinityX

* [x] **Prepare transfer users/groups LDAP**
* [ ] Transfer and Test Users (LDAP); Test UID/GID mapping
---
* [ ] **Write fstab file**
---
* [x] **test if Bright-storage nodes work without bright CM present**
* [x] tue-login001: install as storage node with bright
* [x] connect node to test cluster
* [x] test non-PXE boot & SSH login

    > 1. We moeten alle nodes eerst een keer rebooten met bright om de boot record te kunnen installeren. Deze stond initieel uit (zojuist aangepast). Als dit gedaan is, is de bootrecord correct aanwezig en kan de node zonder PXE booten. IE eerste stap van het onderhoudsmoment
	> 2. Er zal geen (werkende) netwerkconfiguratie zijn, dus we moeten het IP adres statisch instellen in /etc/sysconfig/network-scripts/ifcfg-BOOTIF; specifiek moet je de DEVICE= goedzetten (eno1 in mijn test setup) gevolgd door systemctl restart network (or reboot van het systeem)
	> 3. We kunnen gewoon in blijven loggen met het welbekende root wachtwoord, maar zou willen voorstellen om hiervoor een nieuwe private/public key te maken op de nieuwe headnode(s) en deze alvast klaar te zetten op de storage nodes. Zodat we hier zorgeloos op kunnen inloggen (wat ook nodig zal zijn om de quotas non-interactief in te kunnen stellen voor gebruikers).
	> 4. Zodra de node ontkoppeld is van Bright (en dus standalone kan booten), zullen er ook geen NFS exports aanwezig zijn. Deze zullen we zelf opnieuw moeten configureren. 
Kortom, het is mogelijk om de storage nodes los te koppelen van Bright en te kunnen gebruiken binnen TrinityX.
---
* [ ] **Login image for TrinityX**
* [ ] tue-login001: connect to test cluster for testing
* [ ] cgroup/ulimit per user
* [ ] OOD
---
* [ ] **GPU image for TrinityX**
* [ ] connect id-gpu for testing to test cluster
---
* [ ] **test job submission as mortal user (submit, wait, see results)**
* [ ] test OOD GUI session
---
* [ ] **mail**
* [ ] configure postfix relay on heads
* [ ] configure postfix smarthost on compute images
* [ ] configure postfix to read LDAP for aliases
---
* [/] **(re-)write user creation script **
---
* [ ] **DNS**
* [ ] TrinityX: configure 2nd DNS server
* [ ] head2: configure as follower of head1
---
* [ ] **DHCP**
* [ ] implement active-active dhcpd
---
* [ ] **NTP**
* [ ] ntpd on both head nodes
* [ ] ntp config in compute images
---
* [ ] **Munge**
* [ ] test
---
* [ ] **Slurm controller**
* [ ] test: who adds nodes to slurm config?  TrinityX or no-one?  Can we make it no-one?
* [ ] can we write slurm config using own templates and Luna database?
* [ ] write the actual config
---
* [ ] **Slurm DBD**
* [x] for now we worry not about HA; we try to make the underlaying DB HA
---
* [x] **MariaDB HA**
* [x] We postpone this to next maintenance
---
* [ ] **software installation**
* [ ] keep /cm/shared only for old software
* [ ] make path plan for installations in /sw
* [ ] put new installations in /sw on tue-storage001
---
* [ ] **configure regular backups of databases etc.**
* [ ] MariaDB
* [ ] /trinity/shared
* [x] slurm config
* [x] modulefiles
* [x] installed apps
* [ ] slurm state files ??? (necessary?)
* [ ] compute images
* [ ] head nodes /etc

### Rest

* Make network plan: which switch where
* Make VLAN/network config plan

* [ ] connect head1/2 to mgmt VLAN
* [ ] put mgmt switch in/close to X05
* [ ] connect X05/06 mgmt to switch in X05
	(does network want to get rid of FEX in X07?)
* [ ] put mgmt switch in W11

## Maintenance Plan

* Configure VLAN
* Replace Physical Head node(s)
* Replace Bright Clustermanger with TrinityX
* Update OS login/compute/gpu nodes
* Update EasyBuild Applications/toolchains
* Update Firmware
* Fix mgmt on arch-switch001
* [ ] upgrade tue-storage001 to 10 Gbit

## Post-maintenance

* Remove TUe-side connections of storage nodes
* Deregister storage node MAC addresses
* Deregister storage nodes from Zabbix

## Next maintenance

* MariaDB HA

### Replace Physical Headnode(s)

Current Head Nodes:
- hpc-primary.icts.tue.nl (131.155.2.51 - 10.141.255.254)
- hpc-secondary.icts.tue.nl (131.155.2.52 - 10.141.255.253) 
- VIP external hpc-cluster.tue.nl (131.155.2.50) 
- VIP internal master.cm.cluster (10.141.255.252)

New Head Nodes: 
- hpc-head01.icts.tue.nl (131.155.7.102 - 10.141.100.100)
- hpc-head02.icts.tue.nl (131.155.7.103 - 10.141.100.101)
- VIP external hpc-vip.icts.tue.nl (131.155.7.104)
