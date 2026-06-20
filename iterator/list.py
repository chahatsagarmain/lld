from __future__ import annotations
from iterator import IntIterator


class ListIterator(IntIterator):
    """
    Concrete Iterator implementation for a Python list.

    Traverses elements of a standard list sequentially.
    """

    def __init__(self, ls: list[int]) -> None:
        """
        Initialize the ListIterator with a list of integers.

        Args:
            ls (list[int]): The list of integers to iterate over.
        """
        self._ls = ls
        self._pos = 0

    def has_next(self) -> bool:
        """
        Check if the pointer is within the bounds of the list.

        Returns:
            bool: True if there is a next element, False otherwise.
        """
        return self._pos < len(self._ls)

    def next(self) -> int | None:
        """
        Return the next element in the list and advance the pointer.

        Returns:
            int | None: The next integer, or None if iteration is complete.
        """
        if self.has_next():
            val = self._ls[self._pos]
            self._pos += 1
            return val
        return None
