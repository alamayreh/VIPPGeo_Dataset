# VIPPGeo Dataset UNDER CONSTRUCTION !
&nbsp;



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/vipplogo2020-1466x236.png" alt="Logo" width="733" height="118">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>


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
