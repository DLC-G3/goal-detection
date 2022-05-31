import cv2
import random
import pathlib 
import os


def get_all_frames():
  vidcap = cv2.VideoCapture('./SourceFiles/videoclip_963155.mp4')
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite("./SourceFiles/Images/interessant/1frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

def get_random_frames(start_video=96,interval=24,random_offset=6):
  vidcap = cv2.VideoCapture('./SourceFiles/cam6_footage.mp4')
  success,image = vidcap.read()
  count = 0
  randomv = random.randint(interval-random_offset,interval+random_offset)
  print("starting image creation")
  print(success)
  
  while success and count < start_video:
    success,image = vidcap.read()
    count += 1

  count = 0
  while success:
    if count%randomv == 0:
      print(f"added image {count}")
      cv2.imwrite(f"./SourceFiles/Images/variated/randomframe{count}.jpg", image)     # save frame as JPEG file
      randomv = random.randint(count + interval-random_offset,count + interval+random_offset)     
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

def get_cropped_images(cam=6,cropped_under_line=True):
  vector = [{4:{"x":220,"y":680,"w":1700,"h":1080},6:{"x":380,"y":632,"w":1600,"h":1080}},{4:{"x":380,"y":908,"w":1600,"h":1080},6:{"x":420,"y":908,"w":1500,"h":1080}}][cropped_under_line][cam]
  temp_files = os.listdir("./SourceFiles/Images")
  files = []
  for file in temp_files:
    if file[-4:] == ".jpg":
      files.append(file)
      image = cv2.imread(f"./SourceFiles/Images/{file}")
      cropped_image = image[vector["y"]:vector["h"],vector["x"]:vector["w"]]
      # cv2.imshow("Cropped", cropped_image)
      # cv2.waitKey(0)
      cv2.imwrite(f"./SourceFiles/Images/cropped/{file}", cropped_image)     # save frame as JPEG file
  #image = cv2.imread(r"C:\Users\HP\OneDrive\Desktop\<image>.png")

get_cropped_images()