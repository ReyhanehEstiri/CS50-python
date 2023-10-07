from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.1000") == False
    assert validate ('cat.001.dog.bee') == False
    assert validate ('lion') == False
    assert not validate("192.158.1")
    assert not validate("192.168.1.257")
