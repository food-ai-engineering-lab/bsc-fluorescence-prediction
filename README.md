# BSC Fluorescence Prediction


### Supplementary scripts:
- `contrast.py`: Preprocessing the image data to make the contrast better and the image sharper
- `dump_array.py`: Dump array into a txt view for manual inspection
- `eval.py`: Evaluation script including several different parameters like MSE, SSIM, and Pearson Correlation Coefficient
- `flip_color.py`: Using color palette chaging methods to visualize and inspect noisy images to get a better view of cells
- `jpg_to_tif.py`: Changing jpg files to tif format
- `make_csv.py`: Script to iterate raw file storage data and generate csv with file paths used by model
- `make_gs.py`: Convert multi-channel tifs into single channel grayscale tif
- `make_rgb`: Map model-generated grayscale output into a color palette for better visualization
- `overlay.py`: Overlay two images on top of each other
- `split.py`: Test/Train split
- `tif_to_jpeg.py`: Changing tif files to jpeg for easy visualization of images
- `whitescan.py`: Normalization of images using average whitescan (preprocessing)
- `images`: Directory containing relevant images of experiments

### Workflow for getting results:
- Run preprocessing on your data
    > Relevant Files: whitescan.py (Remove background noise from whitescan), flip_color.py (better visualization of images by mapping to color palettes)
- Change your images to tif
    > Relevant File: jpg_to_tif.py 
- Make a csv of all the tifs
    > Relevant File: make_csv.py
- Split into training and testing csvs
    > Relevant File: split.py
    - Local Path to input images: 
        - /mnt/projects/sinhasa3/pax_data/BF (use gray scale tifs there)
    - Local path to target images: 
        - /mnt/projects/sinhasa3/processed_pax7/ (Pax7) 
        - /mnt/projects/sinhasa3/whitescan_Pax7/graytifs/ (whitescan pax7) 
        - /mnt/projects/sinhasa3/whitescan_rev_Pax7/graytifs/ (reverse whitescan Pax7) 
        - /mnt/projects/sinhasa3/whitescan_DAPI/graytifs/ (whitecsan DAPI) 
        - /mnt/projects/sinhasa3/pax_data/DAPI (original DAPI)
    - Local path to model outputs: 
        - /mnt/projects/sinhasa3/tifs_DAPI_whitescan (whitescan DAPI) 
        - /mnt/projects/sinhasa3/tifs_DAPI (original DAPI)
- Run model training on train csv
- Run model testing on test csv
- Run evaluations on predictions
    > Relevant File: eval.py