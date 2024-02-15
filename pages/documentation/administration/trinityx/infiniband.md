# Infiniband

Some nodes are equipped with Infiniband.  To be useful, at least one node must run the Open Subnet Manager (OpenSM).

On hpc-head01:

Prepare the node image:

```shell
luna osimage clone compute compute-ib

lchroot compute-ib
dnf -y install opensm
systemctl enable opensm
echo blacklist qedr > /etc/modprobe.d/blacklist-qedr.conf
exit

luna osimage pack compute-ib
```

Make a group, change it to use the newly made node image:

```shell
luna group clone compute compute-ib
luna group change -o compute-ib compute-ib
```

Then move the respective nodes into the group.  Currently, these are:

* phys-computec
* phys-computed
* phys-computee
* phys-computef
* phys-computeg
* chem-computea
* chem-computef

# Running jobs on chem-computeF\*

The chem-computeF\* nodes have RoCE-compatible interfaces that show up out of the box.  These interfaces confuse OpenMPI.  To get rid of these interfaces, remove the `qedr` kernel module.  This module is blacklisted in the compute-ib image.

Alternatively, this works for OpenMPI commands:

```shell
FI_VERBS_IFACE=mlx5_0 UCX_NET_DEVICES=mlx5_0:1 mpirun my_command
```
