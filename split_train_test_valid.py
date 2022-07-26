1. Get Flickr, Splash, and Mapillary csv data. 
2. run split_train_test_valid to split the dataset. then, generate_labels.py the lables in labels_json.
3. To download the sub_dataset: train,test,valid run 

# Train 
python3 download_images.py --output /data2/omran/dataset/flickr_splash_mapilry/train_dir --url_csv /data2/omran/dataset/urls/train.csv --shuffle

# Validation - check images size 
python3 download_images.py --output /data2/omran/dataset/flickr_splash_mapilry/valid_dir --url_csv /data2/omran/dataset/urls/valid.csv --shuffle --size_suffix "" 

# Test 
python3 download_test.py --output /data2/omran/dataset/flickr_splash_mapilry/test_dir --url_csv /data2/omran/dataset/urls/test.csv --shuffle --size_suffix ""

4. generate_labels.py # check the script to change for train,valid,test.

5. After that, run filter_by_downloaded_images.py. The paths are in config/flick_splash_mapillary.yml

6. To start training 

export CUDA_VISIBLE_DEVICES=1
python3 -m classification.train_cc --config config/flick_splash_mapillary.yml --progbar 