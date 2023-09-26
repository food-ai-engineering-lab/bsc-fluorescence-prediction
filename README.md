# BSC Fluorescence Prediction


Supplementary scripts:
- `contrast.py`: Preprocessing the image data to make the contrast better and the image sharper
- `eval.py`: Evaluation script including several different parameters like MSE, SSIM, and Pearson Correlation Coefficient
- `jpg_to_tif.py`: Changing jpg files to tif format
- `make_csv.py`: Script to iterate raw file storage data and generate csv with file paths used by model
- `make_gs.py`: Convert multi-channel tifs into single channel grayscale tif
- `make_rgb`: Map model-generated grayscale output into a color palette for better visualization
- `split.py`: Test/Train split
- `tif_to_jpeg.py`: Changing tif files to jpeg for easy visualization of images