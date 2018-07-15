from collections import namedtuple


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


def rotate(l, n):
    return l[-n:] + l[:-n]


Point = namedtuple('Point', 'x, y')
Line = namedtuple('Line', 'point1, point2')


def len_line(point1, point2):
    # len_ = sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
    len_ = (point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2
    return len_


def ratio_line(line1point1, line1point2, line2point1, line2point2):
    # len_ = sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
    len_ = ((line1point2.x - line1point1.x) ** 2 + (line1point2.y - line1point1.y) ** 2) / (
            (line2point2.x - line2point1.x) ** 2 + (line2point2.y - line2point1.y) ** 2)
    return len_


def ratio_(line1, line2, line3, line4):
    # len_ = sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
    fir = (((line1.point2.x - line1.point1.x) ** 2 + (line1.point2.y - line1.point1.y) ** 2) * (
                (line3.point2.x - line3.point1.x) ** 2 + (line3.point2.y - line3.point1.y) ** 2))
    sec = (((line2.point2.x - line2.point1.x) ** 2 + (line2.point2.y - line2.point1.y) ** 2) * (
                (line4.point2.x - line4.point1.x) ** 2 + (line4.point2.y - line4.point1.y) ** 2))
    fir = round(fir, 2)
    sec = round(sec, 2)
    if fir == 0 or sec == 0:
        return False
    result = (sec / fir).is_integer()
    return result


def similar(input_str=None):
    if input_str is None:
        with open('input.txt') as input_:
            vertex_count = input_.readline()[:-1]
            shape1 = input_.readline()[:-1]
            shape2 = input_.readline()[:-1]
    else:
        _, vertex_count, shape1, shape2 = input_str.splitlines()
    vertex_count = int(vertex_count)

    shape1_points = [Point(float(x), float(y)) for x, y in pairwise(shape1.split())]
    shape2_points = [Point(float(x), float(y)) for x, y in pairwise(shape2.split())]

    for point_count in range(vertex_count):
        shape2_rotated = rotate(shape2_points, point_count)
        init_ = True
        for i in range(vertex_count):
            j = 0 if i == (vertex_count - 1) else i + 1
            shape1_line = Line(shape1_points[i], shape1_points[j])
            shape2_line = Line(shape2_rotated[i], shape2_rotated[j])
            if init_:
                shape1_pattern = shape1_line
                shape2_pattern = shape2_line
                init_ = False
            else:
                # ratio_next = shape1_line / shape2_line
                sim_line = ratio_(shape1_line, shape2_line, shape1_pattern, shape2_pattern)
                if sim_line != 1:
                    break
        else:
            return 1
    return 0


if __name__ == "__main__":
    print(similar())
