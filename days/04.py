import sys
from pathlib import Path
import numpy as np
import numpy.typing as nt
from scipy import signal


def star_one(data):
    data = np.array(data)

    data[data == "."] = 0
    data[data == "@"] = 1

    data = np.array(data, dtype=np.uint8)

    print(data)

    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    kernel[1, 1] = 0
    print(kernel)

    c = signal.convolve2d(data, kernel)
    print(c)

    cropped = c[1:-1, 1:-1]
    print(cropped)

    return np.sum(data, where=cropped < 4)


def filter(array: nt.NDArray, kernel: nt.NDArray):
    c = signal.convolve2d(array, kernel)
    cropped = c[1:-1, 1:-1]
    mask = cropped >= 4

    output = array * mask
    num = np.sum(array, where=cropped < 4)

    return (output, num)


def star_two(data):
    data = np.array(data)

    data[data == "."] = 0
    data[data == "@"] = 1

    data = np.array(data, dtype=np.uint8)

    kernel = np.ones(shape=(3, 3), dtype=np.uint8)
    kernel[1, 1] = 0

    output = 0
    num = 1
    while num > 0:
        data, num = filter(data, kernel)
        output += num
    return output


def main():
    data = []
    type = sys.argv[2]
    script_name = Path(__file__).name
    day = script_name.replace(".py", "")
    with open(f"data/{day}_{type}.txt") as file:
        lines = file.readlines()

        for line in lines:
            data.append([e for e in line.strip()])

    if sys.argv[1] == "1":
        print(star_one(data))
    if sys.argv[1] == "2":
        print(star_two(data))


if __name__ == "__main__":
    main()
