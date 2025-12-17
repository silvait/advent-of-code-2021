import sys


def parse_input(data):
    return []


def part1(*args):
    total = 0
    return total


def part2(*args):
    total = 0
    return total


if __name__ == "__main__":
    filename = "./sample.txt" if len(sys.argv) < 2 else sys.argv[1]

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
