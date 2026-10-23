import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("7777777777777777", "7777 77** **** 7777"),
        ("12345678", "1234 56** **** 5678"),
        ("12345678901234567890", "1234 56** **** 7890"),
    ],
)
def test_get_mask_card_number(
    card_number: str, expected: str
) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567890123456", "**3456"),
        ("1234", "**1234"),
        ("12", "**12"),
        ("12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account(
    account_number: str, expected: str
) -> None:
    assert get_mask_account(account_number) == expected
