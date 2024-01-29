# Installation

![SLURM Logo](slurm.png){ align=right heigth="100" }

## Requirements

A succesfull (Non HA) installation of TrinityX using the ansible-playbook.

A second server (hpc-head02) with a basic Rocky 8 install

## Server Configuration

To allow hpc-head02 (the second server) to use the same packages as hpc-head01, add /etc/yum.repos.d/openhpc-base.repo and /etc/yum.repos.d/openhpc-updates.repo
```shell
cat > /etc/yum.repos.d/openhpc-base.repo << EOF
[openhpc-base]
baseurl = http://repos.openhpc.community/OpenHPC/2/EL_8/
gpgcheck = 0
gpgkey = 
name = openhpc-base
EOF
cat > /etc/yum.repos.d/openhpc-update.repo << EOF
[openhpc-updates]
baseurl = http://repos.openhpc.community/OpenHPC/2/update.2.6.2/EL_8/
gpgcheck = 0
gpgkey = 
name = openhpc-updates
EOF
```
Install slurmd and slurmctld
```shell
dnf install slurm-slurmd-ohpc slurm-slurmctld-ohpc slurm-slurmdbd-ohpc slurm-libpmi-ohpc slurm-contribs-ohpc slurm-devel-ohpc
```
Mount the /trinity/shared directory
```shell
mkdir -p /trinity/shared
mount hpc-head01:/trinity/shared /trinity/shared
```