
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def display_list(self):

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
            
    
    def delete_duplicates(self):

        current = self.head

        while current:
            runner = current
            # Check until runner.next is not None.
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    
