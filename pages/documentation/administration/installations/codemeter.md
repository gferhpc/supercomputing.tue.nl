# CodeMeter

Code Meter License Server needs a USB Dongle available in phys-login001
```shell
# lsusb
Bus 001 Device 003: ID 064f:2af9 WIBU-Systems AG CmStick (HID, article no. 1001-xx-xxx)
```

64bit linux rpm can be downloaded from [https://www.wibu.com/support/user/user-software.html](https://www.wibu.com/support/user/user-software.html){:target=_blank}

```shell
yum install ./CodeMeter-X.XX.XXX.x86_64.rpm
systemctl stop codemeter-webadmin.service
systemctl disable codemeter-webadmin.service
systemctl disable codemeter.service
systemctl stop codemeter.service
/etc/wibu/CodeMeter/Server.ini:
BindAddress=10.141.0.20
IsNetworkServer=1
```

```shell
tcp        0      0 127.0.0.1:22350         0.0.0.0:*               LISTEN      3097060/CodeMeterLi
tcp        0      0 10.141.0.20:22350       0.0.0.0:*               LISTEN      3097060/CodeMeterLi
```

!!! note
    Create service codemeter for node phys-login001 in Bright ClusterManager