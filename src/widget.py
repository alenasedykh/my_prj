from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(text: str) -> str | None:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if not text or not text.strip():
        return None

    try:
        name, number = text.rsplit(" ", 1)

        if name == "Счет":
            masked_number = get_mask_account(number)
        else:
            masked_number = get_mask_card_number(number)

        return f"{name} {masked_number}"

    except ValueError:
        return None


def get_date(date_string: str) -> str | None:
    """Преобразует дату в формат ДД.ММ.ГГГГ"""

    try:
        date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
        return date.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return None
