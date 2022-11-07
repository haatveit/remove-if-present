from __future__ import annotations

import argparse
import logging
import pathlib
from typing import Sequence

logger = logging.getLogger(__name__)


def remove_if_present(file: str) -> bool:
    path = pathlib.Path(file)
    success = True
    if path.exists():
        try:
            if path.is_dir():
                logger.info(f"Removing directory '{path}'.")
                path.rmdir()
            elif path.is_file() or path.is_symlink():
                logger.info(f"Removing file '{path}'.")
                path.unlink()
        except:
            logger.error(f"Failed to remove '{path}'.")
            success = False
    return success


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Removes files if they are present.")
    parser.add_argument("filenames", nargs="*", help="Files to remove if present")
    args = parser.parse_args()

    retval = 0

    for file in args.filenames:
        if not remove_if_present(file=file):
            retval = 1

    return retval


if __name__ == "__main__":
    raise SystemExit(main())
