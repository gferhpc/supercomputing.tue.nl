---
title: 3. Transfer Data
---

# Transfer Data

To get your data (files) onto the TU/e Umbrella HPC Cluster or back to your local machine, there are usually different ways.

Commonly used and widely supported copying tools are rsync which mirrors directories (folders) between the supercomputer and your local machine. scp which is useful for a few single files or specified file-lists, and lastly the commonly used ftp or the encrypted version sftp (or ftps). A little bit more information can be found in the File Transfer article.


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

1.  [Connect](cluster-access.md) to any
    of the cluster's login nodes.
2.  Connect to the Windows file share using the following command:
    smbclient -U tue/20232655 //campushome.campus.tue.nl/20232655

    and enter your password when prompted.

    Note: you need to use the appropriate username! If you want to
    connect to a non-centrally managed storage, such as a research group
    NAS, you may need to use a different username and password!
3.  The `smbclient` tool now shows you the following prompt:
    smb: \>

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