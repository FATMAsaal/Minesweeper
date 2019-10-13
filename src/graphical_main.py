"""
GRAPHICAL MAIN
"""

from graphicalboard import *
from minesweeper import *
import sys


game=make_game(10,10,5)
create(game)

print(sys.stdin.readline())
