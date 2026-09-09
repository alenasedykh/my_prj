def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формат XXXX XX** **** XXXX"""
    # Нужно поделить на части полученное значение
    part1 = card_number[:4]
    part2 = card_number[4:6] + "**"
    part3 = "****"
    part4 = card_number[-4:]

    # Из этих пунктов теперь собираем строку
    return f"{part1} {part2} {part3} {part4}"


def get_mask_account(card_number: str) -> str:
    """Маскирует номер банковского счета"""
    return f"**{card_number[-4:]}"
