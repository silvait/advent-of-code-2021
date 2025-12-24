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
        elif line:
            x, y = map(int, line.split(","))
            grid[(x, y)] = "#"

    return (folds, grid)


def fold_grid(grid, axis, number):
    new_grid = {}
    axis = 1 if axis == "y" else 0

    for coord, v in grid.items():
        new_coord = list(coord)

        if coord[axis] > number:
            new_coord[axis] = (2 * number) - coord[axis]

        new_grid[tuple(new_coord)] = v

    return new_grid


def count_dots(grid):
    return sum(v == "#" for v in grid.values())


def part1(folds, grid) -> int:
    axis, number = folds[0]
    new_grid = fold_grid(grid, axis, number)

    return count_dots(new_grid)


def print_grid(grid):
    max_x, max_y = get_grid_size(grid)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(grid.get((x, y), "."), end="")
        print()


def get_grid_size(grid):
    size = (0, 0)

    for x, y in grid.keys():
        size = (max(size[0], x), max(size[1], y))

    return size


def part2(folds, grid):
    for axis, number in folds:
        grid = fold_grid(grid, axis, number)

    print_grid(grid)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(*parsed_data))
