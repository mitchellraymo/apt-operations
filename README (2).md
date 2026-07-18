"""Command-line interface for APT operations utilities."""

import argparse
from pathlib import Path

from apt_ops.validation import missing_required_paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="APT manufacturing operations utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate", help="validate required repository structure")
    validate.add_argument("path", nargs="?", default=".", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "validate":
        missing = missing_required_paths(args.path.resolve())
        if missing:
            print("Missing required paths:")
            for path in missing:
                print(f"- {path}")
            return 1
        print("APT operations repository structure is valid.")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
