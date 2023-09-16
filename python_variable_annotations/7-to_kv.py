#!/usr/bin/env python3
"""a type-annotated function 'to_kv' """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ 'k: str' indicates that the first parameter,
    'k', is expected to be a string.

    'v: Union[int, float]' uses the Union type hint to specify that the second
    parameter, 'v', can be either an integer '(int)' or a float '(float)'.

    '-> Tuple[str, float]' indicates that the
    function returns a tuple containing a string and a float."""
    return (k, float(v ** 2))
