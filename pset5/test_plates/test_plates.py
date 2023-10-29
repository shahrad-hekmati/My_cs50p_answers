from plates import is_valid

def test_begintwoletters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False

def test_length():
    assert is_valid("HICS50") == True
    assert is_valid("CS") == True
    assert is_valid("HELLOCS50") == False

def test_num():
    assert is_valid("AAA345") == True
    assert is_valid("AAA78A") == False
    assert is_valid("AAA090") == False

def test_punct():
    assert is_valid("CS50@") == False
    assert is_valid("CS%") == False
