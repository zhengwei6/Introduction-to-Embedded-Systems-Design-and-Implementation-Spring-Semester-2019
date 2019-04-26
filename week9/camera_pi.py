#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 05/31/2015
# Origin : http://blog.miguelgrinberg.com/post/video-streaming-with-flask

import cv2
import sys
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
class Camera(object):
    def __init__(self):
        if cv2.__version__.startswith('2'):
            PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
            self.HAAR_FLAGS = cv2.cv.CV_HAAR_SCALE_IMAGE
        elif cv2.__version__.startswith('3'):
            PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
            PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
            self.HAAR_FLAGS = cv2.CV_FEATURE_PARAMS_HAAR

        self.cap = cv2.VideoCapture(0)
                
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, frame = self.cap.read()
        #ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=self.HAAR_FLAGS
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.imshow("preview", frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tostring()
