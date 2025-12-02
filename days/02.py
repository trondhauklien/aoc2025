import sys
from pathlib import Path


def star_one(data):
    output = 0
    for e in data:
        for i in range(int(e[0]), int(e[1]) + 1):
            s = str(i)
            str_length = len(s)
            if str_length % 2 == 1:
                continue
            if s[: str_length // 2] == s[str_length // 2 :]:
                output += i
    return output


def star_two(data):
    output = 0
    for e in data:
        for i in range(int(e[0]), int(e[1]) + 1):
            s = str(i)
            str_length = len(s)
            
            for sub_len in range(1, str_length // 2 + 1):
                if check_matching_string(s[sub_len:], s[0:sub_len]):
                    output += i
                    break
            
    return output

def check_matching_string(s: str, subs: str):
    if len(s) == 0:
        return True
    if s.startswith(subs):
        return check_matching_string(s[len(subs):], subs)
    else:
        return False

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
