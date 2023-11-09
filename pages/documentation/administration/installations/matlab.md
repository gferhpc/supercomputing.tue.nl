# MATLAB

As a user on your laptop:

From/on the WebSite, Download the MATLAB installer (Linux) and for the license Create an key (XXXX-XXXX-XXXX-XXXX-XXXX-....)

copy the *.zip to the login node into /local/MATLAB/.

As a user on login node (need X11):

```shell
cd to /local/MATLAB
unzip *.zip -d ./Install
cd ./Install
./install
```

GUI: login (User Account) and select Full Download from drop-down-menu, Download location /local/MATLAB/Download

OR Use the Windows Installer to download Linux Files and copy the XXXX_XX_XX_XX_XX_XX to /local/MATLAB/Download/

As root on login node (no need X11):

```shell
VERSION=R2023a
cd /local/MATLAB/Download/XXXX_XX_XX_XX_XX_XX
mkdir -p /cm/shared/apps/MATLAB/<VERSION>/licenses
cp /cm/shared/apps/MATLAB/<PREVIOUS_VERSION>/licenses/license.dat /cm/shared/apps/MATLAB/<VERSION>/licenses/.
```

vi cm_shared_apps_MATLAB_install.txt
```{ .ini }
destinationFolder=/cm/shared/apps/MATLAB/<VERSION>
fileInstallationKey=XXXX-XXXX-XXXX-XXXX-XXXX-....
agreeToLicense=yes
outputFile=./MATLAB_install.log
enableLNU=no
improveMATLAB=no
licensePath=/cm/shared/apps/MATLAB/<VERSION>/licenses/license.dat
```

```shell
./install -inputfile cm_shared_apps_MATLAB_install.txt
```

Create a module: `/cm/shared/modulefiles/matlab/<VERSION_MINUS_THE_LEADING_R>`