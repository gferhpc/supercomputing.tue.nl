# Installation

## Requirements

- A succesfull (Non HA) installation of TrinityX using the ansible-playbook
- A succesfill creation a compute image using the ansible-playbook (compute-redhat.yml)
- part.txt and post.txt are added to the part/post of the compute image 

## Use luna to creates nodes to provision

tue-computeb001 - c4:cb:e1:a8:f2:76
tue-computeb002 - c4:cb:e1:a8:e8:7a

```shell
luna node clone node001 tue-computeb001 
luna node change tue-computeb001 -if BOOTIF -M 14:23:F2:DD:BA:90
luna node remove node001
luna node remove node002
luna node remove node003
luna node remove node004
luna node clone tue-computeb001 tue-computeb002 
luna node change tue-computeb001 -if BOOTIF -M 14:23:F2:DD:B2:D0
```
