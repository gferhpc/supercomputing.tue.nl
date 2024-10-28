---
draft: true
date: 2025-01-01
start: 2025-02-24T09:00:00
end: 2025-02-26T17:00:00
categories: [ Umbrella HPC Cluster ]
tags: [ HPC ]
authors: [ a.van.hoof, e.loomeijer, a.c.m.bertens ]
type: maintenance
slug: Q1-2025-umbrella-maintenance
title: Umbrella HPC Cluster maintenance
banner:
  enabled: true
---

# 2025 Q1 Umbrella HPC Cluster maintenance

TU/e Umbrella HPC Cluster has a scheduled downtime for maintenance from **Monday 24 Feb 09:00 CET** to **Wednesday 26
Feb 17:00 CET**. The cluster will be unavailable during this time. Please make sure that your jobs are finished before
the start of the maintenance or that they are able to continue after they were (hard) killed/cancelled.

<!-- more -->

## Planned changes

### Install latest firmware and software updates

We will install all latest firmware patches for our servers, switches, & storage nodes, 
and install all available updates of the [Rocky Linux 8](https://rockylinux.org/){ :target=_blank } distribution 
([CHANGELOG](https://errata.build.resf.org){ :target=_blank }).

### Login hostname

Please update your clients to use **hpc.tue.nl** as address/hostname. The following hostnames will be removed:

!!! warning "Deprecated addresses"

    - **M&CS**: `hpc.win.tue.nl` & `mcs-login001.icts.tue.nl`
    - **APSE**: `compass.phys.tue.nl` & `phys-login001.phys.tue.nl`
    - **BE**: `hpc.arch.tue.nl` & `arch-login001.bwk.tue.nl`
    - **CE&C**: `chem-login001.chem.tue.nl`
