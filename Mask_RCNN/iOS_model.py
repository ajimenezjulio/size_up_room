#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:59:15 2018

@author: juliocesar
"""

# import necessary packages
from keras.models import load_model
import coremltools
import argparse
import pickle
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
args = vars(ap.parse_args())

# load the class labels
print("[INFO] loading class labels from label binarizer")
class_labels = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']
print("[INFO] class labels: {}".format(class_labels))
 
# load the trained convolutional neural network
print("[INFO] loading model...")
model = load_model(args["model"])


# convert the model to coreml format
print("[INFO] converting model")
coreml_model = coremltools.converters.keras.convert(model,
	input_names="image",
	image_input_names="image",
	class_labels=class_labels,
	is_bgr=True)

# save the model to disk
output = args["model"].rsplit(".", 1)[0] + ".mlmodel"
print("[INFO] saving model as {}".format(output))
coreml_model.save(output)