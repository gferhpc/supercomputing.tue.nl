# Cluster Policies

Everybody who has used other computing clusters before is used to
different policies. This pages serves to make clear what ours are.

## File storage policies

### No Backups!

Data (incl. home directories) in the HPC Cluster is **NOT** backed up!

The HPC Cluster is not a solution for archiving your work.

!!! danger

    You are **FULLY** responsible for your own data management!

### Fair Use of Disk Space

Each user has a 200GB disk quota. The total disk space is however not
enough for every user to actually use that much. Therefore:

- Try to keep disk usage below 100GB as a general rule.
- If your disk usage exceeds 150GB, think carefully about what can be
  moved.

## Job policies

Please refrain from running long, highly CPU-intensive jobs on the login
node. If many people do this, it significantly slows down using the
system for e.g. submitting jobs, copying data, etc.

## Disk load

Sometimes you just have to do a lot of operations on a lot of files.
This is a regularly occurring cause for poor head node performance. How
do we prevent being a nuisance?

### Bulk Moving, deleting, tarring, files that are in home

This is a common part of cleaning up your home directory. It can cause
overloading of the disk system regardless of measures you take, but you
can still do things to prevent that. Most importantly: Do not do this in
multiple parallel threads or shells: The disk is often the bottleneck in
these operations, so it will not speed things up anyway, and in fact may
cause a slowdown. And if the disk is not the bottleneck (as in some gzip
operations), you are doing everyone a great favor by doing only one
thread at the time because it means the chance that anyone will even
notice you're doing this has gone down significantly.

### Copying files from elsewhere on the cluster

Same as in the previous point: Please do not try to do multiple SCP
sessions in parallel. The chance of generating a speedup for yourself is
smaller than the chance of causing trouble for others.
