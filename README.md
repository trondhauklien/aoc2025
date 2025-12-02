# My Solutions to AOC 2025

Written in Python. Using Uv as package manager.

## Usage

Assuming you have Uv installed and have cloned the repository:

```bash
uv sync
```

Then run for example day 1 part 2 with the following command:

```bash
uv run days/01.py 2 input
```

This will get input from `data/01_input.txt`. Day is inferred from the Python script name and the second argument to the script (e.g. `input`) corresponds to a suffix.

To automatically generate files for the next day, run the following command (substituting `4` with your desired day):

```bash
uv run main.py 4
```

The argument is the day you wish to generate boilerplate for. The following files will be created: `data/{day}_input.txt`, `data/{day}_test.txt` and `days/{day}.py`.
