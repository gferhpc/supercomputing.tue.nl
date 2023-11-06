---
title: 2. Access the cluster
---
# Access the cluster

This page describes how to connect to the cluster making novice users
more familiar with \`CLI\` and \`SSH\` concepts.

## Necessary tools

HPC clusters that are most commonly operated via a [\`Command Line
Interface\`
(CLI)](https://en.wikipedia.org/wiki/Command-line_interface).

Such a CLI can be accessed directly by attaching a monitor and keyboard
to the cluster itself locally to create an operational "terminal",
however it is more common to operate HPC clusters remotely over the
(inter)network through [\`Secure SHell\`
(SSH)](https://en.wikipedia.org/wiki/Secure_Shell) using a [Terminal
Emulators](https://en.wikipedia.org/wiki/Terminal_emulator), as HPC
clusters are usually geographically inconveniently located for their
users.

GNU/Linux and MacOS systems are usually equipped with powerful SSH tools
by default out of the box. Microsoft Windows users can install openSSH
on windows
[1](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse),
or install third-party software, e.g.:

### Free and Open Source Software

-   [MobaXterm](https://mobaxterm.mobatek.net/) (Free Version); Enhanced
    terminal for Windows with X11 server, tabbed SSH client, network
    tools and much more.
-   [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html);
    SSH CLI-terminal.
-   [WinSCP](https://winscp.net/eng/index.php); SSH file-explorer.
-   [Git for Windows](https://git-scm.com/download/win) installs Git
    Bash:; Linux-like CLI environment on Windows, including SSH.

### Proprietary software

-   [SmarTTY](http://sysprogs.com/SmarTTY/); both an SSH CLI-terminal
    and file-explorer combined into one program.

## Logging in

If you get a question about SSH key fingerprints from the server, you
can verify them with the below values.

```shell
2048 SHA256:1XsJDtOvF640B+woZx1i3Jg3H6IhyrLZSmcfbdpePYI hpc.tue.nl (RSA)
256 SHA256:f397R3vn2cnR6gOq3FUwor3fs/ng0GOpA0pJva4L4Xg hpc.tue.nl (ECDSA)
256 SHA256:czSbafxnFyq581Rvlrl4buHLjEApG5dBZkGfjy09HhI hpc.tue.nl (ED25519)
```

### From CLI

Simpy issue the following from the command line:

`$ ssh hpc.tue.nl -l `<USERNAME>

### From a GUI

1.  Open your SSH tool of choice (e.g. PuTTY).
2.  Fill-out the server address (e.g. hpc.tue.nl)\*
3.  Open the connection (click the \[Open\] button in the case of
    PuTTY).
4.  Answer the questions on-screen.

```shell
       _____ _   _  __                                ╮╭
      |_   _| | | |/ /__                         ▄██████████▄
        | | | |_| / / -_)                     ▄████████████████▄
        |_|  \___/_/\___|                   ▄████████████████████▄
                                           ▄██████████████████████▄
 Eindhoven University of Technology       ▐▀▀▀▀███▀▀▀▀██▀▀▀▀███▀▀▀▀▌
------------------------------------                  ▐▌
                                                      ▐▌  ▄
Welcome to the TU/e HPC Umbrella login node           ▐▌  █
                                                       █▄█▀
For WIKI information on how to use this cluster go to:
https://hpcwiki.tue.nl/

--------------------------------------------------------------------
 Data (incl. home directories) in the HPC Cluster is NOT backed up!

     The HPC Cluster is not a solution for archiving your work!
--------------------------------------------------------------------

[username@tue-login001 ~]$
```

### Login nodes

Most TU/e HPC clusters are logged-into via the general log-in nodes from
the TU/e: *hpc.tue.nl*, but some clusters have their own login node:

| Node                      | Users                          |
|---------------------------|--------------------------------|
| phys-login001.phys.tue.nl | Applied Physics (compass)      |
| hpc.win.tue.nl            | Mathematics & Computer Science |
| hpc.arch.tue.nl           | Built Environment              |
| hpc.tue.nl                | All others                     |

## Personal homedir

All HPC accounts come with a
[homedir](https://en.wikipedia.org/wiki/Home_directory) on the cluster.

This directory ("folder" in Ms. Windows terminology) forms the entry
point "location" on the cluster for a user to operate the HPC cluster
from.

It can be used to store scripts but also to have (personal) software
locally installed and/or configured.

## Open OnDemand on the TU/e Umbrella HPC Cluster

Based on <https://openondemand.org/> easy access to the TU/e Umbrella
HPC Cluster is possible using a Web-Browser.
[alt=OpenOnDemand Login
Screen\|300x300px](/File:LoginOOD.png "wikilink")

<big>Goto: <https://hpc.tue.nl> and login with your credentials</big>

### Features

#### Terminal in the Browser

Terminal access to the cluster login-node available from the browser, no
longer client software is needed (other than Chrome) to take your first
steps on the cluster.

[<File:TerminalOOD.png>](/File:TerminalOOD.png "wikilink")

#### Upload and Download Files

Access to the files with upload and download capabilities, in your
home-directory on the cluster via the browser.
[none\|frame](/File:UpdownOOD.png "wikilink")

#### Interactive Graphical Jobs

Start interactive jobs in your browser with a few clicks and interact
within your browser. [thumb\|none](/File:InteractiveOOD.png "wikilink")
Like R Studio: [none\|thumb](/File:RStudioOOD.png "wikilink") Or
Paraview: [none\|thumb](/File:ParaviewOOD.png "wikilink")