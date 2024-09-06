---
date: 2024-08-29
categories: [Umbrella HPC Cluster, Maintenance]
authors: [e.loomeijer@tue.nl, a.van.hoof@tue.nl, a.c.m.bertens@tue.nl]
---

# 2024 Q3 Umbrella HPC Cluster maintenance

The Umbrella HPC Cluster scheduled downtime for maintenance is finished and jobs can be submitted and will run again. Below this e-mail you'll find a list of some of the changes we've made. We don’t expect any issues do due the maintenance, but if you have issues contact us by any of the following means:

* [hpcsupport@tue.nl](mailto:hpcsupport@tue.nl)
* [TOPdesk](https://tue.topdesk.net/tas/public/ssp/content/serviceflow?unid=1906588cfc984bf0b8e5d80469467ee4){target=_blank}
* [Teams](https://teams.microsoft.com/l/team/19:7830cc8a6f244d6689a374c60673b43c%40thread.tacv2/conversations?groupId=a07b9e15-8538-4889-8610-502177c36dc7&tenantId=cc7df247-60ce-4a0f-9d75-704cf60efc64){target=_blank}

!!! danger

    Please remember that data (incl. home directories) on the HPC Cluster is NOT backed up!  The HPC Cluster is not a solution for archiving your work!

<!-- more -->

## Changes

- **ML datasets**: previously, some common machine learning datasets were available on `/home/tue/shared_data/ml_datasets`. We've moved these datasets to `/dataset`. A description of these datasets can be found [here](../../documentation/datasets.md) .
- **Quota**: previously, quota were sometimes set incorrectly or not set at all. We've rectified the situation, and are now setting quota on the total space used and number of files created, both on home directories and project directories.

### New features:

- **Project directories**: we're introducing project directories. If you need to work together with one ore more colleagues on a dataset, or you'd like to easily exchange files with them, you can request a project directory. Project directories are accessible to project members, have quota set per request, and have a limited duration (i.e. until the project ends).  Project directories can be requested using this [TOPdesk form](https://tue.topdesk.net/tas/public/ssp/content/serviceflow?unid=f950a580c8e34a7abb7d37d102c788e8){target=_blank}.
- **Scratch directories**: we're introducing scratch directories. Scratch directories are perfect for storing snapshots or checkpoints of your simulations. Your scratch dir is located in `/scratch-shared/USERNAME`. Files that reside in this directory will be automatically deleted 14 days after they were last modified. You can store at most 8 TB and 3,000,000 files here.

### Changes that should not affect your workflow:

- **OS upgrade**: the current Cluster OS, Rocky Linux 8, was upgraded to the latest version (8.9 -> 8.10). This could have minimal impact if you are using OS-provided tools. When using the module system to load your tools there will be no difference.
- **Slurm upgrade**: Slurm was upgraded to version 23.11.
- **Storage replacement**: a part of the classical storage for e.g. home dirs (which uses spinning disks) is now replaced by newer, faster, HPC-optimised storage solution that uses flash.

## Questions?

For questions and remarks please contact [hpcsupport@tue.nl](mailto:hpcsupport@tue.nl)
