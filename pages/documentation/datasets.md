---
hide: [toc]
title: Datasets
---
# Datasets

!!! tip "No need to download common datasets yourselves!"

    On the Umbrella Cluster, we maintain a list of datasets frequently used to either train or benchmark a model, usually in the context of machine learning. Instead of occupying space on your own space or waiting for the download of the data to finish to your own space, freely use the available datasets at the dataset folder on Umbrella Cluster.
    
    Importantly, the root of most datasets folders is `/home/tue/shared_data`.
    
    For the data storage and conversion we use Python as a framework.
    
    License: CC BY-NC-SA 3.0 (https://creativecommons.org/licenses/by-nc-sa/3.0/)
    
    This means that you must attribute the work in the manner specified by the authors, you may not use this work for commercial purposes and if you alter, transform, or build upon this work, you may distribute the resulting work only under the same license.

## Dataset or model not listed?

If the dataset or model is missing, it can be downloaded or uploaded to Umbrella Cluster. Please contact us if you think other people would also use this model or dataset, we can then add a copy of this to the public model and dataset space. This way, we alleviate having many duplicates of models or datasets on the system and users needing to download or uploaded from external sources. Of course, if your dataset or model is proprietary or privacy-sensitive, this does not apply.

## Getting access to restricted datasets and models

Some datasets and models are not accessible by default on the Umbrella Cluster, because they require explicit acceptance of a license or agreeing to a terms of use on the website of the dataset or model provider.

If you would like to access these datasets or models on the Umbrella Cluster, please contact the system administrators with a screenshot of the dataset or model provider giving you access to the data.

Even if access to a datasets is not restricted, it usually still has a license and a terms of conduct.  By using the dataset or model you are agreeing to both the license and the terms of conduct.

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
    <td>AlphaFold</td>
    <td>2.3.1</td>
    <td>&check;</td>
    <td>
      <code>/dataset/AlphaFold</code>
      <br/>
      Related module: <code>module load AlphaFold/2.3.1-foss-2022a</code>
    </td>
    <td>Apache 2.0</td>
    <td><a href="https://github.com/google-deepmind/alphafold">@GitHub</a></td>
  </tr>
</table>
