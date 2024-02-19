# AMS

**VERSION=2023.104**

As a user on your laptop:

From/on the Website, Download the AMS Linux OpenMPI binary tgz - Login credentitials are in TopDesk Self Service Portal ( Installing AMS )

copy the *.tgz to the login node into /local/AMS.

As root on login node:

```shell
export AMS_VERSION=2023.104
cd /local/AMS
mkdir /sw/rl8/zen/app/AMS/${AMS_VERSION}/
tar -xzf ams${AMS_VERSION}.pc64_linux.openmpi.bin.tgz -C /sw/rl8/zen/app/AMS/${AMS_VERSION}/
cd /sw/rl8/zen/app/AMS/${AMS_VERSION}
mv  ams${AMS_VERSION}/* .
rmdir ams${AMS_VERSION}
cd
chown -R easybuild:tue-support /sw/rl8/zen/app/AMS/${AMS_VERSION}
chmod -R o+rx /sw/rl8/zen/app/AMS/${AMS_VERSION}
# Create a module : /sw/rl8/zen/mod/AMS/${AMS_VERSION}
```

## AMS extra packages

PACKAGE_NAME=m3gnet

As root on ue-login002:

```shell
module load AMS/${AMS_VERSION}
"$AMSBIN"/amspackages install PACKAGE_NAME
```
