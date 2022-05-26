import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import total_ordering
from typing import List


class Tray:
    def __init__(self, name: str, dice:List["Die"]) -> None:
        self.dice: List["Die"] = dice

    def print(self) -> None:
        print(f"{self.name}:")
        for die in self.dice:
            print(f"d{die.value}")

    def add(self, die: "Die") -> None:
        self.dice.append(die)
        self.dice.sort()

    def sort(self) -> None:
        self.dice.sort(reverse=True)

    def __len__(self) -> int:
        return self.dice.len()


@dataclass
@total_ordering
class Die():
    def __init__(self, value: int) -> None:
        self.value = value

    def roll(self) -> int:
        return random.randint(1, self.value)

    def move(self) -> None:
        pass

    def value(self) -> int:
        return self.value

    def __eq__(self, die2) -> bool:
        return self.value == die2.value

    def __gt__(self, die2) -> bool:
        return self.value > die2.value


d20: Die = Die(20)
d12: Die = Die(12)
d10: Die = Die(10)
d8: Die = Die(8)
d6: Die = Die(6)
d4: Die = Die(4)

tray: Tray = Tray("Play", [d8, d10, d12, d20, d6, d4])
holding: Tray = Tray("Holding", [])
tray.print()
tray.sort()
tray.print()
