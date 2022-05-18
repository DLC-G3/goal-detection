import cv2
vidcap = cv2.VideoCapture('./SourceFiles/doelpunten_cam_4.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./SourceFiles/Images/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1