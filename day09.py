import math
import sys

from utils import get_input_filename

type Point = tuple[int, int]
type Grid = dict[Point, int]


def parse_input(data: str) -> Grid:
    grid = {}

    for r, row in enumerate(data.splitlines()):
        for c, col in enumerate(row):
            grid[(r, c)] = int(col)

    return grid


def get_adjacent_points(point: Point, grid: Grid):
    row, col = point
    adjacent_points = [(row, col - 1), (row - 1, col), (row, col + 1), (row + 1, col)]
    return (p for p in adjacent_points if p in grid)


def get_adjacent_values(point: Point, grid: Grid) -> list[int]:
    return [grid[p] for p in get_adjacent_points(point, grid)]


def is_low_point(point: Point, grid: Grid) -> bool:
    p_value = grid[point]

    if p_value == 9:
        return False

    return all(p_value < a_value for a_value in get_adjacent_values(point, grid))


def find_low_points(grid: Grid) -> list[Point]:
    return [p for p in grid.keys() if is_low_point(p, grid)]


def find_basin_size(low_point: Point, grid: Grid) -> int:
    next_point = [low_point]
    basin = set()

    while next_point:
        current = next_point.pop(0)

        if current in basin:
            continue

        basin.add(current)

        for p in get_adjacent_points(current, grid):
            if grid[p] != 9:
                next_point.append(p)

    return len(basin)


def part1(grid: Grid) -> int:
    return sum(grid[p] + 1 for p in find_low_points(grid))


def part2(grid: Grid) -> int:
    basin_sizes = [find_basin_size(p, grid) for p in find_low_points(grid)]
    top3 = sorted(basin_sizes, reverse=True)[:3]

    return math.prod(top3)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
