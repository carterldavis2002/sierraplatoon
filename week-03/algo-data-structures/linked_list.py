class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList():
    def __init__(self, head=None):
        self.head = head
        self.length = 0 if head == None else 1

    def add(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            search = self.head
            while search.next != None:
                search = search.next

            search.next = node

        self.length += 1

    def remove(self, data):
        search = self.head
        if search == None:
            return;

        if search.val == data:
            self.head = search.next
            search = None
            return
        
        prev = None
        while search != None:
            if search.val == data:
                break

            prev = search
            search = search.next

        if search == None:
            return

        prev.next = search.next
        search = None
        self.length -= 1

    def get(self, element):
    # write you code to GET and return an element from the Linked List
        pass

ll = LinkList()
ll.add(5)
ll.add(6)
ll.remove(5)
print(ll.head.val)