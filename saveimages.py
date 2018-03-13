import cv2
import os

folder = "trainingset/"

print(cv2.__version__)
vidcap = cv2.VideoCapture('YDXJ0993.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite(str(folder) + "frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ' + str(success))
  count += 1