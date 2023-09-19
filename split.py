import pandas as pd
import os
import re
import math
from sklearn.model_selection import train_test_split

df = pd.read_csv('path_Pax7.csv')
sample = 144
n_train = int (0.8 * sample)
n_test = sample - n_train

train, test = train_test_split(df, test_size=0.2)

train.to_csv('train_pax7.csv', index=None)
test.to_csv('test_pax7.csv', index=None)