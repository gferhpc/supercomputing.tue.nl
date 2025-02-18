---
title: M&CS High Performance Computing
---

# M&CS High Performance Computing

!!! info "Documentation by M&CS"

    This section of the documentation is maintained by M&CS. For suggestions
    to these pages, please contact
    [Hub MetaForum](https://tuenl.sharepoint.com/sites/intranet-mathematics-and-computer-science/SitePages/Hub-Metaforum.aspx){:target=_blank}.

## Introduction
A part of the TU/e umbrella cluster can be used by the Department of
Mathematics and Computer Science. It is made available for all research staff
for **small- to medium-scale job-based compute needs**. The facility originates
from a collectively expressed need by M&CS research in 2019 for low-barrier
(close to home but serviced) compute resources that could facilitate
most of the computations. The main goal was to enable an **experimental
environment to test jobs** where one would not have to worry
about unnecessarily burning rented compute hours from external
resources.

When using the system, be aware of the impact your type of job has on the
experience of others that you share the hardware with: the remarks later on this
page aim to help you with this.

!!! abstract "Characteristics"

    * Ideal for getting started with high performance job-based computing
    * Account life cycle management by LIS
        * [Get access](../../steps/request/index.md) to the M&CS cluster **within 2 working days**
        * Don't worry about account creation and forgetting passwords: use your TU/e account
    * Setup and maintenance done by the Eindhoven Supercomputing Center
        * Don't worry about buying and maintaining hardware
        * Your **[favourite software](../../software/index.md) is available** without any additional steps, [TU/e (network) licenses](../../software/licenses.md) can be used
    * Funded by department-wide funds
        * No funding proposal/credits needed
        * Unfunded research possible
            * Experimental use: **get to know high-performance computing**
            * Small to medium-scale compute needs
            * BSc/MSc seminar or thesis projects²
            * EngD/PhD candidates
    * **Share resources fairly**
        * No reservations possible, all nodes are available for all M&CS research
        * Get an equal fraction of resources using Slurm's Fairshare¹
    * Next steps: commercial HPC infrastructure, Snellius

## Documentation
For documentation on the umbrella cluster, you can use the navigation on the
left of this page.

### Technical specifications
All specifications of the machines in the cluster can be found
[here](../../specifications/index.md#mcs). Users are given their own 'home'
folder under `/home/[username]` and shared scratch space is available under
`/scratch-shared/[username]`. The M&CS nodes have an additional **2 TB** of
node-specific scratch space available under `$TMPDIR`. Please review
[this page](../../filesystems.md) to see what storage is appropriate for 
different types of data (and for how long data will be stored). The mentioned
file systems are **not** backed up.

## Community
We have a
[mailinglist](https://listserver.tue.nl/mailman/listinfo/hpc-users.mcs){:target=_blank}
and a [Teams
environment](https://teams.microsoft.com/l/team/19%3afe39019482c34550824bebc871cc4b71%40thread.tacv2/conversations?groupId=a54d5913-08b9-4082-a13b-d60296906068&tenantId=cc7df247-60ce-4a0f-9d75-704cf60efc64){:target=_blank}
for all communication concerning this cluster. Please subscribe if you
want to think along about cluster development/expansion; know about
technical changes or outages; be informed about workshops and hand-on
sessions, *etcetera*. Next to that, feel free to reach out to fellow
users when you have doubts about their way of using the cluster.

!!! question "Specialised support"

    Support on your code and/or scripts is available! Contact [TU/e Supercomputing
    Center](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/Supercomputing-center.aspx){:target=_blank}
    for a consultant.

## Policies & guidelines
The cluster is essentially a fixed and shared set of hardware by all
researchers of M&CS. Policy states that all hardware must
remain available for everybody at all times: this means isolation of
machines for individual cases is **not** possible. Also take into
account, you can expect that there are waiting times (of unexpected
length), improper use of resources by others and that in the end, the
cluster might not be a suitable place for your type of job. Know that we
do have alternatives (please contact your [Research IT
consultant](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/Research-IT.aspx){:target=_blank}
for the options).

- Please consider at any time the impact of the job you’re about
to run (given (expected) wall time, allocation of resources, etc.). **Be
especially considerate of running jobs that need less resources than
what has been allocated** (e.g. if you allocate 16 cores, but your script
only starts 4 threads); this prevents others from using the unused resources.
- Do not compile code or run compute tasks on the log-in node.
- Practical suggestions, tips, and practices on how to use the
cluster are collected and shared on this website. For tips on using the GPU
nodes, plesae see [this page](gpu.md) for best practices.

If you have any questions about whether the M&CS HPC cluster is the best fit
for your work, please review the [other solutions](./index.md) or contact your
[Research IT consultant](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/Research-IT.aspx){:target=_blank}.

### Rules (partition policies; technically enforced)
- Slurm's Fairshare is used¹
- Wall-time limit (7 days for M&CS)
- Required to specify the number of cores/RAM explicitly for GPU queue

¹ For each researcher, usage in the last 5 minutes is computed as a fraction
of available resources. Jobs from researchers with a lower usage fraction are 
started first. This allows for a fair distribution of jobs during popular 
times.<br/>
² Access for students should be requested by the supervisor. The supervisor
is expected to be familiar with the service and able to assist in 
ensuring efficent resource usage. For large-scale use in education 
(e.g. courses), please contact 
[Hub MetaForum](https://tuenl.sharepoint.com/sites/intranet-mathematics-and-computer-science/SitePages/Hub-Metaforum.aspx){:target=_blank}
to look for a better alternative.