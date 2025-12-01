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
