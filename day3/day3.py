import re
from dataclasses import dataclass
from pathlib import Path
from typing import List

import numpy as np


@dataclass
class Number:
    number: int
    y: int
    xstart: int
    xend: int
    neighbors: List[str]

    def has_symbol(self) -> bool:
        return any(
            [y not in (["."] + [str(x) for x in range(10)]) for y in self.neighbors]
        )

    def is_near(self, x, y) -> bool:
        return (self.y - 1 <= y <= self.y + 1) and (
            self.xstart - 1 <= x < self.xend + 1
        )


@dataclass
class Gear:
    y: int
    x: int
    neighbor_numbers: List[Number]

    def has_two_numbers(self) -> bool:
        return len(self.neighbor_numbers) == 2

    def gear_ratio(self) -> int:
        return int(np.prod([nn.number for nn in self.neighbor_numbers]))


@dataclass
class Matrix:
    _matrix: List[List[str]]
    numbers: List[Number]
    gears: List[Gear]
    xlen: int
    ylen: int

    def __init__(self, fullstr):
        self._matrix = []
        self.numbers = []
        self.gears = []
        for line in fullstr.split("\n"):
            if len(line) == 0:
                continue
            row = list(line)
            self.xlen = len(row)
            self._matrix.append(row)
        self.ylen = len(self._matrix)
        self.init_numbers()
        self.init_gears()

    def init_gears(self):
        y = 0
        for line in fullstr.split("\n"):
            for match in re.finditer(r"\*", line):
                nn = []
                for num in self.numbers:
                    if num.is_near(match.start(), y):
                        nn.append(num)
                self.gears.append(Gear(y=y, x=match.start(), neighbor_numbers=nn))
            y += 1

    def init_numbers(self):
        y = 0
        for line in fullstr.split("\n"):
            for match in re.finditer(r"\d+", line):
                neig = []
                for x in range(match.start(), match.end()):
                    neig = list(set(neig + self.get_neighbors(x, y)))
                self.numbers.append(
                    Number(
                        number=int(match.group(0)),
                        y=y,
                        xstart=match.start(),
                        xend=match.end(),
                        neighbors=neig,
                    )
                )
            y += 1

    def get_element(self, x: int, y: int):
        if x >= self.xlen or y >= self.ylen:
            return "."
        else:
            return self._matrix[y][x]

    def get_neighbors(self, x: int, y: int):
        neig = []
        for xx in [x - 1, x, x + 1]:
            for yy in [y - 1, y, y + 1]:
                neig.append(self.get_element(xx, yy))
        return neig

    def res1(self):
        res = 0
        for n in self.numbers:
            # print(f"n={n.number} {n.has_symbol()}")
            if n.has_symbol():
                res += n.number
        return res

    def res2(self):
        res = 0
        for n in self.gears:
            if n.has_two_numbers():
                res += n.gear_ratio()
        return res


# fullstr = str(Path("test.txt").read_text())
fullstr = str(Path("day3.txt").read_text())
m = Matrix(fullstr)
# print(m)
# print(fullstr)
print(m.res1())
print(m.res2())
