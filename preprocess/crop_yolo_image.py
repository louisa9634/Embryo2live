from __future__ import print_function

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

import cv2
import os



crop = pd.read_csv("/mnt/louisayu/nfs_share2/embryo/code/final/preprocess/Detection_Results_all.csv")  
image_path= '/mnt/louisayu/nfs_share2/embryo/rawdata/'
yolo_image_path= '/mnt/louisayu/nfs_share2/embryo/Test_Image_Detection_Results/'
save_path= '/mnt/louisayu/nfs_share2/embryo/after_yolocrop_all_1018/'


def adjust_num(x):
    if not x%8==0:
        x=x-x%8
    else:
        x=x
    return x


def yolo_crop43ratio(i):  
    im=cv2.imread(image_path+crop['image'][i])

    imagename = crop['image'][i]
    xmin=crop['xmin'][i]
    xmax=crop['xmax'][i]
    ymin=crop['ymin'][i]
    ymax=crop['ymax'][i]
    xsize=crop['x_size'][i]
    ysize=crop['y_size'][i]
    w=adjust_num(xmax-xmin)
    h=adjust_num(ymax-ymin)
    center_x=(xmax+xmin)//2 
    center_y=(ymax+ymin)//2
    largersize=max(w,h)
    if w<h:
        if center_x+(3/8)*largersize>xsize:
            largersize=largersize-xsize+center_x+(3/8)*largersize
        img=im[ymin:(ymin+largersize),int(center_x-(3/8)*largersize):int(center_x+(3/8)*largersize)]
        assert 3*img.shape[0]==4*img.shape[1], [imagename, 3*img.shape[0],4*img.shape[1],center_x-(3/8)*largersize,center_x+(3/8)*largersize]

    elif w>h:
        if (3*w/4)>ysize:
            largersize=h
            img=im[int(center_y-(3/8)*largersize):int(center_y+(3/8)*largersize),int(center_x-1/2*largersize):int(center_x+1/2*largersize)]
        else:
            img=im[int(center_y-(3/8)*largersize):int(center_y+(3/8)*largersize),xmin:xmin+largersize]
        assert 3*img.shape[1]==4*img.shape[0], [imagename, img.shape[0],img.shape[1]]

    elif w==h:
        img=im[int(center_y-(3/8)*largersize):int(center_y+(3/8)*largersize),xmin:xmin+largersize]
        img1=im[ymin:ymin+largersize,int(center_x-(3/8)*largersize):int(center_x+(3/8)*largersize)]
        assert 3*img.shape[1]==4*img.shape[0], [imagename, img.shape[0],img.shape[1]]
        
    return img


for i in tqdm(range(crop.shape[0])):
    filename=image_path+crop['image'][i]
    if os.path.exists(filename):
        try:
            img_yolo=yolo_crop43ratio(i)
            cv2.imwrite(save_path+crop['image'][i],img_yolo)  
        except:
            print(filename,"error")  
    else:
        print(filename,"file not exists")   
