from typing import Any, Iterable, List


class FlatIterator:
    def __init__(self, list_of_list: List[List[Any]]) -> None:
        self._data = list_of_list
        self._outer_idx = 0
        self._inner_idx = 0

    def __iter__(self) -> "FlatIterator":
        self._outer_idx = 0
        self._inner_idx = 0
        return self

    def __next__(self) -> Any:
        while self._outer_idx < len(self._data):
            current_list: Iterable[Any] = self._data[self._outer_idx]
            if self._inner_idx < len(current_list):
                item = current_list[self._inner_idx]
                self._inner_idx += 1
                return item
            self._outer_idx += 1
            self._inner_idx = 0
        raise StopIteration


def test_1() -> None:
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item

    result = list(FlatIterator(list_of_lists_1))
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print(result)


if __name__ == "__main__":
    test_1()