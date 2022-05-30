import cv2
import random 


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

get_random_frames()