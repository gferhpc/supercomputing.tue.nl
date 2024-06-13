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

1. We moeten alle nodes eerst een keer rebooten met bright om de boot record te kunnen installeren. Deze stond initieel uit (zojuist aangepast). Als dit gedaan is, is de bootrecord correct aanwezig en kan de node zonder PXE booten. IE eerste stap van het onderhoudsmoment
2. Er zal geen (werkende) netwerkconfiguratie zijn, dus we moeten het IP adres statisch instellen in /etc/sysconfig/network-scripts/ifcfg-BOOTIF; specifiek moet je de DEVICE= goedzetten (eno1 in mijn test setup) gevolgd door systemctl restart network (or reboot van het systeem)
3. We kunnen gewoon in blijven loggen met het welbekende root wachtwoord, maar zou willen voorstellen om hiervoor een nieuwe private/public key te maken op de nieuwe headnode(s) en deze alvast klaar te zetten op de storage nodes. Zodat we hier zorgeloos op kunnen inloggen (wat ook nodig zal zijn om de quotas non-interactief in te kunnen stellen voor gebruikers).
4. PXE boot uitschakelen! Anders komt de server niet online en blijft deze "hangen" op de Luna boot-loader.
5. Zodra de node ontkoppeld is van Bright (en dus standalone kan booten), zullen er ook geen NFS exports aanwezig zijn. Deze zullen we zelf opnieuw moeten configureren. 
Kortom, het is mogelijk om de storage nodes los te koppelen van Bright en te kunnen gebruiken binnen TrinityX.

```shell
+ ssh arch-storage001 exportfs -v
/tank/home      10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)

+ ssh bme-storage001 exportfs -v
/tank/home      10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)
/molml/home     10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)

+ ssh chem-storage001 exportfs -v
/tank/scratch   10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)

+ ssh chem-storage002 exportfs -v
/tank/home      10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)

+ ssh mcs-storage001 exportfs -v
/tank/home      10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)

+ ssh mech-storage001 exportfs -v
/tank/home      10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)

+ ssh phys-storage001 exportfs -v
/tank/cmshared  10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)
/tank/home      10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)

+ ssh tue-storage001 exportfs -v
/tank/home      10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)
/tank/cmshared  10.141.0.0/16(async,wdelay,hide,no_subtree_check,sec=sys,rw,secure,no_root_squash,no_all_squash)
```
---
* [ ] **Login image for TrinityX**
* [x] tue-login001: connect to test cluster for testing
* [ ] cgroup/ulimit per user
* [x] Ansible script for OOD install on a specific login node (login001).
* [x] Install OOD/Certs to use https://hpc.tue.nl
---
* [x] **GPU image for TrinityX**
* [x] connect id-gpu for testing to test cluster
* [x] create GPU osimage (and group) with nvida-drivers Rocky8
* [x] test image on node (nvidia-smi)
* [x] create GPU osimage with nvidia 470 Drivers Rocky 8 for elec-gpuB001 : gpu-470drv
* [x] test slurm (--gpus=) GPU reservation on gpu-node  (Guus tested with his gpu-test1.job)
---
* [x] **test job submission as mortal user (submit, wait, see results)**
* [x] test OOD GUI session
---
* [x] **mail**
* [x] configure postfix relay on heads
* [x] configure postfix smarthost on compute images
* [x] configure postfix to read LDAP for aliases
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
* [x] **NTP**
* [x] ntpd on both head nodes
* [x] ntp config in compute images
---
* [x] **Munge**
* [x] munged on both head nodes
* [x] test
---
* [x] **Slurm controller**
* [x] test: who adds nodes to slurm config?  TrinityX or no-one: answer is no-one.
* [x] write the actual config
---
* [x] **Slurm DBD**
* [x] for now we worry not about HA; we try to make the underlaying DB HA
---
* [x] **MariaDB HA**
* [x] We postpone this to next maintenance
---
* [ ] **software installation**
* [x] keep /cm/shared only for old software
* [ ] make path plan for installations in /sw
* [x] put new installations in /sw on tue-storage001
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
---
* [x] **configure InfiniBand**
* [x] run OpenSM on at least a few compute nodes per fabric

### Rest

* Make network plan: which switch where
* Make VLAN/network config plan

* [x] connect head1/2 to mgmt VLAN
* [x] put mgmt switch in/close to X05
* [x] connect X05/06 mgmt to switch in X05
	(does network want to get rid of FEX in X07?)
* [x] put mgmt switch in W11

## Maintenance Plan

* [x] Configure VLAN
* [x] Replace Physical Head node(s)
* [x] Replace Bright Clustermanger with TrinityX
* [x] Update OS login/compute/gpu nodes
* [x] Update EasyBuild Applications/toolchains
* [x] Update Firmware
* [x] Fix mgmt on arch-switch001
* [x] upgrade tue-storage001 to 10 Gbit

## Post-maintenance

* [x] Remove TUe-side connections of storage nodes
* [x] Deregister storage node MAC addresses
* [x] Deregister storage nodes from Zabbix (already done)

* write script to periodically cleanup old osimage packs in: /trinity/local/luna/files

## Next maintenance

* MariaDB HA

### Replace Physical Headnode(s)

Current Head Nodes:
- hpc-primary.icts.tue.nl (131.155.2.51 - 10.141.255.254)
- hpc-secondary.icts.tue.nl (131.155.2.52 - 10.141.255.253) 
- VIP external hpc-cluster.tue.nl (131.155.2.50) 
- VIP internal master.cm.cluster (10.141.255.252)

New Head Nodes: 
- hpc-head01.icts.tue.nl (131.155.7.102 - 10.150.255.254)
- hpc-head02.icts.tue.nl (131.155.7.103 - 10.150.255.253)
- VIP external hpc-vip.icts.tue.nl (131.155.7.104)
- VIP internal controller.cluster (10.141.255.252)

# Maintenance log:

* tue-storage001: at each boot needs manual intervention: issue with PCIe device: PCIe link training failure observed in slot 3.
* head01/02: firewalld configs are very different; should be the same.
