import cv2
from cv2 import bilateralFilter
import numpy as np1
import glob
import os
import time


from concurrent.futures import ThreadPoolExecutor
from threading import Thread, current_thread
from multiprocessing import Pool, Queue, Manager, Value
from itertools import repeat

from sympy import arg

path = "./SourceFiles/Images/interessant/cam_4/"


def lt_5_digits(digit):
    str_digit = str(digit)
    amount_zeros = 5 - len(str_digit)
    zero_str = ""

    for i in range(amount_zeros):
        zero_str += "0"

    return f"{zero_str}{digit}"


class ImageIterator():
    def __init__(self):

        self.path = path
        self.destination_path = "./SourceFiles/Images/ii_cam4/"

        self.kernel = np1.ones((5,5), np1.uint8)
        self.count = 0

    def files_to_queue(self, fileObj):

        file = fileObj[0].replace("\\", "/")
        count = fileObj[1]

        self.files_queue_to_image(cv2.imread(file), count, fileObj[2])



    def files_queue_to_image(self, img, count, total):
        img = cv2.resize(img, (1280,720))
        # Convert to graycsale
        img_blur = cv2.GaussianBlur(img, (3,3), 3)


        img1_erosion1 = cv2.erode(img_blur, self.kernel, iterations=1)

        # edges = cv2.Canny(image=img_blur_gray, threshold1=100, threshold2=400) 

        default = {
            'name': f"{lt_5_digits(count)}_default",
            'img': img
        }        
        
        gray = {
            'name': f"{lt_5_digits(count)}_gray",
            'img': cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        }

        dilation = {
            'name': f"{lt_5_digits(count)}_dilation",
            'img': cv2.dilate(img1_erosion1, self.kernel, iterations=1)
        }

        # bilateral = {
        #     'name': f"{lt_5_digits(count)}_bilateral",
        #     'img': cv2.bilateralFilter(img1_erosion1, d=10, sigmaColor=80, sigmaSpace=80)
        # }


        image_list = [default, gray, dilation]

        for image in image_list:
            cv2.imwrite(f"{self.destination_path}{image['name']}.jpg", image['img'])



def create_files_list(files):
    filesObj = [(file , files.index(file), len(files)) for file in files]
    return filesObj


if __name__ == '__main__':
    ii = ImageIterator()
    
    start_time = time.time()
    filesObj = create_files_list( glob.glob(path + '*.*'))
    print(f"Time: {time.time() - start_time} s")
    with Pool(10) as p:
        p.map(ii.files_to_queue, filesObj)