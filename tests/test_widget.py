import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
    ],
)
def test_mask_account_card(text: str, expected: str) -> None:
    assert mask_account_card(text) == expected


@pytest.mark.parametrize(
    "text",
    [
        "",
        "   ",
        "Visa Platinum",
    ],
)
def test_mask_account_card_invalid_input(text: str) -> None:
    assert mask_account_card(text) is None


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2000-01-01T00:00:00.000000", "01.01.2000"),
        ("2025-12-31T23:59:59.999999", "31.12.2025"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected


@pytest.mark.parametrize(
    "date_string",
    [
        "",
        "не дата",
        "2024-13-45T25:61:61.123456",
        None,
    ],
)
def test_get_date_invalid_input(date_string: str | None) -> None:
    assert get_date(date_string) is None  # type: ignore[arg-type]
