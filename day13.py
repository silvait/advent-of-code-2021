import re
import sys

from utils import get_input_filename


def parse_input(data: str) -> tuple[list[tuple], dict[tuple[int, int], str]]:
    grid = {}
    folds = []

    for line in data.splitlines():
        if line.startswith("fold"):
            [(axis, n)] = re.findall(r"fold along (.)=(\d+)", line)
            folds.append((axis, int(n)))
        elif not line:
            continue
        else:
            x, y = map(int, line.split(","))
            grid[(x, y)] = "#"

    return (folds, grid)


def fold_grid(grid, axis, number):
    new_grid = {}

    for (x, y), v in grid.items():
        if axis == "y":
            if y < number:
                new_grid[(x, y)] = v
            else:
                new_y = y - (2 * (y - number))
                new_grid[(x, new_y)] = v
        else:
            if x < number:
                new_grid[(x, y)] = v
            else:
                new_x = x - (2 * (x - number))
                new_grid[(new_x, y)] = v

    return new_grid


def count_dots(grid):
    return sum(v == "#" for v in grid.values())


def part1(folds, grid) -> int:
    axis, number = folds[0]
    new_grid = fold_grid(grid, axis, number)

    total = count_dots(new_grid)
    return total


def print_grid(grid):
    max_x, max_y = get_grid_size(grid)

    print(max_x, max_y)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(grid.get((x, y), "."), end="")
        print()


def get_grid_size(grid):
    max_x = 0
    max_y = 0

    for x, y in grid.keys():
        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

    return (max_x, max_y)


def part2(folds, grid) -> int:
    for axis, number in folds:
        grid = fold_grid(grid, axis, number)

    print_grid(grid)
    return 0


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(*parsed_data))
