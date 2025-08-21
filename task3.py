from typing import Any, List, Tuple


class FlatIterator:
    def __init__(self, list_of_list: List[Any]) -> None:
        self.list_of_list = list_of_list
        self._stack: List[Tuple[List[Any], int]] = []

    def __iter__(self) -> "FlatIterator":
        self._stack = [(self.list_of_list, 0)]
        return self

    def __next__(self) -> Any:
        while self._stack:
            curr_list, idx = self._stack[-1]
            if idx >= len(curr_list):
                self._stack.pop()
                continue
            self._stack[-1] = (curr_list, idx + 1)
            item = curr_list[idx]
            if isinstance(item, list):
                self._stack.append((item, 0))
                continue
            return item
        raise StopIteration


def test_3() -> None:
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'],
    ):
        assert flat_iterator_item == check_item

    result = list(FlatIterator(list_of_lists_2))
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print(result)


if __name__ == "__main__":
    test_3()