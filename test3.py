# import the necessary packages
import argparse
import cv2

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
# refPt = []
drawing = False


def click_callback(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, drawing

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.append((x, y))
        drawing = True

    # if drawing and event == cv2.EVENT_MOUSEMOVE:
    #     image = temp_img
    #     cv2.line(image, refPt[-1], (x, y), (0, 0, 255), 2)
    #     temp_img = clone


    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        drawing = False
        # draw a line
        cv2.line(image, refPt[-1], refPt[-2], (0, 0, 255), 2)
        cv2.imshow("Room Dimension Estimator", image)


def callback(event, x, y, flags, param):
    idx_cb = param[0]
    colour = (0, 0, 0)
    if idx_cb == 0:
        colour = (255, 0, 0)
    elif idx_cb == 1:
        colour = (0, 255, 0)
    elif idx_cb == 2:
        colour = (0, 0, 255)

    # grab references to the global variables
    global refPt, drawing

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("def callback(" + str(event) + "," + str(x) + "," + str(y) + "," + str(flags) + "," + str(param) + ")")
        refPt[idx].append((x, y))
        drawing = True

    # if drawing and event == cv2.EVENT_MOUSEMOVE:
    #     image = temp_img
    #     cv2.line(image, refPt[-1], (x, y), (0, 0, 255), 2)
    #     temp_img = clone


    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        print("def callback(" + str(event) + "," + str(x) + "," + str(y) + "," + str(flags) + "," + str(param) + ")")
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt[idx].append((x, y))
        drawing = False
        # draw a line
        cv2.line(image, refPt[idx][-1], refPt[idx][-2], colour, 2)
        cv2.imshow("Room Dimension Estimator", image)

def nothing_callback(event = None, x = None, y = None, flags = None, param = None):
    pass


def nothing(x):
    pass


def calculate(point_sets):
    import utils
    lines = []

    print("Point sets:", point_sets)
    for i in range(0, len(point_sets)):
        for j in range(0, len(point_sets[i]), 2):
            lines.append((point_sets[i][j], point_sets[i][j+1]))

    line_idx = 0
    for line in lines:
        print("Line " + str(line_idx) + ": ", line)
        line_idx += 1

    utils.get_v_points(lines)


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
temp_img = image.copy()
clone = image.copy()
cv2.namedWindow("Room Dimension Estimator")
### add first list to ref points for first vanishing point
refPt.append([])
cv2.setMouseCallback("Room Dimension Estimator", callback, param=[0])

idx = 0

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("Room Dimension Estimator", image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        refPt = [[]]
        image = clone.copy()
        idx = 0
        cv2.setMouseCallback("Room Dimension Estimator", callback, param=[idx])

    elif key == ord("n"):
        idx += 1
        refPt.append([])
        cv2.setMouseCallback("Room Dimension Estimator", callback, param=[idx])

    elif key == ord("."):
        cv2.setMouseCallback("Room Dimension Estimator", nothing_callback)
        calculate(refPt)

    # if the 'c' key is pressed, break from the loop
    elif key == ord("q"):
        break


# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()
