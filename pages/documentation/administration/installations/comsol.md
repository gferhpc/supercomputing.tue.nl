# COMSOL

## VERSION=62 VERSION_WITH_A_DOT=6.2

As a user on your laptop:

From/on the WebSite, Download the COLSOL <VERSION> Windows/Linux DVD ISO.

copy the COMSOL<VERSION>_dvd.iso to the login node into /local/COMSOL.

As root on login node (no need for X11), mount the *.iso on /mnt/iso: 
```shell
mount -o loop /local/COMSOL/COMSOL<VERSION>_dvd.iso /mnt/iso
```
Create a /local/COMSOL/setupconfig.ini for automated install (based on /mnt/iso/setupconfig.ini)

```{ .ini }
installdir = /cm/shared/apps/comsol/VERSION_WITH_A_DOT/multiphysics
installmode = install
repair = 0
showgui = 0
quiet = 0
agree = 1
license = 1718@tuelicense.campus.tue.nl
comsol = 1
licmanager = 0
llexcelallusers = 0
doc = no
applications = all
licmanager.service = 0
startmenushortcuts = 0
desktopshortcuts = 0
linuxlauncher = 0
symlinks = 0
fileassoc = 0
checkupdate = 0
firewall = 0
setsecuritypolicy = 0
security.external.enable = 0
server.port = 2036
server.service = 0
server.service.start = manual
server.createadmin = 0
server.multiple = 0
server.primary = 0
server.windowsauthentication = 0
```

```shell
cd /mnt/iso
./setup -s /local/COMSOL/setupconfig.ini
```

Create a module: `/cm/shared/modulefiles/comsol/<VERSION_WITH_A_DOT>`
