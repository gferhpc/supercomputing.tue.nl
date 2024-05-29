# ANSYS ElectroMagnetics

**VERSION=2023R1**

From your laptop copy ELECTRONICS_${ANSYS-EM_VERSION}_LINX64.tgz to /local of the login node.

As easybuild on login node with X forwarding enabled:

```shell
export ANSYSEM_VERSION=2023R1
cd /local/ANSYS-EM
tar -xzf ../ELECTRONICS_${ANSYSEM_VERSION}_LINX64.tgz
cd Electronics_231_linx64
cp VerifyOS.bash VerifyOS.bash.orig 
echo "exit 0" > VerifyOS.bash 
mkdir /sw/rl8/zen/app/ANSYS-EM/${ANSYSEM_VERSION}/
./install
    Install Electromagnetcs Suite
    installpath: /sw/rl8/zen/app/ANSYS-EM/${ANSYSEM_VERSION}
    use /tmp (no read/write for all)
    shared application: /sw/rl8/zen/app/ANSYS-EM/${ANSYSEM_VERSION}
    license server: ansys-research.lic.tue.nl 1055

cd /sw/rl8/zen/app/ANSYS-EM/${ANSYSEM_VERSION}/v231/Linux64
cp VerifyOS.bash VerifyOS.bash.orig 
evho "exit 0" > VerifyOS.bash 
# Create a module : /sw/rl8/zen/mod/all/ANSYS-EM/${ANSYS-EM_VERSION}
# Check the path to the license server
```