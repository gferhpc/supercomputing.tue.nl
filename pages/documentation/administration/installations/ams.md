# AMS

Use EasyBuild to install AMS.

From/on the Website, Download the AMS Linux OpenMPI binary tgz

Login credentitials are in TopDesk Self Service Portal ( Search for: "Installing AMS" )

Place downloaded binary in /home/tue/easybuild/.local/easybuild/sources/a/AMS/

## AMS extra packages 

Package are/need added after EasyBuild Installation.

PACKAGE_NAME=m3gnet

As easybuild user:

```shell
module load AMS/${AMS_VERSION}
"$AMSBIN"/amspackages install PACKAGE_NAME
```
