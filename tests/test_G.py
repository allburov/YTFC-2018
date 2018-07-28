from G import get_order


def test_example1():
    input_str = """1
1 1
2 2 3 3
"""
    assert [1] == get_order(input_str)


def test_example2():
    input_str = """2
1 1
2 2
2 2 3 3
1 1 3 3
"""
    assert [2, 1] == get_order(input_str)


def test_example3():
    input_str = """3
100 100
200 200
300 300
190 230 180 220
190 190 400 400
249 249 700 700
"""
    order = get_order(input_str)
    assert [2, 3, 1] == order or [1, 3, 2] == order
