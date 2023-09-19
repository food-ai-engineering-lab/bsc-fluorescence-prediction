import os
import re
import pandas as pd

print(os.listdir('./processed_pax7'))
bf = []
pax7 = []

for filename in os.listdir('./pax_data/BF'):
    if filename.endswith('.tif') and 'gray' in filename:
        filename = '/mnt/projects/sinhasa3/pax_data/BF/' + filename
        bf.append(filename)

for filename in os.listdir('./processed_pax7'):
    if filename.endswith('.tif'):
        filename = '/mnt/projects/sinhasa3/processed_pax7/' + filename
        pax7.append(filename)

print(len(pax7))
print(len(bf))

pax7.sort()
bf.sort()

data = {
    'some_signal_col': bf,
    'some_target_col': pax7
}

df = pd.DataFrame(data)
df.to_csv('path_Pax7.csv')