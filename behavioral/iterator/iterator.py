from __future__ import annotations
from abc import ABC, abstractmethod


class IntIterator(ABC):
    """
    Abstract Base Class (Interface) for an Integer Iterator.

    Defines the contract for iterating over a collection of integers.
    This demonstrates the classic Iterator pattern with has_next() and next().
    """

    @abstractmethod
    def has_next(self) -> bool:
        """
        Check if there are more elements in the collection to traverse.

        Returns:
            bool: True if the collection has more elements, False otherwise.
        """
        pass

    @abstractmethod
    def next(self) -> int | None:
        """
        Retrieve the next integer in the collection.

        Returns:
            int | None: The next integer in the iteration, or None if the end is reached.
        """
        pass