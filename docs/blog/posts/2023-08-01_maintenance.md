---
draft: false 
date: 2023-08-01
categories: [Umbrella]
tags: [HPC]
authors: [a.van.hoof@tue.nl]
---

# Umbrella Cluster Maintenance

## What did happen?

*Maintenance: the Cluster Scheduler (Slurm) was upgraded to version 22.05.9 and the Cluster Manager (Bright Cluster Manager) to version 9.2.
*Security: firmware updates were installed on all hardware and the OS (Centos 7.9) was upgraded to include the latest security patches.
*Extra: the NewBuild/AMD module is now loaded by default.

<!-- more -->

## What is the impact?

*As the NewBuild/AMD module is now loaded by default, a lot of extra modules are available by default, ScyPy, PyTorch and R, just to name a few. The foss/2022a module has a more recent GCC and OpenMPI.
*When using more memory than available on a node swap will not be utilized and the job will be cancelled.
*Other changes allow the HPC Lab to implement more features and add usability; more information will follow.

## What do you need to do?
Just use the cluster as always. If have issues, first check the maintenance FAQ: [https://hpcwiki.tue.nl/wiki/Detailed_Information_Maintenance_August_2023#Known_issues Known Issues]

## Reminder:
Data (incl. home directories) in the HPC Cluster is NOT backed up! The HPC Cluster is not a solution for archiving your work!

You are FULLY responsible for your own data management!

## Questions?
For questions and remarks please contact [mailto:hpcsupport@tue.nl hpcsupport@tue.nl].

## Known issues

If your issue is not on this list, please contact us!

### Lumerical
Lumerical has issues running through SSH with X11 forwarding enabled. If possible, try to avoid using Lumerical with X11 forwarding. Instead, use the following workflow:

> Prepare your job in the Open OnDemand web interface, in an interactive desktop session.
> Once your .LSF file is prepared, submit a job; see https://hpcwiki.tue.nl/wiki/Ansys_Lumerical#Submitting_a_Lumerical_job
> Once your job is done, view the results using the Open OnDemand web interface.

More detailed instructions can be found [[Ansys Lumerical|here]]. If you experience further issues, or if this workflow doesn't suit your needs, please contact us.
