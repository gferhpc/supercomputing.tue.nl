---
title: Onboarding
---

# Mathematics & Computer Science

*About the [hpc.tue.nl](../../specifications.md)-cluster*

*Onboarding documentation: a mandatory read for all users*

## Introduction

The hpc.tue.nl-cluster is a cluster of compute resources (CPU/GPU)
that is made available for research staff. The facility originates from
a collectively expressed need by M&CS research in 2019 for low-barrier
(close to home but serviced) compute resources that could facilitate
most of the  computations. The main goal was to enable an **experimental
environment to test jobs**\[BB3\]  where one would not have to worry
about unnecessarily burning rented compute hours from external
resources. When using the system, be aware of the impact your type of
job has on the experience of others that you share the hardware with:
this document helps you with this.

## Disclaimer

The cluster is essentially a fixed and shared set of hardware by all of
the research department of M&CS. Policy states that all hardware must
remain available for everybody at all times: this means isolation of
machines for individual cases is **not** possible. Also take into
account, you can expect that there are waiting times (of unexpected
length), improper use of resources by others and that in the end, the
cluster might not be a suitable place for your type of job. Know that we
do have alternatives (please contact your [Research IT
consultant](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/Research-IT.aspx){:target=_blank}
for the options).

## Relevant technical aspects

All specifications of the machines in the cluster are stated
[here](../../specifications.md).
There is a quota of 1 TB on every user's home directory. Because there
is roughly 95TB in total, there is likely no room for everyone to fill
up their quota completely. **Do not  use the cluster as a place to store
data** . Every compute node does have slightly over 2 TB of scratch
storage available under /local, which does not fall under the quota (but
is deleted once a job finishes). **The data residing on the HPC cluster
has no back-up!**

## Documentation

You can browse the HPC wiki and read about how to login, transfer files
to and from the cluster, define and submit compute jobs, track their
progress, work with specific tools/software, *et cetera*.

## Community

We have a
[mailinglist](https://listserver.tue.nl/mailman/listinfo/hpc-users.mcs){:target=_blank}
and a [Teams
environment](https://teams.microsoft.com/l/team/19%3afe39019482c34550824bebc871cc4b71%40thread.tacv2/conversations?groupId=a54d5913-08b9-4082-a13b-d60296906068&tenantId=cc7df247-60ce-4a0f-9d75-704cf60efc64){:target=_blank}
for all communication concerning this cluster. Please subscribe if you
want to think along about cluster development/expansion; know about
technical changes or outages; be informed about workshops and hand-on
sessions, *etcetera*. Next to that, feel free to reach out to your
co-users when you have doubts about their way of using the cluster.

## Specialized support

Support on your code and/or scripts is available! Contact [HPC
lab](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/HPC-Lab.aspx){:target=_blank}
for a consultant.

## User guidelines

**GENERAL PRACTICES**

- Please consider at any time the impact of the job you’re about
to run (given (expected) wall time, allocation of resources, etc.). **Be
especially considerate of running jobs that need a disproportional
amount of cores w.r.t. what has been allocated** (i.e., if your
allocation of resources in your script does not reflect what you
actually use)): this prevents others from using the unused resources.
- Do not compile code on the log-in node.
- Practical suggestions, tips, and practices on how to use the
cluster are collected and shared on this website. For example, are you
using Tensorflow on the GPUs? Read [here](gpu.md) for best practices.

In case you need compute resources for:

- …education,
- …benchmarking,
- …working with a virtual machine,
- …compute a job that needs a lot of RAM,
- …jobs that take more than 7 days on the cluster,
- …development,
- …jobs that cannot run multi-threaded,

The cluster might not be the best fit for your purpose. Please contact
hpcsupport@tue.nl to discuss other options to consider with comparable
functionalities and reasonable border conditions.

## Rules

**(TECHNICALLY) ENFORCED RULES ON CLUSTER**

-         Required to specify the number of cores/RAM explicitly for GPU queue
-         Fixing an equal distribution for every user w.r.t. number of jobs scheduled
-         Implementing a priority system (FAIR system). As this is WIP, a cap (=3) on the number of nodes one can claim will be enforced
-         A limit on wall time (being 7 days)
