---
title: Virtual Machines
---

> On June 1, 2023, all M&CS virtual machines (VMs) will be transferred
> from the old vcenter to the new vcenter environment (see concerned VMs
> in attached word document).
>
> That means, if you are an owner, that all of your VMs in open nebula
> will go offline (i.e., they will stop running) for a few hours.
>
> NB: In order to have the machines online (and running) again after
> June 1, the owner of the machine has to login to the new open nebula
> website
>
> <https://mynebula.tue.nl/fireedge/sunstone/vm>. If you have any
> left-over questions, need help with above instructions, or if you want
> to postpone the migration day, contact Tijs Poort.

On our cluster of vmware servers we provide space for virtual machines.

For you as a (future) user, that is, operator, of a virtual machine, it
is just a machine that you install and operate remotely without ever
touching it.

After installation, it will provide services for production or testing
purposes.

Users of such services will not note the difference with physical
machines.

There are however application areas where virtual machines are better
suited than physical machines. They include:

-   course assignments
-   prototyping
-   monitoring
-   licence servers

or, more general, applications that require relatively small resources
and one or more of:

-   reliability of storage
-   facilities to save snapshots of the system state
-   remote access, with authentication, to the boot procedure
-   independence of hardware upgrades

**Request a VM**

Employees and students can request virtual machines to run Windows and
Linux systems via lisservices@tue.nl.

Please include these details in your request:

-   a short hostname Your virtual machine will be accessible as
    > *`shortname`*`.win.tue.nl`

    It is up to you to install and provide services, often for testing
    purposes, on your virtual machine.
-   type of OS, one of:
    -   Windows, optionally pre-installed
    -   Linux: 32 or 64 bit, you always need to install that yourself
-   operators, accounts that need access to *operate* the virtual
    machine:
    -   reset, power on and off
    -   enter input and view feedback at the virtual console especially
        to install system software and therefore need access to the
        virtual machine *environment*. It is up to you to provide access
        to services that you will run on the virtual machine *itself*
        and to create accounts to setup, use or test such services.
-   estimated required disk space in addition to system-software. For
    example, the entire matlab suite takes 8 GB of diskspace.
-   estimated required memory
-   the subnet, implying a choice for network access.
-   end date or estimated end date. The availability can be extended
    later.
-   For SEP assignments also the SEP group number

Resources such as memory can be changed later, the virtual machine needs
to be down to apply the changes.