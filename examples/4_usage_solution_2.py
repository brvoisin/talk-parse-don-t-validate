import os
from pathlib import Path
from typing import TypeGuard, TypeVar, Unpack

T = TypeVar("T")
NonEmptyTuple = tuple[T, Unpack[tuple[T, ...]]]


def head(seq: NonEmptyTuple[T]) -> T:
    return seq[0]


def get_config_directories() -> NonEmptyTuple[Path]:
    config_dirs_string = os.getenv("CONFIG_DIRS", "")
    config_dirs = tuple(
        Path(dir)
        for dir in config_dirs_string.split(",")
        if dir
    )
    if not is_non_empty(config_dirs):
        raise ValueError("CONFIG_DIRS cannot be empty")
    return config_dirs


def is_non_empty(
    seq: tuple[T, ...]
) -> TypeGuard[NonEmptyTuple[T]]:
    return len(seq) > 0


def main() -> None:
    config_dirs = get_config_directories()
    initialize_cache(head(config_dirs))


def initialize_cache(cache_dir: Path) -> None:
    print(f"Initializing cache in {cache_dir}")


if __name__ == "__main__":
    main()
