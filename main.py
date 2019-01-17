import os
import cv2
import sys
import main_util
import matplotlib.pyplot as plt
import numpy as np

# [0] : base
# [1] : top
# [2] : height
ref_objs = []
unknown_obj = None
iter_ = 0
drawing = False
c_line = None
cid1, cid2, cid3 = None, None, None

mouse_counter = 0


def plot_init(plt, image):
    args = [plt, image]
    plt.imshow(image[::-1,:,:])
    fig = plt.gcf()
    fig.gca().invert_yaxis()

    global cid1, cid2, cid3

    cid1 = fig.canvas.mpl_connect('button_release_event', lambda event: key_press(event, args))
    cid2 = fig.canvas.mpl_connect('button_press_event', lambda event: mouse_ldown(event, args))
    cid3 = fig.canvas.mpl_connect('motion_notify_event', lambda event: mouse_motion(event, args))
    plt.show()


def get_ref_height(line):
<<<<<<< HEAD:main.py
    return 106
=======
    return 220
>>>>>>> 9b21af1aed2ebdbc16af36ad41ad4b49bcb566fc:abso_test.py


def mouse_motion(event, args):
    global c_line, drawing
    plt = args[0]

    try:
        x = event.xdata
        y = event.ydata

        if drawing:
            c_line.set_xdata([c_line.get_xdata()[0], x])
            c_line.set_ydata([c_line.get_ydata()[0], y])
            plt.draw()

    except TypeError as e:
        msg = "TypeError"
        if event.xdata is None:
            msg += "\n   event.xdata " + str(e)

        if event.ydata is None:
            msg += "\n   event.ydata " + str(e)

        print(msg)


def key_press(event, args):
    sys.stdout.flush()
    #key = event.key

    global iter_
    global mouse_counter

    mouse_counter = mouse_counter + 1
    plt = args[0]
    image = args[1]

    # if key == "r":
    #     # reset whole thing
    #     print("\"" + str(event.key).upper() + "\" was pressed. Process for this image has been reset.")
    #     print("")
    #     plt.close()
    #     plot_init(plt, image)
    #     iter_ = 0
    #key == "n":
    # for moving on to the next stage
    if mouse_counter == 2:
        global ref_objs, unknown_obj
        print("Reference objects:", str(ref_objs))
        print("Unknown object:", str(unknown_obj))
        print("\"" + str(event.key).upper() + "\" was pressed. Moving onr to the next stage.")
        if iter_ < 1:
            iter_ += 1
        else:
            plt.gcf().canvas.mpl_disconnect(cid2)
            plt.gcf().canvas.mpl_disconnect(cid3)
            global vanishing_line, vanishing_point
            compute(ref_objs, unknown_obj, vanishing_point, vanishing_line)
        mouse_counter = 0


def compute(refs, unknown, vp, vl):
    import eqs as eq
    vl_ = vl[0][0] - vl[1][0], vl[0][1] - vl[1][1]
    # vl_ = np.cross(np.array(vl[0]), np.array(vl[1]))
    # if vl[0][0]>vl[1][0]:
    #     vl_ = np.cross(np.array(vl[0]), np.array(vl[1]))
    # else:
    #     vl_ = np.cross(np.array(vl[1]), np.array(vl[0]))

    # get_alpha(refs, unknown, vp, vl)
    print("VL:", vl)
    print("VL_:", vl_)
    alpha_vals = []

    for ref in refs:
        # get base, top and height coordinates of known object
        if ref[0][1] < ref[1][1]:
            base = ref[0]
            top = ref[1]
        else:
            base = ref[1]
            top = ref[0]
        height = ref[2]
<<<<<<< HEAD:main.py
        alpha_vals.append(eq.alpha_eq(np.array(base), np.array(top), vl_/np.linalg.norm(vl_), np.array(vp), height))
=======
        alpha_vals.append(eq.alpha_eq2(np.array(base), np.array(top), vl_, np.array(vp), height))
>>>>>>> 9b21af1aed2ebdbc16af36ad41ad4b49bcb566fc:abso_test.py

    print("Alpha vals:", alpha_vals)
    avg_alpha_val = sum(alpha_vals) / float(len(alpha_vals))
    print("Average alpha val:", avg_alpha_val)

    if unknown[0][1] < unknown[1][1]:
        base = unknown[0]
        top = unknown[1]
    else:
        base = unknown[1]
        top = unknown[0]
    # (b, t, l, v, a)
