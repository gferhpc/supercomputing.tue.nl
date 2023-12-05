---
draft: true
date: 2023-12-01
categories: [Umbrella HPC Cluster]
authors: [e.loomeijer@tue.nl, a.van.hoof@tue.nl, a.c.m.bertens@tue.nl]
---

# 2024-Q1 Umbrella HPC Cluster announcement

Changes to the Umbrella HPC Cluster in 2024-Q1:

- Make node features consistent in SLURM to facilitate effective filtering of nodes.[^1]

<!-- more -->

??? abstract "Planning & Considerations"
    -   It is recommended to stack task/cgroup,task/affinity together when
    configuring TaskPlugin, and setting ConstrainCores=yes in
    cgroup.conf. This setup uses the task/affinity plugin for setting
    the cpu mask for tasks and uses the task/cgroup plugin to fence
    tasks into the allocated cpus.

[^1]: [link/to/extensive/explanation]()
