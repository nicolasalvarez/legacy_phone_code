from legacy_phone_code.legacy_phone_code import translate, is_valid

import pytest

is_valid_data = [
    ("22333", True),
    ("2345667890", True),
    ("098765432", True),
    ("00229*9338844734*4234*", True),
    ("*2345667890", False),
    ("12345667890", False),
    ("23145667890", False),
    ("234566*7890", True),
]

@pytest.mark.parametrize("input,expected", is_valid_data)
def test_is_valid(input, expected):
    assert is_valid(input) == expected

translate_data = [
    ("22333", "BF"),
    ("2*", "A"),
    ("2*22*2222222", "ABCCA"),
    ("222222", "CC"),
    ("777709999", "S Z"),
    ("33622*2777*77727777*7777444664044466833777888444339","EMBARRASSING INTERVIEW"),
]

@pytest.mark.parametrize("input,expected", translate_data)
def test_translate(input, expected):
    assert translate(input) == expected
