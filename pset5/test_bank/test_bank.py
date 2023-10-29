from bank import value

def test_greeting():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
    assert value("How's it going?") == 20
    assert value("What's happening?") == 100
    assert value("What's up?") == 100