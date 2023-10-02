#!/usr/bin/env python3
"""class server"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """A method named get_page that takes two integer arguments page
        with default value 1 and page_size with default value 10."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_pages = math.ceil(len(self.dataset()) / page_size)

        if 1 <= page <= total_pages:
            start, end = self.index_range(page, page_size)
            new = self.dataset()[start:end]
            return new
        else:
            return []

    def index_range(self, page: int, page_size: int) -> tuple:
        """Calculate the start and end indices for pagination."""
        start = (page - 1) * page_size
        end = start + page_size
        return start, end

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        hypermedia_info = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        return hypermedia_info
