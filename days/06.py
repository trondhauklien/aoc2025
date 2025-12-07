import sys
from pathlib import Path
import numpy as np

def star_one(data):
    output = 0

    operations = data[-1]
    numbers = np.array(data[:-1], dtype=np.uint)

    for i, o in enumerate(operations):
        if o == "+":
            output += np.sum(numbers[:,i])
        if o == "*":
            output += np.prod(numbers[:,i])
    return output


def star_two(data):
    output = 0
    operations = data[-1].split()
    numbers = []
    for row in data[:-1]:
        numbers.append([d for d in row.replace("\n", "")])
    numbers = np.array(numbers, dtype=str)
    i = -1
    number = int("".join(numbers[:, i]))
    for o in reversed(operations):
        tmp = 0 if o == "+" else 1
        while number:
            # print(o, number, output, tmp)
            if o == "+":
                tmp += number
            if o == "*":
                tmp *= number
            i -= 1
            try:
                number = int("".join(numbers[:, i]))
            except ValueError:
                number = 0
            except IndexError:
                output += tmp
                return output
        output += tmp
        i -= 1
        try:
            number = int("".join(numbers[:, i]))
        except ValueError:
            number = 0
        except IndexError:
            output += tmp
            return output
    return output


def main():
    data = []
    type = sys.argv[2]
    script_name = Path(__file__).name
    day = script_name.replace(".py", "")
    with open(f"data/{day}_{type}.txt") as file:
        data = file.readlines()

    ddata = [d.split() for d in data]

    if sys.argv[1] == "1":
        print(star_one(ddata))
    if sys.argv[1] == "2":
        print(star_two(data))


if __name__ == "__main__":
    main()
