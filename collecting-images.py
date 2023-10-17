import cv2
import os
import time
import uuid
import subprocess

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'
labels = ['hello', 'thanks', 'yes', 'no', 'i love you']
number_imgs = 15

for label in labels:
    directory = os.path.join(IMAGES_PATH, label)
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist

    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgName = os.path.join(directory, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgName, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cap.release()
