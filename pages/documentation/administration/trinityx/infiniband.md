# Infiniband

Some nodes are equipped with Infiniband.  To be useful, at least one node must run the Open Subnet Manager (OpenSM).

On hpc-head01:

Prepare the node image:

```shell
luna osimage clone compute compute-ib

lchroot compute-ib
dnf -y install opensm
systemctl enable opensm
exit
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
