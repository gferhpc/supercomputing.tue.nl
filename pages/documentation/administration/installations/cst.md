# CST Studio Suite

## Requirement

The following 2 system dependencies are required on all compute & gpu nodes

```shell
dnf -y install redhat-lsb-core xorg-x11-server-Xvfb
```

In addition, you'll need to installation files of CST (provided by end-user)

## Installation

1. unknown (will document on next release)

### License

Replace in `%install_path%/LinuxAMD64/cst_settings.conf`:
```shell
#
# !!! NOTE !!!
#

# The settings below will automatically overwrite user-wise
# configuration entries but only if
#
#  a) <INSTALLDIR>/LinuxAMD64/cst_settings.conf exists.
#  b) this file is newer than "~/.config/CST AG/CST DESIGN ENVIRONMENT.conf"
#

LICENSE_TYPE=floating
LICENSE_FILE=""
LICENSE_SERVER="27000@empc101.ele.tue.nl"
LICENSEMODE="Flexnet"
LICENSESERVER_DSLS=""
```
