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
mkdir -p /sw /trinity/ohpc /trinity/shared /home/tue /home/arch001 /home/bme001 /home/bme002 /home/chem002 /home/mcs001 /home/phys
```

## fstab

```
10.150.254.1:/tank/home    /home/tue        nfs     defaults,bg,_netdev     0 0
10.150.254.1:/tank/sw      /sw              nfs     defaults,bg,_netdev     0 0
10.150.254.1:/tank/ohpc    /trinity/ohpc    nfs     defaults,bg,_netdev     0 0
10.150.254.1:/tank/trinity /trinity/shared  nfs     defaults,bg,_netdev     0 0
```
