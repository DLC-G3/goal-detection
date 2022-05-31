import glob
import os

path = './images/'
count = 0

for f in glob.glob(path + '*.*'):
    os.rename(f, f"{path}bal{count}.jpg") 
    count += 0