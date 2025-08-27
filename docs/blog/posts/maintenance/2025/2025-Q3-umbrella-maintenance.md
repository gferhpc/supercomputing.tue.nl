---
title: Umbrella Maintenance 2025 Q3
date: 2025-07-27
start: 2025-08-25T09:00:00
end: 2025-08-27T17:00:00
categories: [ Umbrella ]
tags: [ Maintenance ]
authors: [ a.van.hoof, e.loomeijer, a.c.m.bertens ]
type: maintenance
slug: Q3-2025-umbrella-maintenance
image: assets/images/maintenance.webp
banner:
  enabled: false
---

# 2025 Q3 Umbrella HPC Cluster maintenance

TU/e Umbrella HPC Cluster has a scheduled downtime for maintenance from **Monday 25 August 09:00 CET** to **Wednesday 27
August 17:00 CET**. The cluster will be unavailable during this time. Please make sure that your jobs are finished before
the start of the maintenance or that they can continue after they were (hard) killed/cancelled.

!!! danger ""

    _All_ running Jobs on **Monday 25 August 2025 09:00** will be cancelled!

<!-- more -->

!!! warning ""

    There are **no backups** on the HPC cluster — do not use it for archiving. You are responsible for your own data management!

---

## Important Changes After Maintenance

### Required Job Script Updates

#### Memory Requirement

After this maintenance, all jobs must specify how much memory they require.  If you do not specify the memory, your job will receive **1 GB RAM per CPU core** by default.

Update your SLURM job scripts to include one of the following:

```shell
#SBATCH --mem=10G
#SBATCH --mem-per-cpu=2G
#SBATCH --mem-per-gpu=2G  # This is CPU RAM, not VRAM!
```

*ℹ️ This change helps prevent jobs from being killed unexpectedly when another job uses too much memory.*

#### Maximum Run Time

After maintenance, jobs without a specified maximum run time will be automatically limited to **1 hour**.  Add this line to your job script if you need more time:

```shell
#SBATCH --time=<hh:mm:ss>
```

*ℹ️ This change avoids “runaway” jobs and makes scheduling more efficient.*

#### What happens if I don’t update my script?
- Jobs without a memory request may fail or be killed if they use more than the default amount of memory.
- Jobs without a run time will automatically stop after 1 hour.

---

### 🎉 New Feature: Single Sign-On

You will be able to log in to [hpc.tue.nl (Open OnDemand)](https://hpc.tue.nl) using TU/e Single Sign-On.  No more separate username/password needed for the web interface.

*ℹ️ SSH access remains unchanged: keep using your TU/e username & password for SSH.*

---

### Technical & Security Updates

- Latest updates and patches to [Rocky Linux 8](https://rockylinux.org/) will be installed.
- Security fixes and firmware upgrades will be applied across all nodes, improving reliability and safety.

---

## What You Need To Do

- **Finish your jobs before the maintenance** to avoid interruptions.
- **Update your job scripts** to specify both required memory and run time.
- Do **not** use the cluster during the maintenance window.
- After maintenance, check that your applications and code run as expected.

---

## Questions After Maintenance

If you encounter any issues after the maintenance window, with which you would like assistance, please let us know.
We can be reached by [e-mail](mailto:hpcsupport@tue.nl) and through [Teams](https://teams.microsoft.com/l/team/19:7830cc8a6f244d6689a374c60673b43c%40thread.tacv2/conversations?groupId=a07b9e15-8538-4889-8610-502177c36dc7&tenantId=cc7df247-60ce-4a0f-9d75-704cf60efc64).

Immediately after the maintenance we'll also be available in person.

- **Dates**: Thu 28 August – Fri 5 September
- **Times**: 10.00–12.00, 13.00–15.00
- **Location**: EAISI office (Neuron building, room 1.105)<br/>
  _Find the "Eindhoven Supercomputing Center" banner on the first floor!_
