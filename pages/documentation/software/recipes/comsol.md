---
tags: [Software, Module]
---
# COMSOL

### Getting a license

Check the
[intranet](https://intranet.tue.nl/en/university/services/information-management-services/software/comsol-multiphysics/){:target=_blank}
for the procedure on how to get a license for using COMSOL.

### Running simulations on the cluster

![Comsol Settings](comsol_settings.png){ align=right width=250 }

If you want to use the cluster to compute COMSOL simulations, you have
two possibilities. One is to [submit your job](../../steps/jobs/index.md) similarly as you
do for other programs. Another possibility is to use the COMSOL
interface in your local computer. This short tutorial is about this
second possibility. It is focused on configuring your simulation using a
TU/e cluster. For more information, visit the [COMSOL
blog](https://www.comsol.com/blogs/how-to-run-on-clusters-from-the-comsol-desktop-environment/){:target=_blank}
where the procedure is explained in detail.

Once you are done with building your model and specifying the physics of
your study on COMSOL, you can configure your simulation on a cluster.
Check the settings used in the figure or follow the instructions bellow.

On the *Model Builder* menu, click on *Study \#* with the left button of
your mouse and selecting *Cluster Computing* from the menu. This will
add *Cluster Computing* as an item under *Study \#*. By clicking on this
item, the settings for cluster computing are open on the right of the
*Model Builder* menu.

On the *Computer cluster settings* submenu, choose from the dropdown
menu `user controlled` in *Settings* and `SLURM` in *Scheduler type*.
Leave the next two fields, *i.e.* the fields *Scheduler type* and
*User*, empty. In the field *Queue name*, fill the queue you want to
use, *e.g.* `tue.default.q`. Choose the queue according to your
department and the information in [Technical Specifications](../../specifications.md) of the clusters.

In the same submenu, check the boxes of *Specify external COMSOL batch
directory path* and *Specify external COMSOL installation directory
path* and respectively type the paths `/home/tue/`<user> (or
`home/phys/`<user> if you belong to the Applied Physics department) and
`/cm/shared/apps/comsol/5.5/multiphysics/`.

Assuming that you are using PuTTY and that you have generated a [SSH
key](../../steps/access/ssh.md#passwordless-authentication) to log in, you can fill the
remainder fields as follows. On the *Remote and Cloud Access* submenu,
choose from the dropdown menu `user controlled` in *Settings* and
\`check the box of *Run remote*. In the dropdown menu select `SSH` in
*Remote invoke command* and `Putty` in *Remote invoke command*. In the
*SSH directory* field, browse to the directory where PuTTY is installed
and, in the SSH key file, browse to the directory where you save you
private key, select the key, and click *Open*. You do not need to fill
the fields *Forward ports* and *Port host*. As *SSH user*, fill your
cluster username.

For the *File transfer command* field, choose from the dropdown menu
`SCP`. Fill the SCP fields similarly to the SSH fields, *i.e.*, choose
PuTTY and fill the directory for the program and public key. Once again
use you cluster username in *SCP user*. In the *Remote hosts* table, add
the cluster address `hpc.tue.nl` (or `compass.phys.tue.nl` if you belong
to the Applied Physics department).

You are nearly done, before pressing the *run* button to have your
simulations calculated on the cluster, read the next sections to learn
how to select the number of cores in your calculation and to log out
your computer while a simulation is running on the cluster.

### Selecting the number of cores

By default, COMSOL uses the total amount of available cores in a
computing node. This means that, depending on the queue that you are
going to use, the job can use up to 64 cores, which may (probably) be
too many for your calculation.

You can choose the number of cores by expanding the options under *Study
\#* on the *Model Builder* menu. Do the same with *Job configurations*
and select *Batch 1* to open the *Settings* menu. If this menu is not
visible, select the *eye* icon on the *Model Builder* menu to show more
options. This will open a popup menu from which you can check the
*Solver and Job Configurations* option. On the *Batch 1* settings, check
the option *Number of cores* and type the desired number of cores.

Finally, click on *run* to submit your job on the cluster. Follow the
status of your simulation in the table in the *External process* tab.

### Detaching/attaching/stopping jobs

If you want to log out or close the local interface, you should detach
your job first by clicking on the button in the right bottom corner of
the local interface (near the progress bar).

If you want to keep your job running on the cluster while you are logged
out of your computer or the COMSOL interface is closed, just close it
and click *yes* when asked if you want to save the changes to the file.
When you open your file again to resume your work, open the *External
process* tab on the right side under *Graphics*. Click on the first icon
to attach the job. The table below should update the current status of
your simulation.

If, instead, you want to stop your simulation, click on the second icon
in the *External process* tab. If you think that there is a problem with
your simulation or if the program did not respond as expected, you can
also log in on the cluster and cancel your jobs with `scancel`. Learn
more about the scheduler commands in [Using Slurm](../../steps/jobs/index.md) page of this wiki.
