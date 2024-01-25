---
title: Python
tags: [Software, Module]
---

Please open a terminal and log in to the cluster.

To open an interactive Python session, simply type `python3`. If you
then type in `print("This is clearly working")`, the text will appear in
the output of this line. Exit the session by typing `exit()` or press
\`Ctrl + D\`.

If you want to run a script (a `*.py` file), you must first
create/upload the `*.py` file. Open a text editor and write your own
Python script, or use this dummy example:
```shell
#!/usr/bin/env python3
#SBATCH --partition=tue.test.q
#SBATCH --output=openme.out

print("This is clearly working")
```
Save it as `test.py`. Then use, e.g., Command Prompt to transfer this
file to the cluster by typing in:

`scp test.py `<yourid>`@hpc.tue.nl:myjob/`

You could now run the script on the login node by typing the command
`python3 test.py`. This runs your script on Python 3.6.1. You could also
choose to run it on Python 2.7.5 by changing it into `python2 test.py`.

**However**, the login node of the cluster is not meant to run heavy
calculations and your job will be terminated when it takes too much
resources (CPU, memory, time). To properly [schedule](../../steps/jobs/index.md) the job like
we did before, you have to run:

```shell
sbatch test.py
```

Once the job completes, you will see that a file `openme.out` has been
created which contains `This is clearly working` as expected.

### Virtual environments

We recommend you to work within a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/){:target="_blank"}
if you work with Python packages. This is essentially a local directory
where all packages you install are stored, so as to not interfere with
system packages or other projects you might have. Usage is quite
straightforward. First, create an environment and chose a name for it
(and the directory):

`python3 -m venv my-python-environment`

After that one-time step, you can activate the environment at any time
using

`source my-python-environment/bin/activate`

and deactivate the environment by executing `deactivate`. Your prompt
should indicate if a virtual environment is active, if you use it in an
interactive session.

Within this environment, you can freely install and upgrade packages
using pip. You can start with `pip install --upgrade pip` to make sure
the package manager is on the latest version, followed by
`pip install `<package> to install whatever you need.

#### Check availability and install packages

To check the availability of a package, use the command
`pip show `<package>. If the package is installed, the command will
return the version and some other information about it. Otherwise the
command will issue a warning, and you can then install the package as
follows:

`pip install <package>`

### Using Anaconda

If you want to use [Anaconda](https://www.anaconda.com/){:target=_blank}, you will have
to load a module: `module load anaconda`. Several versions are
available, as you can see by running `module avail anaconda`. The former
command will load the current version of Anaconda (which is kept
up-to-date on a best effort basis). Loading this module will make
several executables available, among which `anaconda`, `conda`, `flask`
and `jupyter`. You *can* then directly use those in your script. We do
however recommend you to always work in a [virtual environment](#virtual-environments).

`conda` in fact allows you to create
[environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html){:target="_blank"}
and even to install a specific version of Python for an environment.
This enables even more flexibility. As opposed to the built-in `venv`
module of Python, Anaconda environments are stored in a central location
in your home directory. You can thus activate environments regardless of
your current working directory.

```shell
module load anaconda
conda config --set auto_activate_base false
conda init bash

source ~/.bashrc

conda create --name my-python-3.9 python=3.9
```

After that, you can at all times activate your environment as follows:

```shell
module load anaconda
conda activate my-python-3.9
```

In an sbatch script, be sure to `source ~/.bashrc` as well, because
Slurm does not do that automatically.

To list your environments, use:

```shell
conda env list
```

And clean up environments you no longer need by running:

```shell
conda env remove --name my-python-3.9
```

Within an environment, you can `pip install` libraries just like in
Python `venv` without impacting other environments.

### Using TensorFlow

If you want to use [TensorFlow](https://www.tensorflow.org/){:target=_blank}, you should
create a [virtual environment](#virtual-environments),
activate it and then
`TMPDIR=~/.tmp/ pip install --build ~/.tmp/ tensorflow`. This is a
slight variation on the `pip install tensorflow` command you might
expect, which is needed because of the limited size of the `/tmp`
partition you get on the HPC cluster. Please try rerunning the command
once or twice if it fails due to too little disk space, before reporting
the problem. Please `rm -rf ~/.tmp` after the installation succeeds to
clean up the temporary build files.

When done, you can verify if the installation was successful by
executing

`python -c $'import tensorflow as tf\nprint(tf.__version__)'`

which should print something like `2.2.0`.

Now that you have installed TensorFlow, using it is a matter of
activating the virtual environment and importing it in your script.
