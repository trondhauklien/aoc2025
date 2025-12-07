import sys
from pathlib import Path
import numpy as np
import numpy.typing as nt


def star_one(data):
    output = 0
    a = np.array(data)
    # print(a)
    (beam_columns,) = np.nonzero(a[0] == "S")
    for i, row in enumerate(a):
        # print(row)
        (splitters,) = np.nonzero(a[i] == "^")
        # print(splitters)
        if splitters.size > 0:
            splits = np.intersect1d(splitters, beam_columns)
            print(splits)
            output += splits.size
            old_beams = np.setdiff1d(beam_columns, splits)
            new_beams = np.append(
                splits + 1,
                splits - 1,
            )
            beam_columns = np.append(old_beams, new_beams)
            cond1 = beam_columns >= 0
            cond2 = beam_columns < row.size
            beam_columns = beam_columns[cond1 * cond2]
            # print(cond1 * cond2)
            beam_columns = np.unique_values(beam_columns)
            # print(beam_columns)

    return output


def star_two(data):
    output = 1
    a = np.array(data)
    # print(a)
    beam_i = a[0] == "S"
    beam_i = np.array(beam_i, dtype=np.uint64)
    for i, row in enumerate(a):
        # print(row)
        (splitters,) = np.nonzero(a[i] == "^")
        # print(splitters)
        new_beams = np.zeros(shape=(row.shape), dtype=np.uint64)
        for splitter in splitters:
            splitted_beams = beam_i[splitter]
            # print(splitted_beams)
            output += splitted_beams
            beam_i[splitter] = 0
            new_beams[splitter + 1] += splitted_beams
            new_beams[splitter - 1] += splitted_beams
            # print(new_beams)
        beam_i += new_beams

    return output


def main():
    data = []
    type = sys.argv[2]
    script_name = Path(__file__).name
    day = script_name.replace(".py", "")
    with open(f"data/{day}_{type}.txt") as file:
        data = file.readlines()

    ddata = []
    for i, row in enumerate(data):
        ddata.append([s for s in row.strip()])

    if sys.argv[1] == "1":
        print(star_one(ddata))
    if sys.argv[1] == "2":
        print(star_two(ddata))


if __name__ == "__main__":
    main()
