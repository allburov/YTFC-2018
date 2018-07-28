def sverka(input_str=None):
    if input_str is None:
        with open('input.txt') as input_:
            system1 = input_.readline()[:-1]
            system2 = input_.readline()[:-1]
            src = input_.readline()[:-1]
    else:
        system1, system2, src = input_str.splitlines()

    answer = str_from(src, system1, system2, 0, 0, 0)
    if answer:
        return "YES"
    else:
        return "NO"


def str_from(src, system1, system2, src_index, system1_index, system2_index):
    src_len = len(src)
    sys1_len = len(system1)
    sys2_len = len(system2)
    if src_len == src_index:
        if system1_index == sys1_len and system2_index == sys2_len:
            return True
        else:
            return False

    if sys1_len == system1_index:
        if src[src_index] == system2[system2_index]:
            return str_from(src, system1, system2, src_index + 1, system1_index, system2_index + 1)
        else:
            return False
    elif sys2_len == system2_index:
        if src[src_index] == system1[system1_index]:
            return str_from(src, system1, system2, src_index + 1, system1_index + 1, system2_index)
        else:
            return False

    if system1[system1_index] == src[src_index]:
        system1_answer = str_from(src, system1, system2, src_index + 1, system1_index + 1, system2_index)
        if system1_answer:
            return True
    if system2[system2_index] == src[src_index]:
        system2_answer = str_from(src, system1, system2, src_index + 1, system1_index, system2_index + 1)
        if system2_answer:
            return True
    return False


if __name__ == "__main__":
    print(sverka())
