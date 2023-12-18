# AMS

**VERSION=2023.104**

As a user on your laptop:

From/on the Website, Download the AMS Linux OpenMPI binary tgz - Login credentitials are in TopDesk Self Service Portal ( Installing AMS )

copy the *.tgz to the login node into /local/AMS.

As root on login node:

```shell
export AMS_VERSION=2023.104
cd /local/AMS
mkdir /cm/shared/apps/ams/${AMS_VERSION}/
tar -xzf ams${AMS_VERSION}.pc64_linux.openmpi.bin.tgz -C /cm/shared/apps/ams/${AMS_VERSION}/
cd /cm/shared/apps/ams/${AMS_VERSION}
mv  ams${AMS_VERSION}/* .
rmdir ams${AMS_VERSION}
cd
chown -R root:root /cm/shared/apps/ams/${AMS_VERSION}
chmod -R o+rx /cm/shared/apps/ams/${AMS_VERSION}
# Create a module : /cm/shared/modulefiles/ams/${AMS_VERSION}
```

## AMS extra packages

PACKAGE_NAME=m3gnet

As root on hpc-secondary:

```shell
module load shared
module load ams/<VERSION>
"$AMSBIN"/amspackages install PACKAGE_NAME
```
