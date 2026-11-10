import argparse
import shutil
from pathlib import Path


def category_for(file_path):
    """Return the lowercase extension, or 'no-extension'."""
    pass


def plan_moves(source_dir):
    """Return (source, destination) pairs for files directly in source_dir."""
    pass


def show_plan(plan):
    """Print every planned move without changing any files."""
    pass


def apply_plan(plan):
    """Move planned files, skipping destinations that already exist."""
    pass


def main():
    parser = argparse.ArgumentParser(description="Organize files by extension.")
    parser.add_argument("directory", type=Path, help="Folder containing files to organize")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Move files after showing the organization plan",
    )
    args = parser.parse_args()

    if not args.directory.is_dir():
        parser.error("directory must be an existing folder")

    plan = plan_moves(args.directory)
    show_plan(plan)

    if args.apply:
        apply_plan(plan)
    else:
        print("Preview only. Run again with --apply to move the files.")


if __name__ == "__main__":
    main()