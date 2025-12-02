from pathlib import Path
import sys
import shutil

def main():
    day = int(sys.argv[1])
    repo = Path(__file__).parent
    data_dir = repo / "data"
    data_dir.mkdir(exist_ok=True)
    input_file = data_dir / f"{day:02d}_day_input.txt"
    test_file = data_dir / f"{day:02d}_test.txt"
    input_file.touch()
    test_file.touch()

    template = repo / "days" / "00.py"
    dest = repo / "days" / f"{day:02d}.py"
    shutil.copyfile(template, dest)

if __name__ == "__main__":
    main()
