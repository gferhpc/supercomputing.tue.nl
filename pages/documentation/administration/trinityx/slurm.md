# Installation

![SLURM Logo](slurm.png){ align=right heigth="100" }

## Requirements

A succesfull (Non HA) installation of TrinityX using the ansible-playbook.

A second server (hpc-head02) with a basic Rocky 8 install

## Server Configuration

As root on **hpc-head02**

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
Make /etc/slurm link to /trinity/shared/etc/slurm
```shell
ln -s /trinity/shared/etc/slurm /etc/slurm
```
Slurm needs to have the same uid and gid as on hpc-head01
```shell
groupmod -g 891 slurm
usermod -g 891 -u 891 slurm
```
Create /var/log/slurm
```shell
mkdir -p /var/log/slurm
chown -R slurm:slurm /var/log/slurm
chmod o-rx /var/log/slurm
```
Munge needs to have the same uid and gid as on hpc-head01
```shell
groupmod -g 892 munge
usermod -g 892 -u 892 munge
chown -R munge:munge /etc/munge
chown -R munge:munge /var/log/munge
chown -R munge:munge /var/lib/munge
```
Add an overwrite to the systemd service for munge
```shell
mkdir /etc/systemd/system/munge.service.d/
cat > /etc/systemd/system/munge.service.d/trinity.conf << EOF
[Unit]
After=remote-fs.target
Requires=remote-fs.target

[Service]
ExecStart=
ExecStart=/usr/sbin/munged --key-file /trinity/shared/etc/munge/munge.key
EOF
```
Enable and start munge service
```shell
systemctl enable munge --now
```

## Database configuration

Allow all hosts to access the slurm_accounting database (limited to `localhost` by default)

```shell
hpc-head01# mysql -uroot
```

```mysql
UPDATE `mysql`.`user` SET `Host` = '%' WHERE `User` = 'slurm_accounting';
```