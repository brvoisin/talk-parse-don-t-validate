from collections.abc import Sequence
from typing import Any


def validate_non_empty(seq: Sequence[Any]) -> None:
    if not seq:
        raise ValueError("Sequence is empty")


#####


def validate_phone_number(text: str) -> bool:
    return len(text) == 10 and text.isdigit()


def send_message(phone_number: str, message: str) -> None:
    if not validate_phone_number(phone_number):
        raise ValueError("Invalid phone number")
    print(f"Sending message to {phone_number}: {message}")
