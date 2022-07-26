# VIPPGeo_Dataset

# 1. Get Flickr, Splash, and Mapillary csv data. 

## First download the dataset urls from google drive  [google drive](https://drive.google.com/drive/folders/1CXVdpfFpolQah4PsfGXrhgoWtOtFEC__?usp=sharing)

# 2. Spliting the dataset.

### Run the following commands to split the dataset into train, validation, and test sets.
    python3 split_train_test_valid.py

# 3. Download the dataset.


### Train 
    python3 download_images.py --output out_dir --url_csv train.csv --shuffle

### Validation - check images size 
    python3 download_images.py --output out_dir --url_csv valid.csv --shuffle --size_suffix "" 

### Test 
    python3 download_test.py --output out_dir --url_csv test.csv --shuffle --size_suffix ""
