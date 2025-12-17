import sys

from utils import get_input_filename

type Command = tuple[int, int]


def parse_input(data: str) -> list[Command]:
    return list(map(parse_command, data.splitlines()))


def parse_command(line: str) -> Command:
    direction, units_str = line.split()
    units = int(units_str)

    match direction:
        case "forward":
            return (units, 0)

        case "down":
            return (0, units)

        case "up":
            return (0, -units)

        case other:
            raise ValueError(f"Unknown command '{other}'")


def part1(commands: list[Command]) -> int:
    horizontal = 0
    depth = 0

    for h, d in commands:
        horizontal += h
        depth += d

    return horizontal * depth


def part2(commands: list[Command]) -> int:
    horizontal = 0
    depth = 0
    aim = 0

    for h, d in commands:
        horizontal += h
        depth += aim * h
        aim += d

    return horizontal * depth


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
