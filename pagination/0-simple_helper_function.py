#!/usr/bin/env python3
"""a function named 'index_range' that takes two
integer arguments 'page' and 'page_size'."""


def index_range(page, page_size):
    """Calculate the start index"""
    start_index = (page - 1) * page_size
    """Calculate the end index"""
    end_indew = start_index + page_size
    """Return a tuple of start and end"""
    return (start_index, end_indew)
