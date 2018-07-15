import io
import random
from copy import deepcopy


class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


def time_(point1, point2):
    return int(abs(point1.x - point2.x) + abs(point1.y - point2.y))


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

    variants = list(range(count_))
    best_time = None
    best_variant = None
    for _ in range(180000):
        random.shuffle(variants)
        current_best_time = 100000000000000000000000
        for i, dest in enumerate(variants):
            dest_point = destinations_cost[dest][0]
            dest_cost = destinations_cost[dest][1]
            work_time = time_(drivers[i], dest_point) + dest_cost
            if best_time is not None and work_time > best_time:
                break
            current_best_time = work_time if work_time < current_best_time else current_best_time
        else:
            if best_time is None or current_best_time < best_time:
                best_variant = deepcopy(variants)
                best_time = current_best_time

    return [x + 1 for x in best_variant]


if __name__ == "__main__":
    for x in get_order():
        print(x)
