from bank.bank import value


def test_greeting():
    assert value("hello world") == 0
    assert value("Hello World") == 0
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
    assert value("wasssup world") == 100
    assert value("Wassup WORLD") == 100
