---
title: Administration Guide
---

!!! danger
    These are "internal" notes and require privileged accounts to execute. Please use with care!

## Hardware

### BMC Configuration

#### iDRAC Hostname
```shell
racadm set idrac.nic.dnsracname HOST-idrac
```

#### iDRAC Authentication
```{ .shell .annotate hl_lines="4" }
racadm set idrac.ipmilan.enable 1
racadm set idrac.ipmilan.orivlimit 3
racadm set idrac.users.4.username bright
racadm set idrac.users.4.password PASSWORD # (1)!
racadm set idrac.users.4.privilege 0x1F3
racadm set idrac.users.4.enable 1
```

1. Replace this value with the actual password which can be retrieved from our KeyPass database.

#### IPMI Authentication
```{ .shell .annotate hl_lines="3" }
module load ipmitool
ipmitool user set name 4 bright
ipmitool user set password 4 PASSWORD # (1)!
ipmitool user enable 4
```

1. Replace this value with the actual password which can be retrieved from our KeyPass database.

### Reboot HP servers
```shell
module load ipmitool
export HST_IP=$(dig -q arch-computeE003-ilo.infra.tue.nl @131.155.2.3 +short)
ipmitool -I lanplus -H $HST_IP -U Administrator -a chassis status
#ipmitool -I lanplus -H $HST_IP -U Administrator -a chassis power cycle
```

## Storage

### ZFS

#### Create ZFS pool
```shell
zpool create tank raidz sdb sdc cache sda
```

#### User Quota
On a storage node as root:

##### Get quota
```shell
zfs userspace tank/home
```

#####  Set quota
In this example we configure a quota of 4TB.
```shell
zfs set userquota@<ID>=4T tank/home
```

#### Group Quota
On a storage node as root:

##### Get quota
```shell
zfs groupspace tank/home
```

#####  Set quota
In this example we configure a quota of 1TB.
```shell
zfs set groupquota@<GroupName>=1T molml/home
```
