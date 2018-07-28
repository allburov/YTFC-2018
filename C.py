"""
23 веке после ядерной войны из животных выжили немногие. Из них самыми умными оказались муравьи. Они основали свою цивилизацию и придумали деньги, но продолжили жить в муравейниках.

Муравьям-таксистам нужно определить, есть ли в лабиринте муравейника маршрут заданной длины.

Муравейники состоят из ячеек, между которыми прорыты ходы. Ячейки принадлежат ярусам от 1 до N. Каждая ячейка на i-м ярусе соединена с каждой ячейкой i+1 и i-1 яруса, кроме 1-го и N-го, которые соединены только с одним соседним ярусом (2-м и N-1-м, соответственно). Для каждого хода известна его длина.

Таксисту нужно понять, может ли он подать машину с ячейки 1-го яруса на ячейку N-го яруса, проехав ровно D метров, двигаясь только в сторону увеличения яруса.

Формат ввода
На первой строке задано целое число N – количество ярусов (3 <= N <= 22), вторая - целое число M – число ячеек на каждом ярусе (2 <= M <= 5).

Следующие M * (N-1) строк содержат в себе длины ходов. j + i*M-я строка среди этих строк состоит из M чисел, которые задают длину ходов из ячейки номера j яруса i в ячейку номера 1 яруса i+1, в ячейку номера 2 яруса i+1 и так далее вплоть до номера M. Длина хода – целое число от 0 до 1018.

Следующая стока содержит в себе два числа, номер ячейки 1-го яруса, в которой находится таксист, и номер ячейки N яруса, в которую таксист должен прибыть.

В последней строке записано число D от 0 до 10^18.

Формат вывода
Строка YES, если такой маршрут существует, или NO, если его нет.
"""
import itertools
from functools import lru_cache


def sverka(input_str=None):
    if input_str is None:
        with open('input.txt') as input_:
            input_str = input_.read()
    tiers_count, cells_count, *moves = input_str.splitlines()  # Type: int, int, list
    tiers_count = int(tiers_count)
    cells_count = int(cells_count)
    moves = list(moves)
    max_miles = int(moves.pop(-1))
    taxi_cell, target_cell = moves.pop(-1).split()
    taxi_cell = int(taxi_cell)
    target_cell = int(target_cell)

    assert len(moves) == (tiers_count - 1) * cells_count

    moves_cost = []
    for tier in range(tiers_count):
        tier_costs = moves[tier * cells_count:(tier + 1) * cells_count]
        tier_cost = tuple(tuple(int(y) for y in x.split()) for x in tier_costs)
        moves_cost.append(tier_cost)
    moves_cost = tuple(moves_cost)

    list2 = list(range(cells_count))

    for variant in itertools.product(list2, repeat=tiers_count - 2):
        variant = (taxi_cell, *variant, target_cell)
        if variant[0] != taxi_cell:
            continue
        if variant[-1] != target_cell:
            continue
        cost = calc_cost(moves_cost, 0, variant, max_miles, cells_count, tiers_count)
        if cost == False:
            continue
        if cost == max_miles:
            return True
    return False

    # return calc_cost(moves_cost, 0, taxi_cell, max_miles, 0, cells, tiers, target_cell)


@lru_cache(maxsize=None)
def calc_cost(moves_cost, current_tier, path_, max_miles, cells_count, tiers_count):
    cels_costs = moves_cost[current_tier][path_[0]][path_[1]]
    if len(path_) == 2:
        return cels_costs
    else:
        other = calc_cost(moves_cost, current_tier + 1, path_[1:], max_miles, cells_count, tiers_count)
        if other == False:
            return False
        else:
            result = other + cels_costs
            if result > max_miles:
                return False
            else:
                return result


if __name__ == "__main__":
    if sverka():
        print("YES")
    else:
        print("NO")
