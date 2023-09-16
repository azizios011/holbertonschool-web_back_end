#!/usr/bin/env python3
"""a type-annotated function 'make_multiplier' """


from typing import Callable


""" 'multiplier: float' indicates that the parameter
'multiplier' is expected to be a float."""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ '-> Callable[[float], float]' indicates that the function returns
    a callable object (a function) that takes a float as an argument and
    returns a float."""
    def multiplier_function(x: float) -> float:
        """Inside the 'make_multiplier' function, a nested function
        'multiplier_function' is defined. This function takes a float 'x'
        as an argument and returns the result of multiplying 'x' by the
        'multiplier' specified when 'make_multiplier' is called."""
        return x * multiplier
    return multiplier_function
