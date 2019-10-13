#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cell` module

:author: SAAL Fatma

:date: 2018, october

This module provides cell's primitive operations for the minesweeper game.

"""


################################################
# Functions for cell's management
################################################
def make():
    """
    :return: a new hidden cell of a minesweeper's grid.
             existence of a bomb, number of bombs in neigh_borhood
             have to be stated later.
    :rtype: cell
    :UC: none
    :Examples:

    >>> cel = make()
    >>> is_bomb(cel)
    False
    >>> is_hypothetic_bomb(cel)
    False
    >>> is_revealed(cel)
    False
    >>> number_of_bombs_in_neighborhood(cel)
    0
    """

    return {'bomb' : False,
            'hypothetic_bomb' : False,
            'nbombs_neighborhood' : 0,
            'hidden' : True}


def is_bomb(cell):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :return:
       * ``True`` if cell contains a bomb
       * ``False`` otherwise
    :rtype: bool
    :UC: none
    :Examples:

    >>> cel = make()
    >>> is_bomb(cel)
    False
    """
    return cell['bomb']

def is_hypothetic_bomb(cell):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :return:
       * ``True`` if cell is marked as containing a hypothetic bomb
       * ``False`` otherwise
    :rtype: bool
    :UC: none
    :Examples:

    >>> cel = make()
    >>> is_hypothetic_bomb(cel)
    False
    """
    return cell['hypothetic_bomb']

def is_revealed(cell):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :return:
       * ``True`` if cell is revealed
       * ``False`` otherwise
    :rtype: bool
    :UC: none
    :Examples:

    >>> cel = make()
    >>> is_revealed(cel)
    False
    """
    return not cell['hidden']

def number_of_bombs_in_neighborhood(cell):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :return: the number of bomb in the cell's neighborhood
    :rtype: int
    :UC: none
    :Examples:

    >>> cel = make()
    >>> number_of_bombs_in_neighborhood(cel)
    0
    """
    return cell['nbombs_neighborhood']

def reveal(cell):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :return: None
    :rtype: NoneType
    :Side effect: set the state of cell cell as revealed
    :UC: none
    :Examples:

    >>> cel = make()
    >>> is_revealed(cel)
    False
    >>> reveal(cel)
    >>> is_revealed(cel)
    True
    """
    cell['hidden'] = False

def set_bomb(cell):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :return: None
    :rtype: NoneType

    :Side effect: mark the cell as containing a bomb
    :UC: none
    :Examples:

    >>> cel = make()
    >>> is_bomb(cel)
    False
    >>> set_bomb(cel)
    >>> is_bomb(cel)
    True
    """
    cell['bomb'] = True

def set_hypothetic(cell):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :return: None
    :rtype: NoneType
    :Side effect: mark the cell as containing a (hypothetic) bomb
    :UC: none
    :Examples:

    >>> cel = make()
    >>> is_hypothetic_bomb(cel)
    False
    >>> set_hypothetic(cel)
    >>> is_hypothetic_bomb(cel)
    True
    """
    if not is_revealed(cell):
        cell['hypothetic_bomb'] = True

def unset_hypothetic(cell):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :return: None
    :rtype: NoneType
    :Side effect: unmark the cell as containing a (hypothetic) bomb
    :UC: none
    :Examples:

    >>> cel = make()
    >>> is_hypothetic_bomb(cel)
    False
    >>> set_hypothetic(cel)
    >>> is_hypothetic_bomb(cel)
    True
    >>> unset_hypothetic(cel)
    >>> is_hypothetic_bomb(cel)
    False
    """
    if not is_revealed(cell):
        cell['hypothetic_bomb'] = False

def set_number_of_bombs_in_neighborhood(cell, nb_bombs):
    """
    :param cell: a cell of a minesweeper's grid
    :type cell: cell
    :param nb_bombs: the number of bombs in the neighborhood of cell
    :type nb_bombs: int
    :return: None
    :rtype: NoneType
    :Side effect: set the number bombs in the neighborhood of cell eqauls to nb_bombs
    :UC: nb_bombs must be >= 0
    :Examples:

    >>> cel = make()
    >>> set_number_of_bombs_in_neighborhood(cel, 4)
    >>> number_of_bombs_in_neighborhood(cel)
    4
    """
    assert nb_bombs >= 0, 'number of bombs must be >= 0.'
    cell['nbombs_neighborhood'] = nb_bombs

if __name__ == '__main__':
    import doctest
    doctest.testmod()
