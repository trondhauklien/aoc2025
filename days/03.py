import sys
from pathlib import Path
import numpy as np
import numpy.typing as npt


def star_one(data):
    sum = 0
    for d in data:
        s = np.array([int(letter) for letter in d.strip()])
        max_index = np.argmax(s[:-1])
        max_first = s[max_index]
        rest_s = s[max_index + 1 :]
        max_second = rest_s[np.argmax(rest_s)]

        sum += int(f"{max_first}{max_second}")
    return sum


def find_max(s: npt.NDArray, digit: int):
    if digit:
        max_index = np.argmax(s[:-digit])
    else:
        max_index = np.argmax(s)
    max_first = s[max_index]
    rest_s = s[max_index + 1 :]

    return max_first, rest_s


def star_two(data):
    output = 0
    holder = np.zeros(shape=(len(data), 12), dtype=int)
    for i, d in enumerate(data):
        s = np.array([int(letter) for letter in d.strip()])

        for j in range(12, 0, -1):
            m, s = find_max(s, j - 1)
            holder[i, 12 - j] = m

    for row in holder:
        output += int(np.array2string(row, separator="")[1:-1])

    return output


def main():
    data = []
    type = sys.argv[2]
    script_name = Path(__file__).name
    day = script_name.replace(".py", "")
    with open(f"data/{day}_{type}.txt") as file:
        data = file.readlines()

    if sys.argv[1] == "1":
        print(star_one(data))
    if sys.argv[1] == "2":
        print(star_two(data))


if __name__ == "__main__":
    main()
