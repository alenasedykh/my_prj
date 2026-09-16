def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список операций по ключу."""
    result = []

    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует операции по дате"""
    result = sorted(operations, key=lambda operation: operation["date"], reverse=reverse)
    return result
