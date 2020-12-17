from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v1 as tf
from imutils.video import VideoStream


import argparse
import facenet
import imutils
import os
import sys
import math
import pickle
import align.detect_face
import numpy as np
import cv2
import collections
from sklearn.svm import SVC
import requests
import asyncio
import time
import RPi.GPIO as GPIO
relay = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay,GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
is_open_door = False
is_open_lock = False
is_first_time = True
GPIO.output(relay,0)
start_time = 0
def check_door():
    print('bat dau check door')
    global is_first_time
    global is_open_door
    #dang dong tra False ,mo thi tra True
    if GPIO.input(15) == False:        
        is_open_door = False
        print('check_door, is_open_door: {}'.format(is_open_door))
        print('check_door, is_first_time: {}'.format(is_first_time))
        if is_first_time:
            is_first_time = False
            print('check_door, is_first_time: {}'.format(is_first_time))
    else:
        is_open_door = True
        print('check_door, is_open_door: {}'.format(is_open_door))
    print('end check door')
check_door()
print('is_first_time: {}'.format(is_first_time))
print('is_open_door: {}'.format(is_open_door))