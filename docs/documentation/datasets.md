---
hide: [toc]
title: Datasets
---
# Datasets

!!! tip "No need to download common datasets yourselves!"

    On the Umbrella Cluster, we maintain a list of datasets frequently used to either train or benchmark a model, usually in the context of machine learning. Instead of occupying space on your own space or waiting for the download of the data to finish to your own space, freely use the available datasets at the dataset folder on Umbrella Cluster.

## List of available datasets

<table>
  <tr>
    <th>Name</th>
    <th>Versions</th>
    <th>Free access</th>
    <th>Path</th>
    <th>License</th>
    <th>References</th>
  </tr>
  <tr>
    <td>ADE20K</td>
    <td>2021-17-01</td>
    <td>&check;</td>
    <td><code>/dataset/ADE20K</code></td>
    <td><a href="https://groups.csail.mit.edu/vision/datasets/ADE20K/terms/">ADE20K license</a></td>
    <td><a href="https://groups.csail.mit.edu/vision/datasets/ADE20K/">Website</a><br/></td>
  </tr>
  <tr>
    <td colspan="6">
      <p>Note: the ADE20K dataset must be unzipped before use. E.g.:</p>
      <pre>
datadir=$TMPDIR/ade20k  # &lt;-- use this in jobs (and Open OnDemand interactive; and through salloc, srun)
datadir=/scratch-shared/$USER/ade20k  # &lt;-- use this in interactive sessions
mkdir $datadir
unzip /dataset/ADE20K/ADE20K.zip -d $datadir
      </pre>
    </td>
  </tr>
  <tr>
    <td>AlphaFold</td>
    <td>2.3.1</td>
    <td>&check;</td>
    <td>
      <code>/dataset/AlphaFold</code><br/>
      Related module: <code>module load AlphaFold/2.3.1-foss-2022a</code>
    </td>
    <td>
      Model params: <a href="https://creativecommons.org/licenses/by/4.0/legalcode">CC BY 4.0</a><br/>
      Mirrored DBs: various; see website
    </td>
    <td><a href="https://github.com/google-deepmind/alphafold">GitHub</a></td>
  </tr>
  <tr>
    <td colspan="6">
      Note: AlphaFold has a related module: <code>module load AlphaFold/2.3.1-foss-2022a</code>
    </td>
  </tr>
  <tr>
    <td>CAMELYON16</td>
    <td>&mdash;</td>
    <td>&check;</td>
    <td><code>/dataset/CAMELYON16</code></td>
    <td><a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a></td>
    <td><a href="https://camelyon16.grand-challenge.org/">Website</a></td>
  </tr>
  <tr>
    <td>CIFAR-10</td>
    <td>&mdash;</td>
    <td>&check;</td>
    <td><code>/dataset/CIFAR-10</code></td>
    <td>See website</td>
    <td><a href="https://www.cs.toronto.edu/~kriz/cifar.html">Website</a></td>
  </tr>
  <tr>
    <td>MNIST</td>
    <td>&mdash;</td>
    <td>&check;</td>
    <td><code>/dataset/MNIST</code></td>
    <td><a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a></td>
    <td><a href="https://yann.lecun.com/exdb/mnist/">Website</a></td>
  </tr>
<tr>
    <td>ImageNet</td>
    <td>&mdash;</td>
    <td>&mdash;</td>
    <td><code>/dataset/ImagNet</code></td>
    <td><a href="https://www.image-net.org/download">Terms and Conditions</a></td>
    <td><a href="https://www.image-net.org/">Website</a></td>
  </tr>
</table>

## Dataset or model not listed?

If the dataset or model is missing, it can be downloaded or uploaded to Umbrella Cluster. Please contact us if you think other people would also use this model or dataset, we can then add a copy of this to the public model and dataset space. This way, we alleviate having many duplicates of models or datasets on the system and users needing to download or uploaded from external sources. Of course, if your dataset or model is proprietary or privacy-sensitive, this does not apply.

## Getting access to restricted datasets and models

Some datasets and models are not accessible by default on the Umbrella Cluster, because they require explicit acceptance of a license or agreeing to a terms of use on the website of the dataset or model provider.

If you would like to access these datasets or models on the Umbrella Cluster, please contact the system administrators with a screenshot of the dataset or model provider giving you access to the data.

Even if access to a datasets is not restricted, it usually still has a license and a terms of conduct.  By using the dataset or model you are agreeing to both the license and the terms of conduct.
