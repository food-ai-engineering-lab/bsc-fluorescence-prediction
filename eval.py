import numpy as np
import os
import re
import cv2
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
from scipy import stats


def mse(prediction, target):
    try:
        mse = 0
        flag = 0

        h, w = target.shape
        diff = cv2.subtract(target, prediction)
        err = np.sum(diff**2)
        mse = err/(float(h*w))

    except Exception as e:
        print(e)
        flag = 1

    finally:
        return mse, flag

    
def pearson(prediction, target):
    try:
        stat = 0
        flag = 0
        
        prediction = prediction.flatten()
        target = target.flatten()

        res = stats.pearsonr(target, prediction)
        stat = res.statistic

    except Exception as e:
        print(e)
        flag = 1

    finally:
        return stat, flag

def eval(path):
    en = 0
    enp = 0
    n = 0

    prediction_file = None
    target_file = None

    avg_mse = 0
    total_mse = 0

    total_ssim = 0
    avg_ssim = 0

    total_pearson = 0
    avg_pearson = 0


    for filename1 in os.listdir(path):
        if filename1.endswith('jpeg') and 'prediction' in filename1:
                prediction_file = filename1

                for filename2 in os.listdir(path):
                    if filename2.endswith('jpeg') and 'target' in filename2 and prediction_file.split('_')[0] == filename2.split('_')[0]:
                        target_file = filename2
                    
                        print('Browsing', prediction_file, target_file)

                        prediction_path = path + prediction_file
                        target_path = path + target_file

                        try:
                            prediction = cv2.imread(prediction_path)
                            target = cv2.imread(target_path)
                        except Exception as e:
                            print('Image Read Error:', prediction_file[0])
                            print(e)

                        prediction = cv2.cvtColor(prediction, cv2.COLOR_BGR2GRAY)
                        target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

                        error, flag = mse(prediction, target)
                        total_mse += error
                        if flag:
                            en += 1
                        
                        pearsonc, flag = pearson(prediction, target)
                        total_pearson += pearsonc
                        if flag:
                            enp += 1

                        total_ssim += ssim(target, prediction)
                        n += 1

    print('Total Images:', n)

    avg_mse = total_mse/n
    print('Average MSE: ', avg_mse)

    print('Missed images: ', en)

    avg_ssim = total_ssim/n
    print('Average SSIM: ', avg_ssim)

    avg_pearson = total_pearson/n
    print('Pearson Correlation Coefficient: ', avg_pearson)

    print('Missed images: ', enp)


eval('/mnt/projects/sinhasa3/tifs_DAPI/')