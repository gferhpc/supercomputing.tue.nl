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
nmcli con mod ens19 ipv4.address 10.141.255.254/16
nmcli con mod ens19 ipv4.method manual
nmcli con mod ens19 connection.autoconnect true
nmcli con up ens19
```

!!! Note

    Replace `ens19` with the name of your internal NIC.

#### Secondary

Configure internal network interface
```shell
nmcli con mod ens19 ipv4.address 10.141.255.253/16
nmcli con mod ens19 ipv4.method manual
nmcli con mod ens19 connection.autoconnect true
nmcli con up ens19
```

!!! Note

    Replace `ens19` with the name of your internal NIC.

## Installation


### Prepare environment

```shell
git clone https://github.com/clustervision/trinityX.git /root/trinityX
cd /root/trinityX

bash prepare.sh

cp /root/trinityX/site/group_vars/all.yml.example /root/trinityX/site/group_vars/all.yml
```

Review and edit the contents of the `all.yml` file accordingly.

*[NIC]: Network Interface Controller
