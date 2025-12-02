import sys
from pathlib import Path


def star_one(data):
    output = 0

    return output


def star_two(data):
    output = 0

    return output


def main():
    data = []
    type = sys.argv[2]
    script_name = Path(__file__).name
    day = script_name.replace(".py", "")
    with open(f"data/{day}_{type}.txt") as file:
        data = file.readlines()

    ddata = [d.split("-") for d in data[0].split(",")]

    if sys.argv[1] == "1":
        print(star_one(ddata))
    if sys.argv[1] == "2":
        print(star_two(ddata))


if __name__ == "__main__":
    main()
