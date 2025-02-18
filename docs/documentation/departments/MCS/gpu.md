---
title: GPU Usage
---

# M&CS High Performance Computing - GPU Partition

!!! info "Documentation by M&CS"

    This section of the documentation is maintained by M&CS. For suggestions
    to these pages, please contact
    [Hub MetaForum](https://tuenl.sharepoint.com/sites/intranet-mathematics-and-computer-science/SitePages/Hub-Metaforum.aspx){:target=_blank}.

## Introduction
M&CS also has two GPU nodes available for GPU-based compute needs. It is
available as `mcs.gpu.q` and was purchased at the same time as the CPU
nodes.

A part of the TU/e umbrella cluster can be used by the Department of
Mathematics and Computer Science. It is made available for all research staff
for **small- to medium-scale job-based compute needs**. The facility originates
from a collectively expressed need by M&CS research in 2019 for low-barrier
(close to home but serviced) compute resources that could facilitate
most of the computations. The main goal was to enable an **experimental
environment to test jobs** where one would not have to worry
about unnecessarily burning rented compute hours from external
resources.

## Documentation
For documentation on the umbrella cluster, you can use the navigation on the
left of this page.

### Technical specifications
All specifications of the machines in the cluster can be found
[here](../../specifications/index.md#mcs). Users are given their own 'home'
folder under `/home/[username]` and shared scratch space is available under
`/scratch-shared/[username]`. The M&CS GPU nodes have an additional **200 GB**
and **500 GB** of node-specific scratch space available under `$TMPDIR`. Please
review [this page](../../filesystems.md) to see what storage is appropriate for 
different types of data (and for how long data will be stored). The mentioned
file systems are **not** backed up.

## Community
See also the
[community section of the general M&CS HPC page](./hpc.md#community).

!!! question "Specialised support"

    [TU/e Supercomputing
    Center](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/Supercomputing-center.aspx){:target=_blank}
    offers support for AI/ML tasks! Contact them for a consult.

## Policies & guidelines
The GPU nodes are shared by all researchers of M&CS. Policy states that all
hardware must remain available for everybody at all times. 

- Please consider at any time the impact of the job you’re about
to run (given (expected) wall time, allocation of resources, etc.). **Be
especially considerate of running jobs that need less resources than
what has been allocated** (e.g. if you allocate 16 cores, but your script
only starts 4 threads); this prevents others from using the unused resources.
- Do not compile code or run compute tasks on the log-in node.

If you have any questions about whether the M&CS HPC cluster is the best fit
for your work, please review the [other solutions](./index.md) or contact your
[Research IT consultant](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/Research-IT.aspx){:target=_blank}.


??? example "Example for buffering datasets that do not fit into RAM"

    In case you have a dataset that fits into local SSD storage, but cannot
    be loaded completely into RAM (see the limits [below](#rules-partition-policies-technically-enforced)),
    please follow the instructions presented below for dynamically buffering
    data from local SSD storage into RAM memory with a particular
    experimentation framework of choice. In case no instructions
    are provided for your experimentation framework of choice, feel free to
    send us instructions so that we can add the instructions on this page.

    <span style="color:red">Note: never buffer from the main storage node
    via the head node!</span> Buffering from the main storage node will
    cause the HPC to become unusable for everyone and is slow. Before
    you start with running your experiment scripts, first copy your dataset
    from e.g. `/home/[login name]/DATASET_FOLDER` to
    `$TMPDIR/DATASET_FOLDER` at the GPU node. Local SSD storage works via a
    NVMe interface which is suitable for buffering which requires many IO
    operations per second. When you have finished your experiments, please
    remove your `DATASET_FOLDER`, including the data residing in this folder,
    at the local SSD storage of the GPU node so that local storage does not
    get clogged with stale datasets.

    **Tensor flow**

    TensorFlow provides an input pipeline API called the `tf.data` API. There
    are two ways in which data can be buffered dynamically into RAM memory:
    either via loading many small files or slicing into a large file with a
    file format that is supported by the TensorFlow I/O collection of file
    systems and file formats. Examples are provided in Algorithms 1 and 2.
    More information on how the specific functions listed in Algorithms 1
    and 2 make sure that overall training time does not increase due to
    buffering from local SSD storage can be found on [this external page](https://www.tensorflow.org/guide/data_performance){:target=_blank rel="nofollow"}.

    ``` py title="Algorithm 1: Tf.data API example when slicing into a large HDF5 file" linenums="1"
    import tensorflow_io as tfio
    import tensorflow as tf
    
    widar_hdf5 = tfio.IOTensor.from_hdf5(filename=<<PATH TO HDF5 FILE>>, spec={
      '/inputs': tf.TensorSpec(shape=(121, 2000, 6), dtype=tf.float32),
      '/task_labels': tf.TensorSpec(shape=(6,), dtype=tf.int8),
      '/domain_labels': tf.TensorSpec(shape=(150,), dtype=tf.int8)
    })
    widar_inputs = widar_hdf5('/inputs')
    widar_task_labels = widar_hdf5('/task_labels')
    widar_domain_labels = widar hdf5('/domain_labels')

    def get_sample(instance):
      return (
        widar_inputs[instance], (
          widar_task_labels[instance],
          widar_domain_labels[
          ...
          ]
        )
      )
    
    train_instances = [1, 2, 4, 8, 16, 17, 18, 19, 24, 46, 61, 63, 128, ...]
    
    train_set = tf.data.Dataset.from_tensor_slices(train_instances)
    
    train_set = train_set.shuffle(
      buffer_size=len(train_instances),
      seed=42,
      reshuffle_each_iteration=True
    ).repeat()\
    .map(
      map_func=get_sample,
      num_parallel_calls=4,
      deterministic=False
    ).batch(
      batch_size=12,
      drop_remainder=True
    )
    train_set = train_set.prefetch(20) 
    ```

    ``` py title="Algorithm 2: Tf.data API example when reading multiple text files" linenums="1"
    import tensorflow as tf

    train_set = tf.data.TextLineDataset(
      [
        "filel.txt",
        "file2.txt",
        ...
      ]
    )
    
    train_set = train_set.shuffle(
      buffer_size=100,
      seed=42,
      reshuffle_each_iteration=True
    ).repeat()\
    .map(
      map_func=lambda x: x + 1,
      num_parallel_calls=4,
      deterministic=False
    ).batch(
      batch_size=12,
      drop_remainder=True
    )
    
    train_set = train_set.prefetch(20) 
    ```

### Rules (partition policies; technically enforced)
- Slurm's Fairshare is used¹
- Wall-time limit (7 days for M&CS)
- Required to specify the number of cores/RAM explicitly for GPU queue
- At most 2 GPUs are allocated simultaneously to a single user
- At most 8 cores and 128GB RAM can be used on node A<br/>At most 7 cores 
and 32GB RAM can be used on node B

¹ For each researcher, usage in the last 5 minutes is computed as a fraction
of available resources. Jobs from researchers with a lower usage fraction are 
started first. This allows for a fair distribution of jobs during popular 
times.
