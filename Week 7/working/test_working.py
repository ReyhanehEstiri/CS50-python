import pytest
from working import convert


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert('09:00 AM to 3:00 PM') == "09:00 to 15:00"
    assert convert('03:11 AM to 8:59 AM') == "03:11 to 08:59"

def test_value_error():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")

if __name__ == '__main__':
    main()