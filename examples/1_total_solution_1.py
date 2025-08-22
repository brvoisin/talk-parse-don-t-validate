from collections.abc import Sequence
from typing import NewType

NothingType = NewType("NothingType", str)
Nothing = NothingType("Nothing")


def head[T](seq: Sequence[T]) -> T | NothingType:
    if not seq:
        return Nothing
    return seq[0]


print(head([]))
print(head([1, 2, 3]))
print(head([None]))
