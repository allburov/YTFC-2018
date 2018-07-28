from A import sverka


def test_example1():
    input_str = """bbabba
bcacabbccc
bbcacbabbcabbac
"""
    assert sverka(input_str) == "NO"


def test_example2():
    input_str = """bbabba
bcacabbcc
bbcacbabbcabbac
"""
    assert sverka(input_str) == "YES"


def test_example3():
    input_str = """aaccc
abbaff
aabbaacccff
"""
    assert sverka(input_str) == "YES"


def test_example4():
    input_str = """acacc
abbaff
aabbaacccff
"""
    assert sverka(input_str) == "NO"


def test_example5():
    input_str = """acaccZZ123
abbaff
aabbaacccff123ZZ
"""
    assert sverka(input_str) == "NO"


def test_example6():
    input_str = """aatcccZ123
abbaffZ
aatabbacccffZ123Z
"""
    assert sverka(input_str) == "YES"


def test_example7():
    input_str = """aatcccZ123AFE
abbaffZEF
aatabbacccffZ123ZAFEEF
"""
    assert sverka(input_str) == "YES"


def test_example8():
    input_str = """
abbaffZEF
abbaffZEF
"""
    assert sverka(input_str) == "YES"


def test_example9():
    input_str = """abcdefgg
abcdefg
abcdefgabcdefg
"""
    assert sverka(input_str) == "NO"


def test_example10():
    input_str = """


"""
    assert sverka(input_str) == "YES"
