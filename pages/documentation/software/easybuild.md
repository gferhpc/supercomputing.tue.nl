---
tags: [Software]
---
# EasyBuild

!!! note 
    This page serves as a reference to system administrators, but the curious user is welcomed to read it as well.

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
3.  `srun -p tue.build.q -N1 -n1 -c8 -t 1-0 --pty bash`
4.  Search for available easyconfig files: `eb -S {software}`
5.  Copy the name of the desired easyconfig file if you want to edit the
    file and place it in de easyconfigs directory and GIT.
    `eb --copy-ec {easyconfig}` copies the easyconfig file to the current directory 
5.  Switch EasyBuild env to production: `eb_env prod`
    If you get "WARNING: Did not unuse ...", repeat the command until it
    succeeds. This should take about 3 tries.
6.  Dry-run build: `eb -Dr {easyconfig}`
7.  Build and install: `eb -r {easyconfig} --parallel=8`
8.  Add the easyconfig file `{easyconfig}` to the `~easybuild/easyconfig` directory and
    commit/push to GIT. Take note of the structure of that dir first!

## Building GPU easyconfig (-CUDA-xx.xx)

When Building CUDA releated software, easybuild may complain about the cuda-compute-capabilities if so add the this option to the eb command ```--cuda-compute-capabilities=3.7,6.0,6.1,7.0,7.5,8.0,8.6``` which relflect the CUDA capabilities in the Umbrella Cluster.

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

