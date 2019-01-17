import cv2
import numpy
import tensorflow
import math
from numpy import linalg as LA


def alpha_z_eq(b, t, l, v):
    return -(numpy.cross(b, t) / (numpy.dot(l, b) * (numpy.cross(v, t))))


def alpha_eq(b, t, l, v, z):
    return -(numpy.abs(numpy.cross(b, t)) / (z * numpy.dot(l, b) * numpy.abs((numpy.cross(v, t)))))

def alpha_eq2(b, t, l, v, z):
    return -(LA.norm(numpy.cross(b, t)) / (z * numpy.dot(l, b) * LA.norm((numpy.cross(v, t)))))


def z_eq(b, t, l, v, a):
    return -(numpy.abs(numpy.cross(b, t)) / (a * numpy.dot(l, b) * numpy.abs((numpy.cross(v, t)))))

def z_eq2(b, t, l, v, a):
    return -(LA.norm(numpy.cross(b, t)) / (a * numpy.dot(l, b) * LA.norm((numpy.cross(v, t)))))

# Get the euclidean distance between two points.
def distance2d(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


def distance2d_numpy(p0, p1):
    return numpy.linalg.norm(p0 - p1)


def get_z_ratio(p0, p1, c, v):
    eq = (distance2d(p1, c) * distance2d(p0, v))/(distance2d(p0, c) * distance2d(p1, v))
    return 1 - eq


def get_Z_from_ref(zr, p0, p1, c, v):
    ratio = get_z_ratio(p0, p1, c, v)
    inverse = math.pow(ratio, -1)
    return inverse * zr


def get_funky_h(I, mu, v, l):
    ratio = (v * numpy.transpose(l))/numpy.dot(v, l)
    return I + mu(ratio)


def resize(img, ratio=0.5):
    return cv2.resize(img, (0, 0), fx=ratio, fy=ratio)


# Units in mm and pixels
def object_distance(obj_height, img_height_px, obj_px, focal_length=None, sensor_height=None, device='iphone_6s'):
    if device == 'iphone_6s':
        focal_length = 4.15
        sensor_height = 3.6
    else:
        focal_length = focal_length
        sensor_height = sensor_height

    return (focal_length * obj_height * img_height_px) / (obj_px * sensor_height)