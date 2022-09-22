# VIPPGeo Dataset UNDER CONSTRUCTION !

This is the official repository for the paper : 

[Which country is this picture from? New data and methods for DNN-based country recognition](https://arxiv.org/pdf/2209.02429.pdf) 


### Download the dataset urls from [google drive](https://drive.google.com/drive/folders/1CXVdpfFpolQah4PsfGXrhgoWtOtFEC__?usp=sharing)

### Or 
### By using gdown

```
pip install gdown
gdown https://drive.google.com/drive/folders/1CXVdpfFpolQah4PsfGXrhgoWtOtFEC__ -O --folder
```

Download the dataset, using the follwoing scripts. To download the datast in msg fromt (to save space), please specify ``` --msg ```
&nbsp;
### Train 
    python3 download_images.py --output out_dir --url_csv train.csv --shuffle

### Validation
    python3 download_images.py --output out_dir --url_csv valid.csv --shuffle 
### Test 
    python3 download_test.py --output out_dir --url_csv test.csv --shuffle 
