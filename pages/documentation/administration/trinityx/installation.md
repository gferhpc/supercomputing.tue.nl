# Installation

## Requirements

- Node with at least 2 NIC interfaces (public & internal network)
- [Rocky Linux](https://rockylinux.org){:target=_blank} 8.x
- iDrac access hpc-head01 : ***172.16.108.55*** hpc-head02 : ***172.16.108.56***

    ??? example "Configuration"

        **Localization**

        - Keyboard: English (US)
        - Language Support: English (United States)
        - Time & Date: Europe/Amsterdam
     
    
        **Software**

        - Software Selection: Minimal Install (Standard)

        **System**

          - Installation Destination: Local Standard Disks (sda), Storage Configuration: Automatic
          - Network & Hostname: Configure Network, Hostname: hpc-head0X.icts.tue.nl

        **User Settings**

          - Root Password: ********
          - User Creation: ********, Make this user administrator

## Server Configuration

As root@hpc-head0X 

**TIP**: use screen to mitigate connection loss during installation
```shell
dnf -y install screen
```

### Network Configuration

Configure internal network interface

=== "hpc-head01"

    ```shell
    export IFACE=ens3f0np0   

    nmcli connection add type ethernet con-name $IFACE
    nmcli con mod $IFACE ipv4.address 10.150.255.254/16
    nmcli con mod $IFACE ipv4.method manual
    nmcli con mod $IFACE connection.autoconnect true
    nmcli con up $IFACE
    ```

=== "hpc-head02"

    ```shell
    export IFACE=enp0s8    

    nmcli connection add type ethernet con-name $IFACE
    nmcli con mod $IFACE ipv4.address 10.150.255.253/16
    nmcli con mod $IFACE ipv4.method manual
    nmcli con mod $IFACE connection.autoconnect true
    nmcli con up $IFACE

    firewall-cmd --zone=trusted --change-interface=$IFACE --permanent
    firewall-cmd --reload
    ```

!!! Note

    Replace `enp0s8` with the name of your internal NIC.


### Update the OS

```shell
dnf -y install git
```

### Reboot System

```shell
reboot
```

## TrinityX Installation

### Prepare environment

As `root@hpc-head01`:

```shell
dnf -y install git
```

```shell
git clone https://github.com/clustervision/trinityX.git /root/trinityX
cd /root/trinityX

bash prepare.sh

cp site/group_vars/all.yml.example site/group_vars/all.yml
```

Review and edit the contents of the `all.yml` file accordingly, notable settings:

| Setting                      | Value                        | Description                                                 |
|------------------------------|------------------------------|-------------------------------------------------------------|
| administrator_email          | `hpc-umbrella@tue.nl`        | Email address of the administrator                          |
| project_id                   | `umbrella`                   | Project ID                                                  |
| ha                           | `false` (default)            | High Availability; _MUST remain `false` at time of writing_ |
| trix_ctrl1_ip                | `10.150.255.254 `            | IP controller node
| trix_ctrl1_bmcip             | `172.16.108.55`              | IP of iDRAC |
| trix_ctrl1_hostname          | `hpc-head01`                 | Hostname    |
| trix_external_fqdn           | `umbrella-cluster.hpc.tue.nl`| FQDN of the external interface of the cluster               |
| trix_dns_forwarders          | `[131.155.2.3, 131.155.3.3]` | List of DNS forwarders to use for the cluster.              |
| firewalld_public_interfaces  | `[eno1]`                   | List of public interfaces to use for the cluster.           |
| firewalld_trusted_interfaces | `[ens3f0np0]`                   | List of trusted interfaces to use for the cluster.          |

```shell
cp site/hosts.example site/hosts
```

Review and edit the contents of the `hosts` file accordingly.

```ini
[controllers]
hpc-head01 ansible_host=10.150.255.254 ansible_connection=local
#hpc-head02 ansible_host=10.150.255.253
```

### Installation

Run the ansible-playbook

```shell
cd /root/trinityX/site
ansible-playbook controller.yml
```

### Configuration

```shell
luna cluster change -n umbrella
```

```shell
obol user add demo -p demo
obol group addusers admins demo
```

Now the following Pages should available:

http://umbrella-cluster.hpc.tue.nl:8080  TrinityX (use demo:demo)

http://umbrella-cluster.hpc.tue.nl:3000  Grafana

http://umbrella-cluster.hpc.tue.nl:3001  Sensu

```shell
ansible-playbook compute-redhat.yml
luna osimage pack compute
```

```shell
luna group change -qpart part.txt compute
```

??? example "part.txt"
    
    ```shell
    parted /dev/sda -s 'mklabel gpt'
    parted /dev/sda -s 'mkpart efi fat32 1 1g'
    parted /dev/sda -s 'mkpart boot ext4 1g 2g'
    parted /dev/sda -s 'mkpart swap linux-swap 2g 4g'
    parted /dev/sda -s 'mkpart root ext4 4g 32g'
    parted /dev/sda -s 'mkpart local ext4 33g 100%'

    while [[ ! -b /dev/sda1 ]] || [[ ! -b /dev/sda2 ]] || [[ ! -b /dev/sda3 ]] || [[ ! -b /dev/sda4 ]] || [[ ! -b /dev/sda5 ]]; do sleep 1; done

    mkswap /dev/sda3
    swaplabel -L swappart /dev/sda3

    mkfs.fat -F 16 /dev/sda1
    mkfs.ext4 /dev/sda2
    mkfs.ext4 /dev/sda4
    mount /dev/sda4 /sysroot
    mkdir /sysroot/boot
    mkfs.ext4 /dev/sda5
    ```

```shell
luna group change -qpost post.txt compute
```
??? example "post.txt"
    
    ```shell
    cat << EOF >> /sysroot/etc/fstab
    /dev/sda4   /       ext4    defaults        1 1
    /dev/sda2   /boot   ext4    defaults        1 2
    /dev/sda1   /boot/efi   vfat    defaults        1 2
    /dev/sda3   swap    swap    defaults        0 0
    /dev/sda5   /local     ext4    defaults        1 1
    EOF
    SH=`chroot /sysroot /bin/bash -c "efibootmgr -v|grep Shim1|grep -oE '^Boot[0-9]+'|grep -oE '[0-9]+'"`
    if [ "$SH" ]; then
            echo 'Shim found on boot '$SH
            chroot /sysroot /bin/bash -c "efibootmgr -B -b $SH"
            echo Remove
            chroot /sysroot /bin/bash -c "efibootmgr -v"
            echo Clean
    fi
    chroot /sysroot /bin/bash -c "efibootmgr --verbose --disk /dev/sda --part 1 --create --label \"Shim1\" --loader /EFI/rocky/shimx64. efi"
    chroot /sysroot /bin/bash -c "grub2-mkconfig -o /boot/efi/EFI/rocky/grub.cfg"
    chroot /sysroot /bin/bash -c "systemctl set-default multi-user.target"

    umount /sysroot/sys
    umount /sysroot/dev
    umount /sysroot/proc
    ```

Authentication via AD
```shell
cat >> /etc/sssd/sssd.conf << EOF

auth_provider = krb5
krb5_server = campus.tue.nl
krb5_kpasswd = campus.tue.nl
krb5_realm = CAMPUS.TUE.NL
cache_credentials = True
EOF
systemctl restart sssd
```

*[NIC]: Network Interface Controller
