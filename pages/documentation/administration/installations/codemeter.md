# CodeMeter

Code Meter License Server needs a USB Dongle available in phys-login001
```shell
# lsusb
Bus 001 Device 003: ID 064f:2af9 WIBU-Systems AG CmStick (HID, article no. 1001-xx-xxx)
```

64bit linux rpm can be downloaded from [https://www.wibu.com/support/user/user-software.html](https://www.wibu.com/support/user/user-software.html){:target=_blank} (Search for "rpm")

```shell
yum install ./CodeMeter-X.XX.XXX.x86_64.rpm
systemctl stop codemeter-webadmin.service
systemctl disable codemeter-webadmin.service
systemctl stop codemeter.service
/etc/wibu/CodeMeter/Server.ini:
BindAddress=<IP of phys-login001.cluster>
IsNetworkServer=1
```
```shell
tcp        0      0 127.0.0.1:22350         0.0.0.0:*               LISTEN      3097060/CodeMeterLi
tcp        0      0 <IP of phys-login001.cluster>:22350       0.0.0.0:*               LISTEN      3097060/CodeMeterLi
```
```shell
systemctl enable codemeter.service --now
```
