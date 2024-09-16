---
title: 3. Transfer Data
---

# Transfer Data

To get your data (files) onto the TU/e Umbrella HPC Cluster or back to your local machine, there are usually different ways.

Commonly used and widely supported copying tools are `rsync` which mirrors directories (folders) between the supercomputer and your local machine. `scp` which is useful for a few single files or specified file-lists, and lastly the commonly used ftp or the encrypted version `sftp` (or ftps).

As all nodes in the Cluster have access to the same shared data as the login nodes (Home Directy, Project Directoy) therefore copying data from and to the login node is sufficient. 

## Accessing Microsoft OneDrive (using rclone)

All tough `rclone` is a command line tool (https://rclone.org/), to configure a OneDrive connection a graphical environment is need to authorize the connection to Microsoft OneDrive. Configuration of the connection only needs to be done once.

### Start an interactive Desktop Session

Login to https://hpc.tue.nl and request a Interactive Desktop (Scroll Down to the bottom of the list of Tiles), ! hour, 1 CPU and 4 GB of memmory should be sufficient to finish the configuration. 

### Setting up a connection to Microsoft OneDrive

Once the Interactive Desktop session is ready, open a terminal. In the terminal, run the command `rclone config`. 

It prompts you with a bunch of questions:

- It shows "No remotes found -- make a new one" or list available remotes you made before
  - Answer "n" for "New remote"
- "name>" (the name for the new remote)
  - Type "OneDrive" (or whatever else you want to call this remote)
- "Storage>" (the storage type of the new remote)
  - This should display a list to choose from. Enter the number corresponding to the "Microsoft OneDrive" storage type, which is "35".
- "client_id>"
  - Leave this blank (just press enter).
- "client_secret>"
  - Leave this blank (just press enter).
- "Choose national cloud region for OneDrive."
  - This should display a list to choose from. Enter the number corresponding to the "Microsoft Cloud Global" region, which is "1".
- "Edit advanced config?"
  - Type "n" for no
- "Use auto config?"
  - Answer "y" for yes
- A web browser window should pop up allowing you to log into box. It is a good idea at this point to verify that the url is actually OneDrive before entering any credentials 
  - Enter your TU/e email, Password and MFA
  - This should take you to the OSU login page. Login with your OSU credentials 
  - Go back to the terminal once "Success" is displayed.
- "Your choice>"
  - Locate the drive you wish to use.
  - Type "1" to use your personal or business OneDrive
- "Choose drive to use"
  - Locate the option: OneDrive (business)
  - Type the number of the option
- "Is this Okay? y/n>"
  - Type "y" to confirm the drive you wish to use is correct.
- "y/e/d>"
  - Type "y" to confirm you wish to add this remote to rclone.
- "Current remotes:"
  - An remote of type "onedrive" should be avaiable.
  - Type "q" to Quit

Close the terminal (type `exit` of close the window) and end the Interactive Desktop (Left Click on your name in the upper right corner en choose "logout" the press "logout" button).

### Testing the OneDrive Connection (Command Line)

Either use SSH to login into the Umbrella cluster (ssh username@hpc.tue.nl) or use https://hpc.tue.nl to open a terminal.

Create an empty hello.txt file and upload it to OneDrive using 'rclone copy' as below in a terminal:

``` shell
touch hello.txt
rclone copy hello.txt OneDrive:/test
```

This creates a toplevel directory in OneDrive called 'test' if it does not already exist, and uploads the file hello.txt to it.

To verify the uploading is successful, you can either login to OneDrive in a web browser to check the file, or use rclone ls command in the terminal as:

``` shell
rclone ls OneDrive:/test
```

Copy the contents of a source directory from a configured OneDrive remote, OneDrive:/src/dir/path, into a destination directory in your OSC session, /dest/dir/path, using the code below:

``` shell
rclone copy OneDrive:/src/dir/path /dest/dir/path
```
Identical files on the source and destination directories are not transferred. Only the contents of the provided source directory are copied, not the directory name and contents.

copy does not delete files from the destination. To delete files from the destination directory in order to match the source directory, use the sync command instead.

If only one file is being transferred, use the copyto command instead:

``` shell
rclone copyto OneDrive:/test/hello.txt test-onedrive.txt
```

### Testing the OneDrive Connection (Webacces https://hpc.tue.nl)

Login, check the "File" top menu bar option, besides a "Homedrive" there now is a "onedrive" which was configured. Uisng the files browser can be copie from and to the "Homedrive". 

## Accessing Windows file shares
Windows file shares (aka. "Samba" shares or "CIFS" shares) can be
accessed from the login nodes using the `smbclient` tool. The workflow
shown below should support most use cases. In the example shown here, we
will connect to the Windows file share
`\\campushome.campus.tue.nl\20232655`, with the username `tue\20232655`.
If you want to connect to a non-centrally mananaged storage, e.g. a
research group's NAS, you might need to use a different username and
password, e.g. `nottue\myname`

Besides through the `smbclient` tool, direct access to Windows file
shares on the cluster is not supported. The reason for this is that a
misbehaving job could easily put a too large demand on the central
Windows storage, which would hinder everyone working at TU/e.

### Connecting

1.  [Connect](../access/index.md) to any
    of the cluster's login nodes.
2.  Connect to the Windows file share using the following command:
    ```
    smbclient -U tue/20232655 //campushome.campus.tue.nl/20232655
    ```
    and enter your password when prompted.

    Note: you need to use the appropriate username! If you want to
    connect to a non-centrally managed storage, such as a research group
    NAS, you may need to use a different username and password!

3.  The `smbclient` tool now shows you the following prompt:
    ```
    smb: \>
    ```

### Navigating the Windows file share

`smbclient` provides you a prompt much like the following:

    smb: \>

Here, the "\\ indicates that we're currently in the root of the Windows
file share. To show the files and folders on the share, do

    ls

For example:

    smb: \> ls
      .                                   D        0  Wed Jun 21 13:46:30 2023
      ..                                  D        0  Wed Jun 21 13:46:30 2023
      software                            D        0  Wed Jun 21 13:59:42 2023
      _viminfo                            A    15029  Wed Jun 21 13:46:30 2023

                    262144 blocks of size 4096. 194259 blocks available

which shows that we have a directory ("D") called "software" and a file
called "_viminfo". To go into the "software" directory, do

    cd software

For example:

    smb: \> cd software
    smb: \software\>

`smbclient` now correctly shows that we're in the "software" folder. To
go back up to the root folder, do

    cd ..

For example:

    smb: \software\> cd ..
    smb: \>

### Copying files into the cluster

The following command will copy a file called "data.zip" to the current
directory on the cluster:

    smb: \> get data.zip
    getting file \data.zip of size 99248046 as data.zip (46574.7 KiloBytes/sec) (average 46574.7 KiloBytes/sec)
    smb: \>

The following commands will copy a folder hierarchy called "myfolder" to
the current directory on the cluster:

    smb: \> recurse on
    smb: \> prompt off
    smb: \> mget myfolder
    getting file \myfolder\data.zip of size 99248046 as data.zip (56912.5 KiloBytes/sec) (average 56912.5 KiloBytes/sec)
    getting file \myfolder\morefolders\afile.txt of size 21 as afile.txt (10.3 KiloBytes/sec) (average 56845.7 KiloBytes/sec)
    smb: \>

### Copying files to the Windows file share

The following command will copy a file called "data.zip" to the current
directory on the Windows file share:

    smb: \> put data.zip
    putting file data.zip as \data.zip (59828.3 kb/s) (average 59828.3 kb/s)
    smb: \>

The following commands will copy a folder hierarchy called "myfolder" to
the current directory on the cluster:

    smb: \> recurse on
    smb: \> prompt off
    smb: \> mput myfolder
    putting file myfolder/morefolders/afile.txt as \myfolder\morefolders\afile.txt (6.8 kb/s) (average 6.8 kb/s)
    putting file myfolder/data.zip as \myfolder\data.zip (110894.6 kb/s) (average 110515.3 kb/s)
    smb: \>

### Closing `smbclient`

Enter the following command:

    smb: \> exit

or hit Ctrl-D.
