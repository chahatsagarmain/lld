from __future__ import annotations
from iterator import IntIterator


class Node:
    """
    A single node in a singly linked list.
    """

    def __init__(self, val: int, next_node: Node | None = None) -> None:
        """
        Initialize a list node with an integer value and optional pointer to the next node.

        Args:
            val (int): The integer value stored in the node.
            next_node (Node | None): The next node in the sequence. Defaults to None.
        """
        self.val = val
        self.next = next_node


class LinkedList:
    """
    A basic singly linked list structure that supports adding elements to the end.
    """

    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.front: Node | None = None
        self.back: Node | None = None

    def add_node(self, val: int) -> None:
        """
        Create a new node containing the value and append it to the end of the list.

        Args:
            val (int): The integer value to append.
        """
        node = Node(val)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            assert self.back is not None
            self.back.next = node
            self.back = node


class LinkedListIterator(IntIterator):
    """
    Concrete Iterator implementation for a LinkedList.

    Traverses the linked nodes sequentially starting from the head.
    """

    def __init__(self, ll: LinkedList) -> None:
        """
        Initialize the LinkedListIterator with a target LinkedList.

        Args:
            ll (LinkedList): The linked list to traverse.
        """
        self.pos = ll.front

    def has_next(self) -> bool:
        """
        Check if the current traversal pointer points to a valid node.

        Returns:
            bool: True if there is a node to visit, False otherwise.
        """
        return self.pos is not None

    def next(self) -> int | None:
        """
        Return the value of the current node and advance to the next node.

        Returns:
            int | None: The integer value, or None if the end of the list is reached.
        """
        if self.has_next():
            assert self.pos is not None
            val = self.pos.val
            self.pos = self.pos.next
            return val
        return None
