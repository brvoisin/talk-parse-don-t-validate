import os
from collections.abc import Sequence
from pathlib import Path


def head[T](seq: Sequence[T]) -> T | None:
    if not seq:
        return None
    return seq[0]


def get_config_directories() -> Sequence[Path]:
    config_dirs_string = os.getenv("CONFIG_DIRS", "")
    config_dirs = [
        Path(dir)
        for dir in config_dirs_string.split(",")
        if dir
    ]
    if not config_dirs:
        raise ValueError("CONFIG_DIRS cannot be empty")
    return config_dirs


def main() -> None:
    config_dirs = get_config_directories()
    match head(config_dirs):
        case None:
            raise ValueError(
                "should never happen; "
                "already checked config_dirs is non-empty"
            )
        case cache_dir:
            initialize_cache(cache_dir)


def initialize_cache(cache_dir: Path) -> None:
    print(f"Initializing cache in {cache_dir}")


if __name__ == "__main__":
    main()
