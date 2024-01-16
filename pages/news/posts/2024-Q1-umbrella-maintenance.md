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

* [x] Prepare transfer users/groups LDAP
* [ ] Transfer and Test Users (LDAP); Test UID/GID mapping

* [ ] Write fstab file

* [ ] test if Bright-storage nodes work without bright CM present
* [ ] tue-login001: install as storage node with bright
* [ ] connect node to test cluster
* [ ] test non-PXE boot & SSH login

* [ ] Login image for TrinityX
* [ ] tue-login001: connect to test cluster for testing
* [ ] cgroup/ulimit per user
* [ ] OOD

* [ ] GPU image for TrinityX
* [ ] connect id-gpu for testing to test cluster

* [ ] test job submission as mortal user (submit, wait, see results)
* [ ] test OOD GUI session

* [ ] mail
* [ ] configure postfix relay on heads
* [ ] configure postfix smarthost on compute images
* [ ] configure postfix to read LDAP for aliases

* [ ] (re-)write user creation script 

* [ ] DNS
* [ ] TrinityX: configure 2nd DNS server
* [ ] head2: configure as follower of head1

* [ ] DHCP
* [ ] implement active-active dhcpd

* [ ] NTP
* [ ] ntpd on both head nodes
* [ ] ntp config in compute images

* [ ] Munge
* [ ] test

* [ ] Slurm controller
* [ ] test: who adds nodes to slurm config?  TrinityX or no-one?  Can we make it no-one?
* [ ] can we write slurm config using own templates and Luna database?
* [ ] write the actual config

* [ ] Slurm DBD
* [x] for now we worry not about HA; we try to make the underlaying DB HA

* [x] MariaDB HA
* [x] We postpone this to next maintenance

* [ ] software installation
* [ ] keep /cm/shared only for old software
* [ ] make path plan for installations in /sw
* [ ] put new installations in /sw on tue-storage001

* [ ] configure regular backups of databases etc.
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
