# PyTorch Implementation of Paper "Active Gradual Domain Adaptation: Dataset and Approach"


### How to run

Please download the EVIS_40 dataset from this repository: https://github.com/LianzheWang/EVIS

Unzip and put the EVIS dataset under the data director. It should appear like 

```
root/data/EVIS_40/..
```

In the notebook Active_Gradual_Domain_Adaptation_EVIS.ipynb , We are able to replicate our experiment results in the paper.

Specificly, the following things have been done in the notebook:

1. Introducing example torch dataset classes for EVIS dataset.
2. Showing the "gradual domain drift" inside the EVIS dataset.
3. Implementing our AGST approach in the paper and compare with other baselines on the task of gradual domain adaptation on EIVS dataset. Ablation study is included.


### Citation
If you find this work helpful in your research, please consider cite our paper through
```
@ARTICLE{Zhou2021,
author={Zhou, Shiji and Wang, Lianzhe and Zhang, Shanghang and Wang, Zhi and Zhu, Wenwu},  
journal={IEEE Transactions on Multimedia},   
title={Active Gradual Domain Adaptation: Dataset and Approach},   
year={2022},   
pages={1-1}, 
doi={10.1109/TMM.2022.3142524}
}
```
