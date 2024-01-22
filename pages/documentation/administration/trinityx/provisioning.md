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

## Use luna to creates nodes to provision

| GROUP       | NAME                  | BOOTIF MAC        | IPMI            |
|---------    |-----------------------|-------------------|-----------------|
| compute     | tue-computeb001       | 14:23:f2:dd:bA:90 | 172.16.108.57   | 
| compute     | tue-computeb002       | 14:23:f2:dd:b2:d0 | 172.16.108.58   |
| login       | tue-login001          | 50:9a:4c:a5:f3:c0 | 172.16.108.150  |

```shell
luna node add -g $GROUP -if BOOTIF -M $MAC $NAME
luna node changeinterface -N ipmi -I $IPMI $NAME BMC
```

## GPU packages
```
dnf -y install kmod-nvidia
```
