# Installation

## Requirements

- [Rocky Linux](https://rockylinux.org){:target=_blank} 8.x (= preferred) or 9.x
- At least 2 NIC interfaces (public & internal network)

### Required packages
```shell
dnf install git
```

### Network Configuration

#### Primary

Configure internal network interface
```shell
export NWNAME=enp0s8
nmcli connection add type ethernet con-name $NWNAME
nmcli con mod $NWNAME ipv4.address 10.141.255.254/16
nmcli con mod $NWNAME ipv4.method manual
nmcli con mod $NWNAME connection.autoconnect true
nmcli con up $NWNAME
```

!!! Note

    Replace `ens19` with the name of your internal NIC.

#### Secondary

Configure internal network interface
```shell
export NWNAME=enp0s8
nmcli connection add type ethernet con-name $NWNAME
nmcli con mod $NWNAME ipv4.address 10.141.255.253/16
nmcli con mod $NWNAME ipv4.method manual
nmcli con mod $NWNAME connection.autoconnect true
nmcli con up $NWNAME
```

!!! Note

    Replace `enp0s8` with the name of your internal NIC.

### NTP Configuration

```shell
timedatectl set-timezone Europe/Amsterdam
cat > /etc/chrony.conf << EOF
allow 10.141.0.0/16
local stratum 10 
server ntp1.tue.nl
server ntp2.tue.nl
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
keyfile /etc/chrony.keys
leapsectz right/UTC
logdir /var/log/chrony
EOF
```

## Installation


### Prepare environment

As root: 

```shell
git clone https://github.com/clustervision/trinityX.git /root/trinityX
cd /root/trinityX

bash prepare.sh

cp /root/trinityX/site/group_vars/all.yml.example /root/trinityX/site/group_vars/all.yml
```

Review and edit the contents of the `all.yml` file accordingly.

*[NIC]: Network Interface Controller
