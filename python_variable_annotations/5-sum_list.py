#!/usr/bin/env python3
"""a type-annotated function sum_list"""

from typing import List


""" 'input_list: List[float]' indicates that the function takes
a parameter 'input_list' that is expected to be a list of floats."""


def sum_list(input_list: List[float]) -> float:
    """ '-> float' indicates that the function is
    expected to return a float."""
    return sum(input_list)
