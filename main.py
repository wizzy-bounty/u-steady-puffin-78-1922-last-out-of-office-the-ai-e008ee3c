import os
from pathlib import Path

TEXT = "Out of office: I no longer process tickets, I process oat milk; your urgent request is queued behind a flat white."


def output_file() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def main() -> None:
    output_file().write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
