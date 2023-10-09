#!/usr/bin/env python3
# The types of the elements of the input are not known
from typing import List


def safe_first_element(lst) -> List:
    if lst:
        return lst[0]
    else:
        return None
