import io
import itertools
from math import fabs


class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


def time_(point1, point2):
    return fabs(point1.x - point2.x) + fabs(point1.y - point2.y)


def how_long(point0, point1, point2):
    return int(time_(point0, point1) + time_(point1, point2))


def get_order(input_str=None):
    if input_str is None:
        input_ = open('input.txt')
    else:
        input_ = io.StringIO(input_str)
    count_ = input_.readline()[:-1]
    count_ = int(count_)
    drivers = {}
    destinations = {}
    for driver in range(count_):
        line = input_.readline()
        drivers[driver] = Point(*line.split())

    for dest in range(count_):
        line = input_.readline()
        destinations[dest] = (Point(*line.split()[:2]), Point(*line.split()[2:]))

    destinations_cost = {x: (y[0], time_(y[0], y[1])) for x, y in destinations.items()}

    variants = itertools.permutations(range(count_), count_)
    best_time = 1000000000
    best_variant = None
    test_count = 0
    for variant in variants:
        times = []
        test_count += 1
        if test_count >=300:
            break
        for i, dest in enumerate(variant):
            dest_point = destinations_cost[dest][0]
            dest_cost = destinations_cost[dest][1]
            work_time = time_(drivers[i], dest_point) + dest_cost
            if work_time > best_time:
                break
            times.append(work_time)
        else:
            max_time = max(times)
            if max_time < best_time:
                best_variant = variant
                best_time = max_time
                test_count = 0

    return [x + 1 for x in best_variant]


if __name__ == "__main__":
    for x in get_order():
        print(x)
