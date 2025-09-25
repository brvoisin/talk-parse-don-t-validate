from typing import TypeVar

T = TypeVar("T")
NonEmptyTuple = tuple[T, *tuple[T, ...]]


def head(seq: NonEmptyTuple[T]) -> T:
    return seq[0]


print(head((1, 2, 3)))
print(head(tuple()))
# error: Argument 1 to "head" has incompatible type "tuple[Never, ...]"; expected "tuple[Never, *tuple[Never, ...]]"
