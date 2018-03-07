# -*- coding: utf-8 -*-
import logging
import os
import sys

import cv2
import sys

if getattr( sys, 'frozen', False ) :
    # running in a bundle
    SENSOR = os.path.join(sys._MEIPASS, 'data', 'sensor_data.json')
else :
    # running live
    abspath = os.path.abspath(os.path.dirname(__file__))
    SENSOR = os.path.join(abspath,  'data', 'sensor_data.json')

logger = logging.getLogger(__name__)

# Handle different OpenCV versions
OPENCV3 = int(cv2.__version__.split('.')[0]) >= 3

if hasattr(cv2, 'flann_Index'):
    flann_Index = cv2.flann_Index
elif hasattr(cv2, 'flann') and hasattr(cv2.flann, 'Index'):
    flann_Index = cv2.flann.Index
else:
    logger.warning('Unable to find flann Index')
    flann_Index = None


# Parallel processes
def parallel_map(func, args, num_proc):
    """Run function for all arguments using multiple processes."""
    return list(map(func, args))

# Memory usage
if sys.platform == 'darwin':
    rusage_unit = 1
else:
    rusage_unit = 1024


def current_memory_usage():
    return 0
