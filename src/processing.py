from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список операций по ключу."""
    result = []

    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует операции по дате."""
    result = sorted(operations, key=lambda operation: operation["date"], reverse=reverse)
    return result
