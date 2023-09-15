#!/usr/bin/env python3
"""a type-annotated function 'sum_mixed_list' """


from typing import List, Union


"""mxd_lst: List'[Union[int, float]]' indicates that the parameter 'mxd_lst'
is expected to be a list containing 
elements that can be either integers '(int)'
or floats '(float)'. We use the 'Union' type hint to specify that
the list can contain elements of either type."""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    
    """-> float indicates that the function is expected to return a
    float, which is the sum of the elements in the mixed list."""

    return sum(mxd_lst)
