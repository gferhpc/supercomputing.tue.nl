# Installation

## Requirements

- A succesfull (Non HA) installation of TrinityX using the ansible-playbook
- A succesfill creation a compute image using the ansible-playbook (compute-redhat.yml)
- part.txt and post.txt are added to the part/post of the compute image 

## Cleanup luna nodes that are auto-created
```shell
luna node remove node001
luna node remove node002
luna node remove node003
luna node remove node004
```

## Create the extra node groups and osimages
```shell
luna osimage clone compute gpu
luna group clone compute gpu -o gpu
luna osimage clone compute login
luna group clone compute login -o login
```


```shell
# Compute
export GROUP=compute NAME=tue-computeX001 MAC=00:00:00:00:00 IPMI=172.16.0.0
# GPU
export GROUP=gpu NAME=tue-gpuX001 MAC=00:00:00:00:00 IPMI=172.16.0.0
# LOGIN
export GROUP=login NAME=tue-login001 MAC=00:00:00:00:00 IPMI=172.16.0.0

luna node add -g $GROUP -if BOOTIF -M $MAC $NAME
luna node changeinterface -N ipmi -I $IPMI $NAME BMC
```

## Use luna to creates nodes to provision

| Name                      | BOOTIF MAC          | ipmi IP         |
|---------------------------|---------------------|-----------------|
| tue-computeb001           | 14:23:f2:dd:bA:90   | 172.16.108.57   | 
| tue-computeb002           | 14:23:f2:dd:b2:d0   | 172.16.108.58   |
| tue-login001              | 50:9a:4c:a5:f3:c0.  | 172.16.108.150  |

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

### Provision Nodes (from scratch)
```shell
# Compute
export GROUP=compute NAME=tue-computeX001 MAC=00:00:00:00:00 IPMI=172.16.0.0
# GPU
export GROUP=gpu NAME=tue-gpuX001 MAC=00:00:00:00:00 IPMI=172.16.0.0
# LOGIN
export GROUP=login NAME=tue-login001 MAC=00:00:00:00:00 IPMI=172.16.0.0

luna node add -g $GROUP -if BOOTIF -M $MAC $NAME
luna node changeinterface -N ipmi -I $IPMI $NAME BMC
```

### GPU packages
```
dnf -y install kmod-nvidia
```
