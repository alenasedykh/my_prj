from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations() -> list[dict[str, Any]]:
    """Возвращает список операций с разными состояниями и датами."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-15T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-20T09:00:00"},
        {"id": 4, "state": "PENDING", "date": "2025-06-01T15:30:00"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(
    operations: list[dict[str, Any]],
    state: str,
    expected_ids: list[int],
) -> None:
    """Проверяет фильтрацию операций по заданному состоянию."""
    result = filter_by_state(operations, state)
    assert [operation["id"] for operation in result] == expected_ids


def test_filter_by_state_default(
    operations: list[dict[str, Any]],
) -> None:
    """Проверяет фильтрацию по состоянию EXECUTED по умолчанию."""
    result = filter_by_state(operations)
    assert [operation["id"] for operation in result] == [1, 3]


def test_sort_by_date_descending(
    operations: list[dict[str, Any]],
) -> None:
    """Проверяет сортировку от новых операций к старым по умолчанию."""
    result = sort_by_date(operations)
    assert [operation["id"] for operation in result] == [4, 1, 3, 2]


def test_sort_by_date_ascending(
    operations: list[dict[str, Any]],
) -> None:
    """Проверяет сортировку от старых операций к новым."""
    result = sort_by_date(operations, reverse=False)
    assert [operation["id"] for operation in result] == [2, 3, 1, 4]


def test_sort_by_date_does_not_modify_original(
    operations: list[dict[str, Any]],
) -> None:
    """Проверяет, что исходный список не изменяется при сортировке."""
    original_ids = [operation["id"] for operation in operations]
    sort_by_date(operations)
    assert [operation["id"] for operation in operations] == original_ids
