import sys
from math import trunc
from pathlib import Path


def star_one(data):
    output = 0
    value = 50
    for rotation, num in data:
        if rotation == "L":
            value -= num
        else:
            value += num
        value %= 100
        if value == 0:
            output += 1

    return output


def star_two(data):
    output = 0
    value = 50
    for rotation, num in data:
        old_value = value
        if rotation == "L":
            value -= num
        else:
            value += num
        if value < 0 and old_value != 0:
            output += 1
        if value > 100 or value < -100:
            output += abs(trunc(value / 100))
        elif value % 100 == 0:
            output += 1
        value %= 100

    return output


def main():
    data = []
    type = sys.argv[2]
    script_name = Path(__file__).name
    day = script_name.replace(".py", "")
    with open(f"data/{day}_{type}.txt") as file:
        data = file.readlines()

    ddata = [(d[0], int(d[1:])) for d in data]

    if sys.argv[1] == "1":
        print(star_one(ddata))
    if sys.argv[1] == "2":
        print(star_two(ddata))


if __name__ == "__main__":
    main()
