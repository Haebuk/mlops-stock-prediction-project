from src.utils import get_from_to


def test_get_from_to_same_year():
    year = 2022
    month = 1
    from_, to = get_from_to(year, month)
    expected_from_, expected_to = "2022-01-01", "2022-02-01"
    assert from_ == expected_from_
    assert to == expected_to


def test_get_from_to_different_year():
    year = 2022
    month = 12
    from_, to = get_from_to(year, month)
    expected_from_, expected_to = "2022-12-01", "2023-01-01"
    assert from_ == expected_from_
    assert to == expected_to
