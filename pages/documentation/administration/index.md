---
title: Administration Guide
---

!!! danger
    These are "internal" notes and require privileged accounts to execute. Please use with care!

## Training, Courses & Resources
- [Bright View Admin Portal](https://hpc-cluster.tue.nl/bright-view/){:target=_blank}
- [Bright User Portal](https://hpc-cluster.tue.nl/userportal/){:target=_blank}
- [Bright Cluster Manager online training (free)](https://academy.nvidia.com/en/training-search-wizard/?mySearch=bright%20cluster%20manager){:target=_blank}
- [NVIDIA Bright Cluster Manager Customer Portal](https://customer.brightcomputing.com/){:target=_blank}

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

## Slurm Accounting
Script written by Wouter Ellenbroek after an idea by Bart de Braaf. The
maintainers of this Wiki do not accept any responsibility for damage
incurred by using this script.

```python
#!/usr/bin/python3

import subprocess;

users=subprocess.check_output('squeue -O "username:14" |tail -n +2|sort|uniq',shell=True)
userlist=users.decode().splitlines()
print("USER          RUNNING/PENDING (REASONS)")
for user in userlist:
    #user=user.strip()
    nrunning=subprocess.check_output("squeue -u {!s} -t R -O numtasks |tail -n +2".format(user),shell=True).decode().splitlines()
    nrunning=[int(x) for x in nrunning]
    nrunning=sum(nrunning)
    npending=subprocess.check_output("squeue -u {!s} -t PD -O numtasks |tail -n +2".format(user),shell=True).decode().splitlines()
    npending=[int(x) for x in npending]
    npending=sum(npending)
    if (npending==0): 
        print("{:s}: {:d}/0".format(user,nrunning))
    else:
        reasons=subprocess.check_output("squeue -u {!s} -t PD -O reason | tail -n +2 |sort|uniq".format(user),shell=True).decode().splitlines()
        reasons=[x.strip() for x in reasons]
        reasons=','.join(reasons)
        print("{:s}: {:d}/{:d}\t({:s})".format(user,nrunning,npending,reasons))
```