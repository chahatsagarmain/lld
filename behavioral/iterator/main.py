from linkedlist import LinkedList, LinkedListIterator
from list import ListIterator


def run_iterator_demo() -> None:
    # 1. Iterate over a standard Python list using custom ListIterator
    print("--- Demonstrating List Iterator ---")
    ls = [1, 2, 3, 4, 5]
    ls_iter = ListIterator(ls)
    while ls_iter.has_next():
        print(f"List element: {ls_iter.next()}")

    print("\n--- Demonstrating LinkedList Iterator ---")
    # 2. Populate a linked list
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)

    # Traverse the linked list using custom LinkedListIterator
    ll_iter = LinkedListIterator(ll)
    while ll_iter.has_next():
        print(f"LinkedList element: {ll_iter.next()}")


if __name__ == "__main__":
    run_iterator_demo()