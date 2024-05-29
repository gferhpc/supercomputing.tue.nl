# ANSYS ElectroMagnetics

**VERSION=2023R1**

From your laptop copy ELECTRONICS_${ANSYS-EM_VERSION}_LINX64.tgz to /local of the login node.

As easybuild on login node with X forwarding enabled:

```shell
export ANSYS-EM_VERSION=2023R1
cd /local/ANSYS-EM
tar -xzf ../ELECTRONICS_${ANSYS-EM_VERSION}_LINX64.tgz
cd Electronics_231_linx64
mv VerifyOS.bash VerifyOS.bash.orig 
echo "exit 0" > VerifyOS.bash 
mkdir /sw/rl8/zen/app/ANSYS-EM/${ANSYS-EM_VERSION}/
./install
    installpath: /sw/rl8/zen/app/ANSYS-EM/${ANSYS-EM_VERSION}
    use /tmp
    shared application: /sw/rl8/zen/app/ANSYS-EM/${ANSYS-EM_VERSION}
    license server: ansys-research.lic.tue.nl

cd /sw/rl8/zen/app/ANSYS-EM/${ANSYS-EM_VERSION}/v231/Linux64
mv VerifyOS.bash VerifyOS.bash.orig 
evho "exit 0" > VerifyOS.bash 
# Create a module : /sw/rl8/zen/mod/all/ANSYS-EM/${ANSYS-EM_VERSION}
# Check the path to the license server
```