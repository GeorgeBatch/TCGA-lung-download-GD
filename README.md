# Download TCGA-lung files and Annotations from Google Drive

**Source:** [WSI_TCGA-Lung](https://drive.google.com/drive/folders/1UobMSqJEqINX2izxrwbgprugjlTporSQ) Google Drive folder provided by [Bin Li](https://github.com/binli123) in [DSMIL: Multiple instance learning networks for tumor detection in Whole Slide Image](https://github.com/binli123/dsmil-wsi) repository.

This repository relies on the [gdown](https://github.com/wkentaro/gdown) library which can be used both from command line or from within Python scripts/notebooks.

**Important:** The library does not work for downloading folders with more than 50 files. This is why the first step is to get the links (ids) for the individual subfolders each of which has less than 50 files and iterate over them.

## 1. Create csv files with names and links

Use Google Sheets functionality to get all the names and links into a google sheet and then download as multiple csv files: https://drive.google.com/drive/folders/108x3iNiCRmJx9s-pa05xH6vKLyg_1zbh?usp=sharing

Save the csv files into `names_and_links`.

## 2. Create files to record which of the files have already been downloaded and download all files

```
cd download_scripts/

# keep a record so that if the download is interrupted,
# there is a way to resume the download  instead of
# starting from scratch
python create_record_files.py

# IDs and annotations
python download_ids.py

# corrupt files and annotations
python download_corrupt_WSIs.py

# good files and annotations
python download_good_WSIs.py
```

## Potential problems

Google Drive might stop giving access to files when many files from the same Google Drive folder are requested using code (my idea of why it happens). This **will not** result in the script execution interrupting, but instead give warnings, which I was not able to catch with `try`-`except` construct in Python. This may result in folders with missing files being downloaded.

```
Access denied with the following error:

 	Too many users have viewed or downloaded this file recently. Please
	try accessing the file again later. If the file you are trying to
	access is particularly large or is shared with many people, it may
	take up to 24 hours to be able to view or download the file. If you
	still can't access a file after 24 hours, contact your domain
	administrator.

You may still be able to access the file from the browser:
%%%URLHERE
```

This is an [open issue](https://github.com/wkentaro/gdown/issues/43) with the [gdown](https://github.com/wkentaro/gdown) library. The problem seems to be on Google's side.


## TODO:

1. Catch warnings and interrupt execution or at least not update the download status in the record files so that the download is not marked complete.
