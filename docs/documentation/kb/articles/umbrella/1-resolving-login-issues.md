---
date: 2025-04-02
authors: [ e.loomeijer ]
type: kb
slug: "1"
tags: [ "Umbrella", "Knowledge Base", "Account" ]
categories: [ "Umbrella", "Account" ]
---

# Resolving Login Issues with SSH and OpenOnDemand

When accessing the TU/e Umbrella HPC Cluster, you might encounter login issues. This guide provides a step-by-step 
approach to resolving them.

## 1. Ensure You Are on the TU/e Network

Access to the TU/e Umbrella HPC Cluster requires you to be connected to the TU/e network. 

For this you'll need either to be on campus, or connect to
[TU/e VPN Services](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/New-VPN-Service--eduVPN.aspx){:target=_blank}. 

## 2. Check the Address

Ensure you are using the correct address for accessing the HPC resources.

For OpenOnDemand ensure you're using [https://hpc.tue.nl](https://hpc.tue.nl){:target=_blank}. When using SSH, 
the command should be similar to one of the following:
```shell
ssh USERNAME@hpc.tue.nl
ssh hpc.tue.nl -l USERNAME

# USERNAME needs to be replaced with your actual username
```

## 3. Verify Your Username

Your username should be your TU/e network name. This is (usually) a numeric ID. Double-check for
typos or incorrect capitalization.


!!! success "Valid Usernames"

    Most users have a 8-digit numeric ID as username, but for historically reasons you may still have a "s" (student number) or 
    have a named username.

    - **Numerical Accounts** _(8 digits)_
            
        `20191262`, `20243781`, etc...

    - **Student Accounts** _(s-number)_

        `s160320`, `s168334`, etc...

    - **Named Accounts**

        `rzoontjens`, `ahoof`, etc...

??? danger "Invalid Usernames (examples)"

    - **E-Mail addresses can't be used**  

        - l.s.surname@tue.nl
        - l.s.surname@student.tue.nl

    - **Usernames can't contain NETBIOS names**
    
        - TUE\20191262
        - 20191262@TUE

## 4. Verify Your Password

Make sure you are entering the correct TU/e password. This should be the same password you use for other TU/e systems.
If you suspect the password might be incorrect:

- Try logging into another TU/e service to confirm it's working.
- If necessary, reset your password.

## 5. Check for Expired Accounts

Typically, Umbrella HPC accounts expire about a year after the initial request and needs periodic renewal to ensure your
account remains active. Account renewals can be requested through our [Service Portal](https://tue.topdesk.net/tas/public/ssp/content/serviceflow?unid=a745121fa0ab45f2b24aaaf64060760f){:target=_blank}.
