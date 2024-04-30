# Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class My_linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # Move towards the end of the linked list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


linked_list = My_linkedlist()
linked_list.append("List weekdays from the start:")
linked_list.append("Monday")
linked_list.append("Tuesday")
linked_list.append("Wednesday")
linked_list.append("Thursday")
linked_list.append("Friday")
linked_list.print_list()

print(linked_list)

"""
Output:
Weekdays:
Monday
Tuesday
Wednesday
Thursday
Friday
"""

print()
print()
