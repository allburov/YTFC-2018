from F import similar


def test_example1():
    input_str = """
3
1.0 1.0 2.0 2.0 3.0 1.0
1.0 1.0 2.0 2.0 3.0 1.0
"""
    assert similar(input_str) == 1


def test_example2():
    input_str = """
3
1.0 1.0 2.0 2.0 3.0 1.0
1.0 6.0 2.0 7.0 3.0 6.0
"""
    assert similar(input_str) == 1


def test_example3():
    input_str = """
3
1.0 1.0 2.0 2.0 3.0 1.0
1.0 6.0 2.0 7.0 3.0 7.0
"""
    assert similar(input_str) == 0


def test_example2_minus():
    input_str = """
3
-1.0 -1.0 2.0 2.0 3.0 1.0
-1.0 -1.0 2.0 2.0 3.0 1.0
"""
    assert similar(input_str) == 1


def test_example1_00():
    input_str = """
3
0.1 0.1 0.2 0.2 0.3 0.1
1.0 1.0 2.0 2.0 3.0 1.0
"""
    assert similar(input_str) == 1


def test_example1_000():
    input_str = """
3
-0.011 -0.011 -0.021 -0.021 -0.031 -0.011
1.1 1.1 2.1 2.1 3.1 1.1
"""
    assert similar(input_str) == 1


def test_example1_1():
    input_str = """
3
1.0 1.0 2.0 2.0 3.0 1.0
1.1 1.0 2.0 2.0 3.0 1.0
"""
    assert 0 == similar(input_str)
