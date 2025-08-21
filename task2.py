import types
from typing import Any, Generator, Iterable, List


def flat_generator(list_of_lists: List[Iterable[Any]]) -> Generator[Any, None, None]:
    for inner in list_of_lists:
        for item in inner:
            yield item


def test_2() -> None:
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item

    result = list(flat_generator(list_of_lists_1))
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print(result)


if __name__ == "__main__":
    test_2()