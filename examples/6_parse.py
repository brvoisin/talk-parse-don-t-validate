from collections.abc import Sequence
from typing import Any, TypeGuard, Unpack

NonEmptyTuple = tuple[Any, Unpack[tuple[Any, ...]]]


def parse_non_empty(seq: Sequence[Any]) -> NonEmptyTuple:
    result = tuple(seq)
    if not is_non_empty(result):
        raise ValueError("Sequence is empty")
    return result


def is_non_empty(
    seq: tuple[Any, ...]
) -> TypeGuard[NonEmptyTuple]:
    return len(seq) > 0


#####

from typing import NewType

ValidPhoneNumber = NewType("ValidPhoneNumber", str)


def parse_phone_number(text: str) -> ValidPhoneNumber:
    if len(text) != 10 and not text.isdigit():
        raise ValueError("Invalid phone number")
    return ValidPhoneNumber(text)


def send_message(
    phone_number: ValidPhoneNumber, message: str
) -> None:
    print(f"Sending message to {phone_number}: {message}")
