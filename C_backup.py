from functools import lru_cache


def sverka(input_str=None):
    if input_str is None:
        with open('input.txt') as input_:
            input_str = input_.read()
    tiers, cells, *moves = input_str.splitlines()  # Type: int, int, list
    tiers = int(tiers)
    cells = int(cells)
    moves = list(moves)
    miles = int(moves.pop(-1))
    taxi_cell, target_cell = moves.pop(-1).split()
    taxi_cell = int(taxi_cell)
    target_cell = int(target_cell)

    moves_cost = []
    for tier in range(tiers):
        tier_costs = moves[tier * cells:(tier + 1) * cells]
        tier_cost = [[int(y) for y in x.split()] for x in tier_costs]
        moves_cost.append(tier_cost)

    return calc_cost(moves_cost, 0, taxi_cell, miles, 0, cells, tiers, target_cell)


@lru_cache(maxsize=0)
def calc_cost(moves_cost, current_tier, current_cell, max_miles, current_miles, cells_count, tiers_count, target_cell):
    if current_tier + 1 == tiers_count:
        if max_miles == current_miles and target_cell == current_cell:
            return True
        else:
            return False

    cels_costs = moves_cost[current_tier][current_cell]
    for i in range(cells_count):
        if cels_costs[i] > max_miles:
            continue
        new_miles = current_miles + cels_costs[i]
        if new_miles > max_miles:
            continue
        else:
            answer = calc_cost(moves_cost, current_tier + 1, i, max_miles, new_miles, cells_count, tiers_count,
                               target_cell)
        if answer:
            # print('{}-{} => {}-{}'.format(current_tier, current_cell, current_tier + 1, i))
            return True

        else:
            continue

    return False


if __name__ == "__main__":
    if sverka():
        print("YES")
    else:
        print("NO")
