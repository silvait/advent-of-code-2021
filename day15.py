import heapq
import math
import sys
from collections import defaultdict

from utils import get_input_filename

FIRST_TILE = (0, 0)
MAX_VALUE = 9

type Coordinate = tuple[int, int]


class Grid:
    def __init__(self, rows: int, cols: int):
        self._grid = {}
        self.rows = rows
        self.cols = cols

    def add_value(self, coordinate: Coordinate, value: int):
        self._grid[coordinate] = value

    def get_value(self, coordinate: Coordinate) -> int:
        return self._grid[coordinate]

    def get_neighbors(self, coordinate: Coordinate) -> list[Coordinate]:
        row, col = coordinate

        neighbors = [
            (row, col - 1),
            (row - 1, col),
            (row, col + 1),
            (row + 1, col),
        ]

        return [c for c in neighbors if c in self._grid]

    def first_coordinate(self) -> Coordinate:
        return FIRST_TILE

    def last_coordinate(self) -> Coordinate:
        return (self.rows - 1, self.cols - 1)

    def size(self) -> tuple[int, int]:
        return self.rows, self.cols

    def coordinates(self):
        return self._grid.keys()

    def values(self):
        return self._grid.items()

    def __contains__(self, key: Coordinate) -> bool:
        return key in self._grid


def parse_input(data: str) -> Grid:
    lines = data.splitlines()

    rows = len(lines)
    cols = len(lines[0])
    grid = Grid(rows, cols)

    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            grid.add_value((r, c), int(val))

    return grid


def increase_wrap(val: int, inc: int, max_value: int) -> int:
    new_val = (val + inc) % max_value
    return max_value if new_val == 0 else new_val


def expand_grid(grid: Grid, rows_scale: int, cols_scale: int) -> Grid:
    rows, cols = grid.size()
    expanded_grid = Grid(rows * rows_scale, cols * cols_scale)

    for (r, c), val in grid.values():
        for sr in range(rows_scale):
            for sc in range(cols_scale):
                new_row = r + (rows * sr)
                new_col = c + (cols * sc)
                new_val = increase_wrap(val, sc + sr, MAX_VALUE)

                expanded_grid.add_value((new_row, new_col), new_val)

    return expanded_grid


def find_lowest_risk_path(grid: Grid, start: Coordinate, end: Coordinate) -> float:
    heap = []
    costs = defaultdict(lambda: math.inf)

    heapq.heappush(heap, (0, start))
    costs[start] = 0

    while heap:
        current_cost, current = heapq.heappop(heap)

        if current == end:
            return current_cost

        if costs[current] < current_cost:
            continue

        for neighbor in grid.get_neighbors(current):
            new_cost = current_cost + grid.get_value(neighbor)

            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return math.inf


def part1(grid: Grid) -> float:
    start = grid.first_coordinate()
    end = grid.last_coordinate()

    return find_lowest_risk_path(grid, start, end)


def part2(grid: Grid) -> float:
    expanded_grid = expand_grid(grid, 5, 5)
    return part1(expanded_grid)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