<<<<<<< HEAD:main.py
    estimated_height = eq.z_eq(np.array(base), np.array(top), vl_/np.linalg.norm(vl_), np.array(vp), avg_alpha_val)
=======
    estimated_height = eq.z_eq2(np.array(base), np.array(top), vl_, np.array(vp), avg_alpha_val)
>>>>>>> 9b21af1aed2ebdbc16af36ad41ad4b49bcb566fc:abso_test.py
    print("Estimated height:", estimated_height)


def mouse_ldown(event, args):

    global drawing, c_line, ref_objs, unknown_obj, iter_

    plt = args[0]
    image = args[1]

    try:
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))

        x = event.xdata
        y = event.ydata

        if drawing:
            print("End drawing")
            drawing = not drawing
            c_line.set_xdata([c_line.get_xdata()[0], x])
            c_line.set_ydata([c_line.get_ydata()[0], y])
            # c_line = plt.plot([c_line.get_xdata()[0], x], [c_line.get_ydata()[0], y], 'c-')[0]
            plt.draw()

            if iter_ == 0:
                xs = c_line.get_xdata()
                ys = c_line.get_ydata()

                if ys[0] < ys[1]:
                    points = [(xs[0], ys[0]), (xs[1], ys[1])]
                else:
                    points = [(xs[1], ys[1]), (xs[0], ys[0])]

                points.append(get_ref_height(c_line))
                ref_objs.append(points)
            else:
                xs = c_line.get_xdata()
                ys = c_line.get_ydata()

                if ys[0] < ys[1]:
                    points = [(xs[0], ys[0]), (xs[1], ys[1])]
                else:
                    points = [(xs[1], ys[1]), (xs[0], ys[0])]

                unknown_obj = points
        else:
            print("Start drawing")
            drawing = not drawing
            c_line = plt.plot([x, x], [y, y], get_colour())[0]
            plt.draw()

    except TypeError as e:
        msg = "TypeError"
        if event.xdata is None:
            msg += "\n   event.xdata " + str(e)

        if event.ydata is None:
            msg += "\n   event.ydata " + str(e)

        print(msg)
        print("Event.x:", event.x)


def get_colour():
    if iter_ == 0:
        return 'c-'
    else:
        return 'r-'


def get_vp_and_vl(vp_list):
    x = 0
    y = 1

    cur_max = 0
    vp_ = None

    d1 = abs(vp_list[0][y] - vp_list[1][y])
    d2 = abs(vp_list[1][y] - vp_list[2][y])
    d3 = abs(vp_list[2][y] - vp_list[0][y])

    if d1 > d2 and d3 > d2:
        vp_ = vp_list[0]
    elif d2 > d1 and d3 > d1:
        vp_ = vp_list[2]
    else:
        vp_ = vp_list[1]

    for v in vp_list:
        print("Current Y val:", v[y])

    vl = [(v[x], v[y]) for v in vp_list if v is not vp_]

    return (vp_[x], vp_[y]), vl


for subdir, dirs, files in os.walk('./imgs'):
    for file in files[6:7]:
        filepath = subdir + os.sep + file
        if filepath.endswith(".jpg"):
            print(filepath)
            image = cv2.imread(filepath)

            edgelets1 = main_util.compute_edges(image)
            # vis_edgelets(image, edgelets1)
            vp1 = main_util.ransac_vanishing_point(edgelets1, num_ransac_iter=5000,
                                                   threshold_inlier=5)
            vp1 = main_util.reestimate_model(vp1, edgelets1, threshold_reestimate=5)
            main_util.vis_model(image, vp1)

            edgelets2 = main_util.remove_inliers(vp1, edgelets1, 10)
            vp2 = main_util.ransac_vanishing_point(edgelets2, num_ransac_iter=5000,
                                                   threshold_inlier=5)
            vp2 = main_util.reestimate_model(vp2, edgelets2, threshold_reestimate=5)

            # vis_model(image, vp2)

            # vis_model(image, vp2)
            edgelets3 = main_util.remove_inliers(vp2, edgelets2, 10)
            vp3 = main_util.ransac_vanishing_point(edgelets3, num_ransac_iter=5000,
                                                   threshold_inlier=5)
            vp3 = main_util.reestimate_model(vp3, edgelets3, threshold_reestimate=5)

            vp, vl = get_vp_and_vl([vp1, vp2, vp3])

            global vanishing_point, vanishing_line
            vanishing_point = vp
            vanishing_line = vl
            print("vanishing_point:", vanishing_point)
            print("vanishing_line:", vanishing_line)

            plt.figure(figsize=(10, 10))
            plot_init(plt, image)





