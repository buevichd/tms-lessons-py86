import re


def is_car_number(string: str) -> bool:
    return re.fullmatch(r'\d{4}[A-Z]{2}-\d', string) is not None


def is_phone_number(string: str) -> bool:
    return re.fullmatch(r'\+375 \(\d\d\) \d\d\d-\d\d-\d\d', string) is not None


def is_phone_number_2(string: str) -> bool:
    return re.fullmatch(r'\+375 \((25|29|33|44)\) \d\d\d-\d\d-\d\d', string) is not None


if __name__ == '__main__':
    assert is_car_number('1234AB-5')
    assert is_car_number('9999TD-3')
    assert not is_car_number('12345')
    assert not is_car_number('1234aa-6')
    assert not is_car_number('1234AA-A')
    assert not is_car_number('AAAABB-3')

    assert is_phone_number('+375 (29) 123-45-67')
    assert is_phone_number('+375 (99) 999-99-99')
    assert not is_phone_number('+375 99 99-99-99')
    assert not is_phone_number('+5 (99) 999-99-99')
    assert not is_phone_number('999-99-99')

    assert is_phone_number_2('+375 (25) 123-45-67')
    assert is_phone_number_2('+375 (29) 123-45-67')
    assert is_phone_number_2('+375 (33) 123-45-67')
    assert is_phone_number_2('+375 (44) 123-45-67')
    assert not is_phone_number_2('+375 (99) 999-99-99')
    assert not is_phone_number_2('+375 (49) 999-99-99')
    assert not is_phone_number_2('+375 99 99-99-99')
    assert not is_phone_number_2('+5 (99) 999-99-99')
    assert not is_phone_number_2('999-99-99')
