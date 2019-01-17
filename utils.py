from __future__ import division


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C


def intersection(line1, line2):
    d = line1[0] * line2[1] - line1[1] * line2[0]
    dx = line1[2] * line2[1] - line1[1] * line2[2]
    dy = line1[0] * line2[2] - line1[2] * line2[0]
    if d != 0:
        x = dx / d
        y = dy / d
        return x, y
    else:
        return False


def one_v_line(v_points):
    v_line = (v_points[0], v_points[1])

    pass


def get_v_points(lines):
    # vanishing points
    v_points = []
    for i in range(0, len(lines), 2):
        l1 = lines[i]
        l2 = lines[i+1]
        line1 = line(l1[0], l1[1])
        line2 = line(l2[0], l2[1])
        vp = intersection(line1, line2)
        v_points.append(vp)
        print("Vanishing point:", vp)

    if len(v_points) == 2:
        one_v_line(v_points)
