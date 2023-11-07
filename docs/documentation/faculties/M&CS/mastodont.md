---
title: Mastodont (big memory)
---

# Mastodont

!!! note
    This machine isn't managed by the HPC Lab and is only documented here for historic reasons.

`mastodont.win.tue.nl` is a Linux system designed to support
long-running computations that require a large amount of RAM.
It was *not* designed to support CPU-bound or parallel computations.
For such computations please use one of the
[<https://hpcwiki.tue.nl/wiki/Technical_specifications>
clusters](/https://hpcwiki.tue.nl/wiki/Technical_specifications_clusters "wikilink")
.

The mastodont server is *not* part of a cluster.

## Hardware specifications

<table>
<thead>
<tr class="header">
<th><p>Resource</p></th>
<th><p>Provides</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CPUs</p></td>
<td><p>4 x Intel(R) Xeon(R) Gold 6136 CPU @ 3.00GHz (96
processors)</p></td>
</tr>
<tr class="even">
<td><p>RAM</p></td>
<td><p>3 TB (3169407968 KB)</p></td>
</tr>
<tr class="odd">
<td><p>disk</p></td>
<td><p>swap space: 4 x 2.9 TB (SSD, equal priority, parallel)</p>
<p><code>/home</code>: 50 GB SSD in RAID 1</p>
<p><code>/scratch</code>: 33 TB HDD in RAID 6</p></td>
</tr>
</tbody>
</table>

## Operating system

`mastodont` runs Ubuntu Server 20.04 LTS.

Software is installed and upgraded by IMS on request.

Security updates are applied automatically every night. Reboots only
happen after communicating with users, so as not to disturb long-running
processes.

## User accounts

If you wish to be granted access, please apply at the IMS help desk in
MF 3.083 and inform Jan Friso Grootte (his cluster is the biggest
consumer so they can take your application into account).

SSH access is only allowed from the campus or VPN.

Login using SSH with your TUE user name and password. It is highly
recommended that you setup and use [public key
authentication](https://linuxwiki.tue.nl/wiki/SSH#SSH_Keys).

### User account names starting with a digit

Starting at Ubuntu 20, obstacles were raised by the service manager
`systemd` for user names starting with a digit.
Such user names were introduced at TU/e as part of the IAM, Identity
Access Management,
way before `systemd` introduced the obstacles.

The obstacles mostly concern desktop applications that you will probably
not use on mastodont.
Such applications will complain that they cannot connect to the dbus.

Also XDG_RUNTIME_DIR will be missing.
That is, the pointer $XDG_RUNTIME_DIR in the process environment and the
directory that it would normally point to.
This may concern applications that you do use on mastodont.

## Disk space

All disk space is local, not shared with other systems:

<dl>
<dt>

`/home/`<em>`username`</em>

<dd>

Your home directory; mostly intended for configuration files.
We do not provide backup service, so keep your files safe elsewhere.
Disk space is limited (50 GB shared by all users), and quota are not
enforced;
please be considerate of other users and keep your use as limited as
possible.

<dt>

`/scratch`

<dd>

Scratch space for temporary files;
Use it for files you can afford to lose.
We reserve the right to clean it up when required!
There is plenty of disk space, but please be considerate of other users
and regularly remove files you no longer need.

</dl>

At the moment, **no backup** is in place for any of these files.
Be sure to make your own backups of important files, e.g. on
[SURFdrive](https://www.surf.nl/bewaar-en-deel-je-bestanden-veilig-in-de-cloud-met-surfdrive/tutorials-voor-het-gebruik-van)
.

Disk error protection is provided by the
[RAID](https://en.wikipedia.org/wiki/RAID) levels as mentioned in the
Hardware specifications section.
Note that this does not protect against disk <i>controller</i> failures.

<h2>

Software

</h2>

Packages from the Ubuntu repositories can be installed on request.
We will check the requested packages for security and side-effects for
other users
and install them if we do not see issues.