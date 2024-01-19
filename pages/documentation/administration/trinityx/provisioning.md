# Installation

## Requirements

- A succesfull (Non HA) installation of TrinityX using the ansible-playbook
- A succesfill creation a compute image using the ansible-playbook (compute-redhat.yml)
- part.txt and post.txt are added to the part/post of the compute image 

## Use luna to creates nodes to provision

tue-computeb001 - 14:23:F2:DD:BA:90 - ipmi 172.16.108.57
tue-computeb002 - 14:23:F2:DD:B2:D0 - ipmi 172.16.108.58

```shell
luna node clone node001 tue-computeb001 
luna node changeinterface -M 14:23:F2:DD:BA:90 tue-computeb001 BOOTIF
luna node changeinterface -I 172.16.108.57 tue-computeb001 BMC
luna node remove node001
luna node remove node002
luna node remove node003
luna node remove node004
luna node clone tue-computeb001 tue-computeb002 
luna node changeinterface -M 14:23:F2:DD:B2:D0 tue-computeb001 BOOTIF
luna node changeinterface -I 172.16.108.57 tue-computeb001 BMC
```

### GPU Nodes
```shell

```

### GPU packages
```
dnf -y install kmod-nvidia
```
