#!/usr/bin/env python3
"""annotate the 'element_length function' """


from typing import Iterable, Sequence, List, Tuple


""" 'lst: Iterable[Sequence]': This indicates that the 'lst'
parameter is expected to be an iterable (e.g., a list) of sequences.
A "sequence" here means any iterable type, such as a string or a list."""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """ '-> List[Tuple[Sequence, int]]': This specifies that the function
    will return a list of tuples, where each tuple contains a sequence
    and an integer. In other words, the function returns a list of pairs,
    where the first element of each pair is a sequence from the input,
    nd the second element is the length of that sequence"""

    return [(i, len(i)) for i in lst]
