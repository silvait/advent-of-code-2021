import sys

from utils import get_input_filename


def parse_input(data: str) -> list[str]:
    return data.splitlines()


CLOSING_SYMBOLS = ["}", ">", "]", ")"]
SYMBOL_PAIRS = {"[": "]", "(": ")", "<": ">", "{": "}"}

COMPLETION_SYMBOL_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}
ILLEGAL_SYMBOL_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}


def get_closing_symbol(opening_symbol: str) -> str:
    return SYMBOL_PAIRS[opening_symbol]


def is_closing_symbol(symbol: str) -> bool:
    return symbol in CLOSING_SYMBOLS


def score_illegal_symbol(symbol: str) -> int:
    return ILLEGAL_SYMBOL_SCORE[symbol]


def score_completion_symbol(symbol: str) -> int:
    return COMPLETION_SYMBOL_SCORE[symbol]


def find_illegal_symbol(line: str) -> str | None:
    queue = []

    for symbol in line:
        if is_closing_symbol(symbol):
            if queue[-1] != symbol:
                return symbol

            queue.pop()
        else:
            queue.append(get_closing_symbol(symbol))

    return None


def part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        if symbol := find_illegal_symbol(line):
            total += score_illegal_symbol(symbol)

    return total


def score_completion(completion: str) -> int:
    total = 0

    for symbol in completion:
        total = (total * 5) + score_completion_symbol(symbol)

    return total


def complete_line(incomplete_line: str) -> list[str]:
    queue = []

    for symbol in incomplete_line:
        if is_closing_symbol(symbol):
            queue.pop()
        else:
            queue.append(get_closing_symbol(symbol))

    return reversed(queue)


def part2(lines: list[str]) -> int:
    scores = []

    for line in lines:
        if find_illegal_symbol(line) is None:
            completion = complete_line(line)
            score = score_completion(completion)
            scores.append(score)

    sorted_scores = sorted(scores)
    total = len(sorted_scores)

    return sorted_scores[total // 2]


if __name__ == "__main__":
    filename = get_input_filename(sys.argv)

    with open(filename, "r", encoding="utf-8") as f:
        parsed_data = parse_input(f.read())

        for solve in [part1, part2]:
            print(solve(parsed_data))
