---
title: Umbrella Maintenance 2025 Q1
date: 2025-01-01
start: 2025-03-03T09:00:00
end: 2025-03-05T17:00:00
categories: [ Umbrella ]
tags: [ Maintenance ]
authors: [ a.van.hoof, e.loomeijer, a.c.m.bertens ]
type: maintenance
slug: Q1-2025-umbrella-maintenance
image: assets/images/maintenance.webp
banner:
  enabled: true
---

# 2025 Q1 Umbrella HPC Cluster maintenance

TU/e Umbrella HPC Cluster has a scheduled downtime for maintenance from **Monday 3 March 09:00 CET** to **Wednesday 5
March 17:00 CET**. The cluster will be unavailable during this time. Please make sure that your jobs are finished before
the start of the maintenance or that they can continue after they were (hard) killed/cancelled.

!!! danger ""

    _All_ running Jobs on **Monday 3 March 2025 09:00** will be cancelled!

<!-- more -->

## What will happen?

- **Minor OS Upgrade**:

    The current OS running in the cluster is [Rocky Linux 8](https://rockylinux.org/){:target=_blank}. This version
    regularly has updates and patches, the latest will be applied. To patch the OS there can be no running jobs on the
    cluster and all nodes need to reboot.

  - **Network Upgrade**:

    The current network connection to the TU/e Umbrella HPC Cluster will be upgraded to allow faster speeds between the
    TU/e and the TU/e Umbrella HPC Cluster.

  - **Maintenance**:

    Upgrade of the job scheduler (Slurm). The scheduler (Slurm) has a newer version available that fixes bugs.

  - **Security**:

    Firmware updates (hardware). Because a part of the nodes (especially the login nodes and storage nodes) has been
    continuously running for a long time, their operating system and firmware(s) are out-of-date and need a refresh. OS
    and firmware upgrades will address security issues. For nodes that are accessible from the TU/e Campus directly this
    is an urgent issue. For this the nodes need to reboot without any jobs running on those nodes.

  - **Storage**:

    The internal shared storage will be upgraded, removing the 16 locks per file limit.

## What is the impact?

Aside from the downtime, there is no impact expected for the users and jobs started after the maintenance.

- This maintenance involves all nodes for all departments being part of the TU/e HPC Umbrella Cluster. Head nodes, login
  nodes, storage nodes, compute nodes and GPU nodes.
  See [specifications](https://supercomputing.tue.nl/documentation/specifications/).
- During the downtime/maintenance no compute jobs will be running nor can be started or scheduled.
- All running jobs on Monday 3 March 2025 09:00 will be cancelled.
- All login nodes will be rebooted killing any processes running and the nodes are unavailable during maintenance

## What do you need to do?

- Make sure your jobs are finished before Monday 3 March 2025 or that they can continue after they were (hard)
  killed/cancelled.
- Do not try to use the cluster in any way during the maintenance window.
- Check if the applications/code that you are using is still able to execute on the new OS after the maintenance.

!!! warning "No Backups!"

    Data (incl. home directories) in the HPC Cluster is NOT backed up!
    The HPC Cluster is not a solution for archiving your work!

    You are _FULLY_ responsible for your own data management!

## Questions?

For questions and remarks please contact [hpcsupport@tue.nl](mailto:hpcsupport@tue.nl).
