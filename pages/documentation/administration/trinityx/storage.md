Export NFS on storage nodes

=== "tue-storage001"
    
    ```shell
    # Create datasets
    zfs create tank/sw      # for: /sw
    zfs create tank/ohpc    # for: /trinity/ohpc
    zfs create tank/trinity # for: /trinity/shared

    # Configure NFS exports
    zfs set sharenfs='rw=@10.150.0.0/16,async,no_root_squash,no_all_squash' tank/sw
    zfs set sharenfs='rw=@10.150.0.0/16,async,no_root_squash,no_all_squash' tank/ohpc
    zfs set sharenfs='rw=@10.150.0.0/16,async,no_root_squash,no_all_squash' tank/trinity

    zfs set sharenfs='rw=@10.150.0.0/16,async,no_root_squash,no_all_squash' tank/home
    ```

### On all head nodes:
```shell
mkdir -p /sw /trinity/ohpc /trinity/shared 
mkdir -p /home/tue /home/arch001 /home/bme001 /home/bme002 /home/chem002 /home/mcs001 /home/phys /home/mech001 /home/elec001
mkdir -p /scratch/chem001
```

## fstab

```
10.150.254.1:/tank/sw      /sw              nfs     defaults,bg,soft,_netdev     0 0
10.150.254.1:/tank/ohpc    /trinity/ohpc    nfs     defaults,bg,soft,_netdev     0 0
10.150.254.1:/tank/trinity /trinity/shared  nfs     defaults,bg,soft,_netdev     0 0

10.150.254.1:/tank/home    /home/tue        nfs     defaults,bg,soft,_netdev     0 0
10.150.254.11:/tank/home   /home/phys       nfs     defaults,bg,soft,_netdev     0 0
10.150.254.21:/tank/home   /home/arch001    nfs     defaults,bg,soft,_netdev     0 0
10.150.254.31:/tank/home   /home/bme001     nfs     defaults,bg,soft,_netdev     0 0
10.150.254.31:/molml/home  /home/bme002     nfs     defaults,bg,soft,_netdev     0 0
10.150.254.41:/tank/home   /home/mech001    nfs     defaults,bg,soft,_netdev     0 0
10.150.254.51:/tank/home   /home/mcs001     nfs     defaults,bg,soft,_netdev     0 0
10.150.254.61:/tank/scratch /scratch/chem001 nfs    defaults,bg,soft,_netdev     0 0
10.150.254.62:/tank/home   /home/chem002    nfs     defaults,bg,soft,_netdev     0 0
10.150.254.71:/tank/home   /home/elec001    nfs     defaults,bg,soft,_netdev     0 0
```

# Clean install

1. Install Rocky 8.
    - Like head nodes; see [here](installation.md).
    - Hostname: e.g. `tue-storage001.cluster`
    - IP address: fixed from 10.150.254.x/16.  Update networking.md accordingly.
    - Gateway: 10.150.255.252
    - DNS servers: 10.150.255.253,10.150.255.254
    - DNS search domains: cluster

```shell
dnf -y install epel-release https://zfsonlinux.org/epel/zfs-release-2-3.el8.noarch.rpm
dnf -y update
dnf -y remove mlocate
dnf -y install iotop iftop screen

dnf -y install lldpd
systemctl enable --now lldpd.service

dnf -y install zfs nfs-utils
systemctl enable --now nfs-server.service
firewall-cmd --add-service={nfs,nfs3,mountd,rpc-bind} --permanent
reboot

zpool import -f tank
```
