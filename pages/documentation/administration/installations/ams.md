# AMS

**VERSION=2023.105**

As a user on your laptop:

From/on the Website, Download the AMS Linux OpenMPI binary tgz - Login credentitials are in TopDesk Self Service Portal ( Installing AMS )

`mkdir /local/AMS`

copy the *.tgz to the login node into /local/AMS.

`chown -R easybuild /local/AMS`

As easybuild on login node:

```shell
export AMS_VERSION=2023.105
cd /local/AMS
mkdir /sw/rl8/zen/app/AMS/${AMS_VERSION}/
tar -xzf ams${AMS_VERSION}.pc64_linux.openmpi.bin.tgz -C /sw/rl8/zen/app/AMS/${AMS_VERSION}/
cd /sw/rl8/zen/app/AMS/${AMS_VERSION}
mv  ams${AMS_VERSION}/* .
rmdir ams${AMS_VERSION}
cd
chown -R easybuild:easybuild /sw/rl8/zen/app/AMS/${AMS_VERSION}
chmod -R o+rx /sw/rl8/zen/app/AMS/${AMS_VERSION}
# Create a module : /sw/rl8/zen/mod/all/AMS/${AMS_VERSION}
# Check the path to the license file (/sw/rl8/zen/lic/FloatADF/....)
```

## AMS extra packages

PACKAGE_NAME=m3gnet

As easybuild on tue-login002:

```shell
module load AMS/${AMS_VERSION}
"$AMSBIN"/amspackages install PACKAGE_NAME
chown -R easybuild:easybuild /sw/rl8/zen/app/AMS/${AMS_VERSION}
chmod -R o+rx /sw/rl8/zen/app/AMS/${AMS_VERSION}
```
