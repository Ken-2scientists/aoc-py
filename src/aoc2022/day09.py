"""Solution to https://adventofcode.com/2022/day/9"""
from itertools import accumulate, repeat
from more_itertools import flatten
from operator import add, sub
# from utils.core import AoCSolution

# Constants

MOVES = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


# Input parsing


def parse_line(line):
    char, count = line.split()
    return (char, int(count))


def parse(input):
    return flatten(repeat(*parse_line(line)) for line in input)

# Puzzle logic

# Move to a utility module


def tmap(f, *args):
    return tuple(map(f, *args))


def cap(num):
    return num // 2 if num % 2 == 0 else num


def tail_delta(tail, head):
    """
    Compute the amount by which the tail position should change based on the
    new position of the knot in front of it
    """
    diff = tmap(sub, head, tail)
    if (abs(diff[0]) <= 1 and abs(diff[1]) <= 1):
        return (0, 0)
    else:
        return tmap(cap, diff)


def move_tail(tail, head):
    """
    Update the tail position based on the knot in front of it
    """
    return tmap(add, tail, tail_delta(tail, head))


def step(chain, cmd):
    tail, head = chain
    newhead = tmap(add, head, MOVES[cmd])
    return [move_tail(tail, newhead), newhead]


def all_moves(cmds):
    return accumulate(cmds, step, initial=[(0, 0), (0, 0)])


def unique_tail_positions(cmds):
    return set(x[0] for x in all_moves(cmds))


def unique_tail_pos_count(cmds):
    return len(unique_tail_positions(cmds))


# Puzzle solutions

def part1(input):
    return unique_tail_pos_count(input)

# day09_soln = \
#     AoCSolution(parse,
#                 p1=
#                 p2=)
