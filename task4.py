import types
from typing import Any, Generator, List


def flat_generator(list_of_list: List[Any]) -> Generator[Any, None, None]:
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


def test_4() -> None:
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []],
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'],
    ):
        assert flat_iterator_item == check_item

    result = list(flat_generator(list_of_lists_2))
    assert result == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
    print(result)


if __name__ == "__main__":
    test_4()