---
title: M&CS Virtual Machines
---

# M&CS Virtual Machines

!!! info "Documentation by M&CS"

    This section of the documentation is maintained by M&CS. For suggestions
    to these pages, please contact
    [Hub MetaForum](https://tuenl.sharepoint.com/sites/intranet-mathematics-and-computer-science/SitePages/Hub-Metaforum.aspx){:target=_blank}.

The Department of Mathematics & Computer Science has a cluster of
VMware ESXi servers. On this cluster, virtual machines (VMs) are provided for
researchers and educators of M&CS.

For users (operators), the VM will behave like a regular physical machine
without having to worry about hardware maintenance. After installation, it will
provide services for production or testing purposes. Users of such services
will not note the difference with physical machines.

The VM cluster is suitable for applications that require relatively small 
resources. The cluster provides

-   reliability of storage
-   facilities to save snapshots of the system state
-   remote access, with authentication, to the boot procedure
-   independence of hardware upgrades

!!! abstract "Characteristics"

    * Ideal for getting started with hosting custom applications &amp; continuous usage
    * Virtual machine set up by Hub MetaForum
        * [Get access to a VM](./virtual_machines.md) in the M&CS environment **within 5 working days**
        * Limited support for own software by lab manager
    * Hardware and platform maintenance by LIS
        * Don't worry about buying and maintaining hardware
        * Available with Ubuntu Server or Windows Server (other OS'es in consultation)
        * Access through virtual console, RDP (Windows) and SSH (Ubuntu)
    * Flexible software solutions    
        * Install and maintain your own software
        * Enable automatic updates
    * Funded by department-wide funds
        * No funding proposal/credits needed
        * Unfunded research possible
            * Experimental use: **proof of concept, short-lived projects, prototyping**
            * Small-scale compute needs
            * BSc/MSc course assignments (software engineering project), seminar or thesis projects²
            * EngD/PhD candidates
    * **Share resources fairly**
        * Resources are shared for all M&CS education and research needs
        * Maximum 4 CPU cores, 16GB RAM, 250GB storage³
    * Next steps: Azure, SURF Research Cloud

    ³ If more is needed, an evaluation should be made what the best solution is for
    your needs; for this, please contact
    [Hub MetaForum](https://tuenl.sharepoint.com/sites/intranet-mathematics-and-computer-science/SitePages/Hub-Metaforum.aspx){:target=_blank}.

## Access to the management interface
Currently, a management interface, MyNebula, is provided.

The interface is available on [mynebula.tue.nl](https://mynebula.tue.nl){:target=_blank}
(campus network or VPN only) and allows you to start/stop and remotely manage
the VM without using SSH/RDP.

!!! info "Management interface update"

    MyNebula is no longer maintained for use with VMware ESXi and usage will
    be phased out at the start of 2025. For users that have a reason for console
    access, an alternative will be provided. Existing users of MyNebula will be
    contacted about this by the support engineer.

## Request procedure
New virtual machines can be requested through TOPdesk SSP. Please use the
[Request Server Hosting](https://tue.topdesk.net/tas/public/ssp/content/serviceflow?unid=936bf107e86a464f927122f17dc20b07){:target=_blank}
form. 

**Budget/Budgetholder**: for the M&CS cluster, you can enter "/" in both fields.

**Functional Point of Contact**: contact for administrative tasks.
For physical servers, this includes the procurement process, but for VMs in the
M&CS ESX cluster this role is limited.

**Technical Point of Contact**: contact in case of e.g. security
incidents or maintenance and is also able to request changes.<br/>
The initial user account created by us will also be for this user.<br/>
*If the functional point of contact and technical point of contact are the same
person, please provide a backup technical contact.*

**CPU/Memory/Harddisk (system/data)**: please include all requirements 
regarding technical specifications in your request.

**Function server**: include a brief description of what the server will do
**and a preference for a hostname (ending in `.win.tue.nl`)**.

**Operating system**: we offer Windows and the latest Ubuntu Server LTS. If
you need a specific operating system or a custom image, please contact
the lab manager before making your request (and leave this field empty when
submitting your request).

**Firewall**: please list all applications that will be accessible on the
machine and who needs to access this. As a matter of policy, SSH, remote
desktop services and alternatives are only accessible from the campus network.<br/>
If you host a web server that needs to be publicly accessible, this commonly
uses port 80 (HTTP) and 443 (HTTPS). If you are still unsure, note that you
can also request changes later.

**Third-party access**: on the M&CS cluster third-party access for
maintenance/installation is **not** allowed. This means that for example in
the case of a webserver, a third party may access website functionality, but
may not remotely connect to the server through SSH/remote desktop.

**Backup**: the cluster does **not** offer a backup solution; users are
requested to make backups of critical files themselves.

In the **extra information** field, please include that the request should be
redirected to "LIS-MetaForum". Please also include an (estimated) end date
after which the VM is no longer needed. Virtual machines need to be renewed
once a year for security and maintenance reasons. 

!!! info "Software Engineering Project (2IPE0/2IRR30)"
    Typically during software engineering projects, a demo is needed. For some
    projects, a backend or website is required. The department supports these
    courses in providing the necessary server hosting.

    Students that take 2IPE0 or 2IRR30 can request 1 VM per group. The
    group may request a VM themselves. In case any assistance is needed with
    filling the request, please contact
    [Hub MetaForum](https://tuenl.sharepoint.com/sites/intranet-mathematics-and-computer-science/SitePages/Hub-Metaforum.aspx){:target=_blank}.
    Please note that processing the request may take [some time](./index.md),
    so request the VM once you know that you will be needing it.

    We will set up the VM including Windows/Ubuntu Server and will help with
    (requesting) any changes to the TU/e environment, such as network rules,
    but no support is given on installing and configuring software. 

    Please include the specifications that are needed and provide a (brief)
    reasoning for the requested specifications. To make sure that resources
    are allocated fairly, we will review this reason. 

    The end date will be the first day of the next quartile. After the 3 day 
    grace period, we will shut down your VM if we have not heard anything else
    from you. If your VM is needed for a longer period, please request an
    extension and include the approval of your supervisor.<br/>
    If the VM is needed permanently, this is only possible if the 'client'
    is part of the Department of M&CS. 

## Responsibilities of the owner
As the owner of a virtual machine, you are responsible for all management of the VM, including the following:

* installing regular system updates in accordance with the [patch policy](https://tuenl.sharepoint.com/:b:/r/sites/LIS/DocumentManagement/Shared%20Documents/Policies/1-0008%20-%20SP07%20-%20Policy%20Patch%20Management.pdf?csf=1&web=1&e=ZOJMsE){:target=_blank}<br/>
*For Windows Server virtual machines this happens automatically*
* installing application updates in accordance with the [patch policy](https://tuenl.sharepoint.com/:b:/r/sites/LIS/DocumentManagement/Shared%20Documents/Policies/1-0008%20-%20SP07%20-%20Policy%20Patch%20Management.pdf?csf=1&web=1&e=ZOJMsE){:target=_blank}
* the system has its own firewall that only allows necessary incoming traffic

## Data classification & network access
As is also the case for physical servers, for virtual servers, we will ask
some questions regarding the data that will be processed. If the server
is meant to store and process personal/confidential data, additional security
measures need to be taken.

For most educational projects, the virtual machine will be part of a specific
network zone (the 'play zone'; here VLAN 468/469). This means that access
to the following resources is allowed:

* Any HTTP(S) destination
* TU/e GitLab server (`gitlab.tue.nl`) through HTTPS/SSH
* TU/e SMTP server (`smtp.tue.nl`)
* Other TU/e servers, provided incoming access is allowed on that server

Other access is blocked by default. If you need to access other destinations
(e.g. to SSH to a clients environment for copying files), please contact
Hub MetaForum to request the requirements and the impact for the data
classification. 

Remote management is only possible from the campus or the TU/e VPN. External
management is never allowed. Incoming access to for example a web server needs
to be requested during the VM creation or afterwards.