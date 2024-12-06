# Slurm Viewer

Slurm Viewer^[:fontawesome-brands-git:](https://gitlab.com/lkeb/slurm_viewer){:target=_blank}^ (**slurm-viewer**) is a Graphical Command Line
Interface to the Slurm Scheduler. View the status of a SLURM cluster, including nodes and partitions/queues. It is
available as a [module](../../steps/software/index.md) on the login node and needs initialization once.

Load the module

```shell
user@umbrella$ module load SlurmViewer
```

Initialize SlurmViewer, only needed once, after this you can edit `~/.config/slurm-viewer/settings.toml` anytime.

```shell
user@umbrella$ slurm-viewer-init
```

Start SlurmViewer

```shell
user@umbrella$ slurm-Viewer
```

![SlurmViewerExample](SlurmViewerExample.png)

Use 'q' to quit. The interface can be used with a mouse (it's clickable)
