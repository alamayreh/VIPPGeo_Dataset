# VIPPGeo Dataset UNDER CONSTRUCTION !

This is the official repository for the paper : 

[Which country is this picture from? New data and methods for DNN-based country recognition](https://arxiv.org/pdf/2209.02429.pdf) 


### Download the dataset urls from [google drive](https://drive.google.com/drive/folders/1CXVdpfFpolQah4PsfGXrhgoWtOtFEC__?usp=sharing)

### Or 
### By using gdown

```
pip install gdown
gdown https://drive.google.com/drive/folders/1CXVdpfFpolQah4PsfGXrhgoWtOtFEC__ --folder
```

Download the dataset, using the follwoing scripts. To download the datast in msg fromt (to save space), please specify ``` --msg ```
&nbsp;
### Train 
    python3 download_images.py --output dir_out/train --url_csv GeoDataset_Urls/train.csv 

### Validation
    python3 download_images.py --output dir_out/validation --url_csv GeoDataset_Urls/valid.csv  
### Test 
    python3 download_images.py --output dir_out/test --url_csv GeoDataset_Urls/test.csv 

# Citation

If you use this code for your research, please cite our paper.

```
@article{alamayreh2022country,
  title={Which country is this picture from? New data and methods for DNN-based country recognition},
  author={Alamayreh, Omran and Dimitri, Giovanna Maria and Wang, Jun and Tondi, Benedetta and Barni, Mauro},
  journal={arXiv preprint arXiv:2209.02429},
  year={2022}
}

```

# Acknowledgement 

This code heavily depends on the code provided by 

[Geolocation Estimation of Photos using a Hierarchical Model and Scene Classification](https://github.com/TIBHannover/GeoEstimation) 
