import re


def is_date(s: str) -> bool:
    m = re.fullmatch(r'(\d{2})-(\d{2})-(\d{4})', s)
    if m is None:
        return False
    day = int(m.group(1))
    month = int(m.group(2))
    year = int(m.group(3))
    return 1 <= day <= 31 and 1 <= month <= 12


if __name__ == '__main__':
    assert is_date('01-01-2023')
    assert is_date('99-99-9999')
    assert not is_date('999-99-9999')
    assert not is_date('9-9-9999')
    assert not is_date('9-9-9999')
