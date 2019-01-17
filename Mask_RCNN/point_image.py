#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 20:09:42 2018

@author: juliocesar
"""
import numpy as np
import os 
import argparse
import skimage.io
import matplotlib.pyplot as plt
import pickle


# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to image")
#args = vars(ap.parse_args())
def main():
    args = {}
    args['image'] = 'images/masked.jpg'
    args['measures'] = 'measures.p'
    args['real_size'] = 'real_measures.p'
    
    measures = pickle.load(open(args['measures'], 'rb') )
    real_sizes = pickle.load(open(args['real_size'], 'rb') )
    
    image = skimage.io.imread(os.path.join(args['image']) )
    image = image.astype(np.uint8)
    
    plt.imshow(image)
    plt.axis('image')
    points = plt.ginput(2)
    
    min_measure = None
    min_cat = None
    for cat, measure in measures.items():
        xrange = range(measure[0], measure[0] + measure[2])
        yrange = range(measure[1], measure[1] + measure[3])
        x1, y1 = points[0]
        x2, y2 = points[1]
    
        if int(x1) in xrange and int(y1) in yrange and int(x2) in xrange and int(y2) in yrange:
            min_measure = measure
            min_cat = cat
    
    if min_measure is None:
        print("There's no match between the selected points and a category")
    else:
        real = real_sizes[min_cat]
        
        print('\n\n{}'.format(min_cat) )
        print("-------------------------------")
        print("type\twidth\theight\tdepth")
        print('pixel\t{}\t{}\tNaN'.format(min_measure[2], min_measure[3]) )
        print('cm\t{}\t{}\t{}'.format(real[1], real[0], real[2]) )
        print("-------------------------------")


def get_measures(coords):
    args = {}
    args['image'] = 'images/masked.jpg'
    args['measures'] = 'measures.p'
    args['real_size'] = 'real_measures.p'
    
    measures = pickle.load(open(args['measures'], 'rb') )
    real_sizes = pickle.load(open(args['real_size'], 'rb') )
    
    image = skimage.io.imread(os.path.join(args['image']) )
    image = image.astype(np.uint8)
    h, w, ch = image.shape
    
    plt.imshow(image)
    plt.axis('image')
    
    for coor in coords:
        x1 = int(coor[0] )
        y1 = coor[1]
        y1 = int(h - y1)
        x2 = int(coor[2])
        y2 = coor[3]
        y2 = int(h - y2)
        
        min_measure = None
        min_cat = None
        for cat, measure in measures.items():
            xrange = range(measure[0], measure[0] + measure[2])
            yrange = range(measure[1], measure[1] + measure[3])
    
            if (int(x1) in xrange and int(y1) in yrange) or (int(x2) in xrange and int(y2) in yrange):
                min_measure = measure
                min_cat = cat
        if min_measure is None:
            print("There's no match between the selected points and a category")
        else:
            real = real_sizes[min_cat]
        
            print('\n\n{}'.format(min_cat) )
            print("-------------------------------")
            print("type\twidth\theight\tdepth")
            print('pixel\t{}\t{}\tNaN'.format(min_measure[2], min_measure[3]) )
            print('cm\t{}\t{}\t{}'.format(real[1], real[0], real[2]) )
            print("-------------------------------")
        
if __name__ == "__main__":
    main() 