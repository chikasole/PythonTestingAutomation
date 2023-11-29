import teachercode


def test_add():
    assert teachercode.add(2, 2) == 4


def test_multiply():
    assert teachercode.multiply(1, 4) == 4
    assert teachercode.multiply(10, 6) == 60


def test_power():
    assert teachercode.power(2, 8) == 256
