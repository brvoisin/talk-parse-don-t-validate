from collections.abc import Sequence


def head[T](seq: Sequence[T]) -> T:
    return seq[0]


print(head([]))
