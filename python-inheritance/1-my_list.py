#!/usr/bin/python3
"""Defines an inherited list class MyList with a sorted print method.
"""


class MyList(list):
    """A custom list class that inherits from list and adds print_sorted."""

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Only works if all elements are integers.
        """
        if not all(isinstance(x, int) for x in self):
            raise TypeError("unorderable types: mixed or non-int elements found")
        print(sorted(self))
