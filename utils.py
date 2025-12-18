def get_input_filename(argv):
    if len(argv) < 2:
        return argv[0].replace(".py", ".txt")

    return argv[1]


def compare(a, b):
    if a < b:
        return -1

    if a > b:
        return 1

    return 0


def get_line_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    step_x = compare(x1, x2)
    step_y = compare(y1, y2)

    points = [p1]

    while (x1, y1) != p2:
        x1 -= step_x
        y1 -= step_y
        points.append((x1, y1))

    return points
