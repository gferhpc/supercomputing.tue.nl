---
title: 2. Access the cluster
---
# Access the cluster

The TU/e Umbrella HPC Cluster is a Linux environment with shell (commandline) access.
To log in, one usually uses SSH to reach the respective Login Nodes (computers reserved for people just like you that 
want to connect to the HPC Cluster). This access is restricted, so you can only connect, when you are within the 
university/facility and its network. To still access the Login Nodes externally, you'll need to setup a VPN (Virtual Private Network) connection. 
Dedicated documentation on how to set this up is provided on the intranet
[VPN for employees](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/VPN.aspx){:target=_blank} or 
[VPN for students](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/Provisional-VPN-for-Students.aspx){:target=_blank}.
 
Once there, the user can interact with the system and run (small) programs to generally test the system/software.

There are currently two options to connect to the TU/e HPC Umbrella Cluster. Either by using a GUI/Website 
via [Open Ondemand](openondemand.md) ^(suggested)^ or through [SSH/Command Line](ssh.md).

## Secure Shell

Secure Shell (ssh) is a commandline-tool for logging into a different computer over some network (e.g. the internet) and for executing commands on that machine, as if one would be sitting there instead of the own computer. So you use ssh to build a connection to the other computer and can then interact with it, using its shell. It is commonly used to login to the login nodes of a supercomputer.

To start an SSH session and to esablish a shared session key to encrypt the SSH traffic, [Diffie–Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) is used.

OpenSSH is the standard ssh client on Linux and the Mac and it is freely available for everyone.
On Windows, you can use Putty, Bitvise or the GitBash (coming with ssh) which is also free. On Windows 10 since Update 1709, Microsoft has packaged "ssh" right into windows. You can thus open a cmd window (Start - type "cmd" - <ENTER>) and run ssh username@hostname.domain like you would with Linux or MacOS.

### VPN

Sometimes access to a cluster's login nodes is restricted to certain networks within the university/facility, so you can connect while being on the campus, but not from your network at home or at other institutions. To nevertheless access those login nodes from external, one can 'pretend to be inside the network' by using a Virtual Private Network (VPN) provided by the university operating the cluster.

[Alice and Bob](../images/Public_key_encryption.png)

## Usage

Logging in with OpenSSH on the HPC cluster is done with:

'''$ ssh -l login@cluster'''

Here <login> is your username and <cluster> is one of the login nodes of the system, you are trying to connect to. At the first login you will be asked to verify the authenticity of the host. If the shown host is correct, enter yes. After pressing RETURN you will be prompted to enter your password for the provided username.

## Graphical Applications on the Login Node

This might or might not work depending on the your operating system, because it requires an X11-Server running on your local machine, which is not available by default on Mac and Windows. To utilize graphical tools anyway, you might want to look into MobaXterm, which provides the necessary functionality for Windows or Xquartz for Mac.


### Linux
If you need to start graphical applications you need to enable X11 forwarding/X11 tunneling by your ssh client. For OpenSSH this is done by giving it the command line option -X (or -Y if the previous did not work):

'''$ ssh -X -l login@cluster'''

### Mac

### Windows

This might or might not work depending on the your operating system, because it requires an X11-Server running on your local machine, which is not available by default on Mac and Windows. To utilize graphical tools anyway, you might want to look into FastX, which provides the necessary functionality for Mac and Windows.

For more security and ease of use you should consider setting up authentication via ssh keys.

## OpenOnDemand