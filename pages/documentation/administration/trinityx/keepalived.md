# VIP (keepalived) Installation  

## Requirements

A succesfull (Non HA) installation (hpc-head01) of TrinityX using the ansible-playbook.

A second server (hpc-head02) with a basic Rocky 8 install and server Setup done (see [installation](https://supercomputing.tue.nl/documentation/administration/trinityx/installation/))

## Server Configuration

### Heartbeat network

```shell
export IFACE=eno2   

nmcli connection add type ethernet con-name $IFACE
nmcli con mod $IFACE ipv4.method auto
nmcli con mod $IFACE connection.autoconnect true
nmcli con up $IFACE
```


### VIP Configuration with keepalived

Run on both hosts unless otherwise indicated.


```shell
dnf -y install keepalived
```

```shell

firewall-cmd --add-rich-rule='rule protocol value="vrrp" accept' --zone=public --permanent
firewall-cmd --reload
```

=== "hpc-head01"

    ```shell
    cat > /etc/keepalived/keepalived.conf << EOF
    vrrp_instance VI_1 {
        state MASTER
        interface eno1
        virtual_router_id 50
        priority 200
        advert_int 1
        authentication {
              auth_type PASS
              auth_pass <PASSWD01>
        }
        virtual_ipaddress {
             131.155.7.104/27
        }
    }
    vrrp_instance VI_2 {
        state MASTER
        interface ens3f0np0
        virtual_router_id 51
        priority 200
        advert_int 1
        authentication {
              auth_type PASS
              auth_pass <PASSWD02>
        }
        virtual_ipaddress {
              10.150.255.252/16
        }
    }
    EOF
    ```

=== "hpc-head02"

    ```shell
    cat > /etc/keepalived/keepalived.conf << EOF
    vrrp_instance VI_1 {
        state BACKUP
        interface eno1
        virtual_router_id 50
        priority 100
        advert_int 1
        authentication {
              auth_type PASS
              auth_pass <PASSWD01>
        }
        virtual_ipaddress {
             131.155.7.104/27
        }
    }
    vrrp_instance VI_2 {
        state BACKUP
        interface ens3f0np0
        virtual_router_id 51
        priority 100
        advert_int 1
        authentication {
              auth_type PASS
              auth_pass <PASSWD02>
        }
        virtual_ipaddress {
              10.150.255.252/16
        }
    }
    EOF
    ```
```shell
systemctl enable keepalived --now
```
