# -*- coding: utf-8 -*-
import os
import cv2
import sys

if getattr( sys, 'frozen', False ) :
    # running in a bundle
    SENSOR = os.path.join(sys._MEIPASS, 'data', 'sensor_data.json')
else :
    # running live
    abspath = os.path.abspath(os.path.dirname(__file__))
    SENSOR = os.path.join(abspath,  'data', 'sensor_data.json')

OPENCV3 = int(cv2.__version__.split('.')[0]) >= 3
