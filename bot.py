"""Launch the example bot from the repository root."""

from pathlib import Path
from runpy import run_path

if __name__ == "__main__":
    run_path(str(Path(__file__).with_name("05-example_bot") / "bot.py"), run_name="__main__")
