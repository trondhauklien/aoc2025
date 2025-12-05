import sys
from pathlib import Path
import numpy as np


def star_one(data: list):
    output = 0
    split = data.index("")
    ranges = np.array([d.split("-") for d in data[:split]], dtype=np.uint)
    ids = np.array(data[split + 1 :], dtype=np.uint)

    print(ranges)
    print(ids)

    for i in ids:
        spoiled = True
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                spoiled = False
                break
        if not spoiled:
            output += 1
    return output


def star_two(data, test=False):
    output = 0
    split = data.index("")

    ranges = np.array([d.split("-") for d in set(data[:split])], dtype=np.uint)

    sorted_ranges = ranges[ranges[:, 0].argsort()]
    print(sorted_ranges)
    # Check for fully overlapping ranges
    del_indices = np.array([], dtype=np.intp)
    for i, r in enumerate(sorted_ranges):
        cond1 = sorted_ranges[:, 0] >= r[0]
        cond2 = sorted_ranges[:, 1] <= r[1]
        cond = cond1 * cond2
        cond[i] = 0
        del_indices = np.append(del_indices, np.argwhere(cond))
    print(del_indices)
    sorted_ranges = np.delete(sorted_ranges, del_indices, axis=0)
    print(sorted_ranges)
    for i, r in enumerate(sorted_ranges[:-1]):
        next_r = sorted_ranges[i + 1]
        if r[1] < next_r[0]:
            output += r[1] + 1 - r[0]
            print(r, r[1] + 1 - r[0]) if test else None
            continue
        overlap = r[1] - next_r[0] + 1
        if overlap > 0:
            output += r[1] + 1 - r[0] - overlap
            print(r, r[1] + 1 - r[0] - overlap) if test else None
    output += sorted_ranges[-1, 1] + 1 - sorted_ranges[-1, 0]
    if test:
        print(test_r(ranges))
    return output


def test_r(ranges):
    numbers = np.array([], dtype=np.uint8)
    for r in ranges:
        numbers = np.append(numbers, np.arange(r[0], r[1] + 1))

    return np.unique_values(numbers).size


def main():
    data = []
    type = sys.argv[2]
    script_name = Path(__file__).name
    day = script_name.replace(".py", "")
    with open(f"data/{day}_{type}.txt") as file:
        data = file.readlines()

    ddata = [d.strip() for d in data]

    if sys.argv[1] == "1":
        print(star_one(ddata))
    if sys.argv[1] == "2":
        print(star_two(ddata, sys.argv[2] == "test"))


if __name__ == "__main__":
    main()
