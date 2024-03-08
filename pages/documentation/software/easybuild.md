---
tags: [Software]
---
![EasyBuild logo](easybuild_logo_2022_vertical_dark_bg_transparent.png#only-dark){: align=right style="height:250px"}
![EasyBuild logo](easybuild_logo_2022_vertical_light_bg_transparent.png#only-light){: align=right style="height:250px"}
# EasyBuild
!!! note 
    This page serves as a reference to system administrators, but the curious user is welcome to read it as well.

EasyBuild helps building and installing software packages and their
dependencies using tested build scripts.

## Implementation

-   Software is built and installed using the "easybuild" user.
-   The easybuild user has a shell function `eb_env` that sets the
    environment for building in the test env or production env.
-   The test env is a software installation tree in the easybuild user's
    home dir.
-   The production env is in `/sw/rl8/{arch}/{app,mod}`
    where `{arch}` is the result of `module load archspec;archspec cpu`
    on a node in the `tue.build.q`.
-   We keep a private repository of installed easyconfigs in `~/easyconfigs`.
    Part of `~`, including the easyconfigs, is also on GitLab.
-   Software is built and installed using the `tue.build.q`, which makes
    use of the lowest common denominator micro architecture that we
    have. This produces builds that can run on all nodes, but with
    degraded performance.

## Installation procedure

Prerequisites:

-   Add your SSH public key to the authorized keys of the easybuild
    user. This will allow logging in as that user.

Procedure:

1.  Connect via SSH to the cluster as user "easybuild".
2.  Start a screen/tmux so building can continue when you lose connection

Search for software (built-in easyconfigs):

3.  Search for available easyconfig files: `eb -S {software}`
4.  Copy the desired easyconfig file to the right place in `~/easyconfigs`.
    `eb --copy-ec {easyconfig}` copies the easyconfig file to the current directory.

Search for software (e.g. easyconfigs pull requests on GitHub):

3.  Search for software in the [easyconfigs pull requests](https://github.com/easybuilders/easybuild-easyconfigs/pulls).
4.  Download the raw files to the right place in `~easyconfigs`.

Build:

5.  Start a shell in `tue.build.q`: `eb_srun`  (Optionally add number of CPU cores)
6.  Dry-run build: `eb -Dr {easyconfig}`
7.  Build and install: `eb -r {easyconfig} --parallel=8`

Add to GIT repo:

8.  `git add`, `git commit`, `git push` as needed.

## Building GPU easyconfigs -CUDA-xx.xx

When Building CUDA releated software, easybuild may complain about the cuda-compute-capabilities if so add the this option to the eb command ```--cuda-compute-capabilities=3.7,6.0,6.1,7.0,7.5,8.0,8.6``` which are the CUDA capabilities of the GPUs in the Umbrella Cluster. Or add this to the {easyconfig} ```cuda_compute_capabilities = {'3.7', '6.0', '6.1', '7.0', '7.5', '8.0', '8.6'}```

## Fixes and workarounds:

-   Software that uses OpenMPI cannot correctly be started by EasyBuild,
    when EasyBuild is running from within srun, causing self-tests to
    fail. Running the self-tests with srun, i.e.
    `srun {software-self-test}`, works. A workaround is to build such
    packages outside the srun session, e.g. through SSH on the same
    node.
-   If EasyBuild cannot download a source tarball, you can download it
    manually and put it somewhere in `~/.local/easybuild/sources` or `~easybuild/easyconfig` (don't add sources to GIT). Take
    note of the structure of that dir first!

## Pain points

-   EasyBuild offers very little flexibility in software versions built:
    only software versions for which easyscript files exist can be
    built, and the dependecy versions are hardcoded. EasyBuild allows
    some flexibility with `--try-toolchain` and `--try-software`, but
    for building FEniCS this failed.

