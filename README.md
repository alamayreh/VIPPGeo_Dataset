# VIPPGeo Dataset UNDER CONSTRUCTION !
&nbsp;

This is the official repository for the paper : 
Which country is this picture from? New data and methods for DNN-based country recognition https://arxiv.org/pdf/2209.02429.pdf 

## 1. Get Flickr, Splash, and Mapillary csv data. 

## First download the dataset urls from google drive  [google drive](https://drive.google.com/drive/folders/1CXVdpfFpolQah4PsfGXrhgoWtOtFEC__?usp=sharing)

&nbsp;

## 2. Spliting the dataset.

### Run the following commands to split the dataset into train, validation, and test sets.
    python3 split_train_test_valid.py

&nbsp;
## 3. Download the dataset.
&nbsp;
### Train 
    python3 download_images.py --output out_dir --url_csv train.csv --shuffle
&nbsp;
### Validation
    python3 download_images.py --output out_dir --url_csv valid.csv --shuffle --size_suffix "" 
&nbsp;
### Test 
    python3 download_test.py --output out_dir --url_csv test.csv --shuffle --size_suffix ""
