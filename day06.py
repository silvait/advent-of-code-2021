import sys
from collections import Counter

from utils import get_input_filename

AFTER_SPAWN_TIMER = 6
NEW_FISH_TIMER = 8


def parse_input(data: str) -> list[int]:
    return list(map(int, data.split(",")))


def simulate(initial_state: list[int], rounds: int) -> int:
    counter = Counter(initial_state)

    for _ in range(rounds):
        births = counter[0]

        for i in range(1, NEW_FISH_TIMER + 1):
            counter[i - 1] = counter[i]

        counter[AFTER_SPAWN_TIMER] += births
        counter[NEW_FISH_TIMER] = births

    return counter.total()


def part1(initial_state: list[int]) -> int:
    return simulate(initial_state, 80)


def part2(initial_state: list[int]) -> int:
    return simulate(initial_state, 256)


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
