import numpy as np
import pandas as pd
import cv2
from matplotlib import pyplot as plt
from shutil import copy2
import os
import fnmatch
import glob


inputcsv = pd.read_csv("C:/Users/Jonathan/Desktop/Software Stuff/Python 3.6 Stuff/Filemove/inputcsv.csv")
#C:\Users\Jonathan\Desktop\Software Stuff\Python 3.6 Stuff\Filemove

inputarray = inputcsv.values
inputarray
#inputcsv
dst = "C:/Users/Jonathan/Desktop/Software Stuff/Python 3.6 Stuff/Filemove/result"

# src1 = "C:/Users/Jonathan/Desktop/Software Stuff/Python 3.6 Stuff/Filemove/"
# src2 = "5021"
# #src3 = "/"
# src4 = glob.glob(src1+src2+src3+'*Capture123.JPG')



for x in range(0,inputarray.size):
    src1 = "C:/Users/Jonathan/Desktop/Software Stuff/Python 3.6 Stuff/Filemove/"
    src2 = str(inputarray[x][0])
    src3 = "/"
    src4 = glob.glob(src1+src2+src3+'*Capture123.JPG')
    #src = src1 + src2 + src3 + src4
    copy2(src4[0], dst)

    
