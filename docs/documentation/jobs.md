---
title: 5. Submit Jobs
tags: [SLURM]
---
# Submit Jobs

The HPC Umbrella Cluster uses SLURM (Simple Linux Utility for Resource
Management) as its scheduler. SLURM uses the term partition to describe
a part of the Cluster, a partition groups a number of nodes with the
same characteristics like the number of CPUs per node, the CPU/GPU type
and Memory size. Note that nodes can be part of more than 1 partition.
These partitions are also named queues and those names are often used
interchangeable. Access to partitions is given to a group or groups.
Accounts on the HPC Umbrella Cluster can be a member of 1 or more
groups. Each partition or queue can have different constrains such as
the maximum wall time (how long a job can run) the maximum nodes per
job.

After logging in on the login node:

Checking access to partition/queues: **sinfo**

Checking group membership: **id**

## Per-partition constraints

The table below lists all configured partitions, and per partition also
lists the following:

-   constraints on maximum job wall-time (the maximum time a job can
    run);
-   constraints on maximum number of nodes per job;
-   priority tier of jobs in this partition; and
-   user groups that can use this partition.

Note that if you're not in one of the groups that is allowed to use a
certain partition, the scheduler will not accept your job and instead
give the following error:

    sbatch: error: Batch job submission failed: User's group not permitted to use this partition

| Partition         | Max wall-time[1] | Max nodes/job[2] | PriorityTier[3] | Allowed groups                 |
|-------------------|------------------|------------------|-----------------|--------------------------------|
| be.gpuresearch.q  | UNLIMITED        | UNLIMITED        | 1               | be-research                    |
| be.gpustudent.q   | UNLIMITED        | UNLIMITED        | 1               | be-student                     |
| be.research.q     | UNLIMITED        | UNLIMITED        | 1               | be-research                    |
| be.student.q      | UNLIMITED        | UNLIMITED        | 1               | be-student                     |
| bme.gpuresearch.q | UNLIMITED        | UNLIMITED        | 1               | bme-research                   |
| bme.gpustudent.q  | 7-00:00:00       | UNLIMITED        | 1               | bme-student                    |
| chem.6ema08.q     | 5-00:00:00       | UNLIMITED        | 2               |                                |
| chem.default.q    | 5-00:00:00       | UNLIMITED        | 1               | chem,chem-guest                |
| chem.gpu.q        | UNLIMITED        | UNLIMITED        | 1               | chem,chem-guest                |
| chem.longterm.q   | 14-00:00:00      | UNLIMITED        | 2               | chem,chem-guest                |
| chem.smm01.q      | UNLIMITED        | UNLIMITED        | 1               | chem-smm                       |
| chem.smm02.q      | UNLIMITED        | UNLIMITED        | 1               | chem-smm                       |
| elec.default.q    | UNLIMITED        | UNLIMITED        | 1               | elec                           |
| elec-em.gpu.q     | UNLIMITED        | UNLIMITED        | 1               | elec-em,elec-em-guest          |
| elec.gpu-es02.q   | UNLIMITED        | UNLIMITED        | 1               | elec-es                        |
| elec.gpu.q        | UNLIMITED        | UNLIMITED        | 1               | elec-es,elec-5LIL0             |
| elec-phi.gpu.q    | UNLIMITED        | UNLIMITED        | 1               | elec-phi                       |
| id.fe.q           | 5-00:00:00       | UNLIMITED        | 1               | id-fe                          |
| mcs.default.q     | 7-00:00:00       | 3                | 1               | mcs                            |
| mcs.gpu.q         | UNLIMITED        | UNLIMITED        | 1               | mcs                            |
| mech.cm.q         | 5-00:00:00       | UNLIMITED        | 1               | mech-cm,tue-support            |
| mech.pf.q         | UNLIMITED        | UNLIMITED        | 1               | mech-pf,mech-et                |
| mech.student.q    | 5-00:00:00       | UNLIMITED        | 1               | mech-student                   |
| phys.and.q        | UNLIMITED        | UNLIMITED        | 1               | phys-and                       |
| phys.bigmem.q     | UNLIMITED        | UNLIMITED        | 1               | phys                           |
| phys.default.q    | UNLIMITED        | UNLIMITED        | 1               | phys                           |
| phys.edu.q        | UNLIMITED        | UNLIMITED        | 1               | phys-3mq110,phys-ccer          |
| phys.gpu.q        | UNLIMITED        | UNLIMITED        | 1               | phys                           |
| phys.psn.q        | UNLIMITED        | UNLIMITED        | 1               | phys-psn                       |
| phys.simbeyond.q  | 5-00:00:00       | 1                | 1               | phys                           |
| tue.default.q     | 7-00:00:00       | 2                | 1               | elec,tue,ieis,tue-hpc,chem,bme |

Partition/Queue constraints on TU/e HPC Umbrella Cluster

<references />

[1] Maximum time a job can run (Days-Hours:Minutes:Seconds). The job
will be killed if **Max wall-time** is reached.

[2] Maximum number of nodes a job can allocate

[3] A higher priority schedules a job sooner, applicable when node(s)
are in more than one partition