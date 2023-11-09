---
draft: true
date: 2023-12-01
categories: [Umbrella HPC Cluster]
tags: [HPC]
authors: [e.loomeijer@tue.nl, a.van.hoof@tue.nl, a.c.m.bertens@tue.nl]
---

# 2024-Q1 Umbrella HPC Cluster announcement

TBD.

<!-- more -->

??? abstract "Planning & Considerations"
    -   It is recommended to stack task/cgroup,task/affinity together when
    configuring TaskPlugin, and setting ConstrainCores=yes in
    cgroup.conf. This setup uses the task/affinity plugin for setting
    the cpu mask for tasks and uses the task/cgroup plugin to fence
    tasks into the allocated cpus.