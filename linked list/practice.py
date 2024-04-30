"""
[] -> [] -> * (None)
Create an ArrayList object that supports:
1. Appending
2. Printing whole list
3. [Extra] Printing whole list in reverse
"""


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        pass

    def append(self, data):
        # Insert an element at the end of the list

        # New node
        node = Node(data=data, next=None)

        if not self.head:
            self.head = node
            return

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = node

    def print_list(self):
        # Prints list in order
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def print_list_in_reverse(self, node=None):
        # Prints list in reverse

        # Naive solution
        # if node is None:
        #     # First node
        #     node = self.head
        #     if node.next is None:
        #         print(node.data)
        #     else:
        #         self.print_list_in_reverse(node.next)
        #         print(node.data)
        # else:
        #     if node.next is None:
        #         # Last node
        #         print(node.data)
        #     else:
        #         # Middle node
        #         self.print_list_in_reverse(node.next)
        #         print(node.data)

        # Optimized solution
        if node is None:
            # Called for first time
            node = self.head

            # Empty list case
            if node is None:
                return

        if node.next is None:
            print(node.data)
        else:
            self.print_list_in_reverse(node.next)
            print(node.data)


# TESTING

linked_list = LinkedList()
linked_list.append("1")
linked_list.append("2")
linked_list.append("3")
linked_list.append("4")
linked_list.append("5")

# linked_list.print_list()
linked_list.print_list_in_reverse()
