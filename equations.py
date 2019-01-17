import numpy
import cv2

def alpha_z_eq(b, t, l, v):
    return -(numpy.cross(b, t)/(numpy.dot(l, b)*(numpy.cross(v, t))))


def alpha_eq(b,t,l,v,z):
    return -(numpy.cross(b, t)/(z*numpy.dot(l, b)*(numpy.cross(v, t))))


def z_eq(b,t,l,v,a):
    return -(numpy.cross(b, t) / (a * numpy.dot(l, b) * (numpy.cross(v, t))))

def resize(img, ratio = 0.5):
    return cv2.resize(img, (0,0), fx = ratio, fy = ratio)

# Units in mm and pixels
def object_distance(obj_height, img_height_px, obj_px, focal_length = None, sensor_height = None, device = 'iphone_6s'):
    
    if device == 'iphone_6s':
        focal_length = 4.15
        sensor_height = 3.6
    else:
        focal_length = focal_length
        sensor_height = sensor_height
        
    return (focal_length * obj_height * img_height_px ) / (obj_px * sensor_height)
    
