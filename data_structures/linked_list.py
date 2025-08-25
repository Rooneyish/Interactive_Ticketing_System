class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        if not self.head:
            self.head = new_element
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_element

    def insert(self, new_element, position):
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return

        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        if current:
            new_element.next = current.next
            current.next = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_position(self, position):
        current = self.head
        count = 1
        while current and count <= position:
            if count == position:
                return current
            current = current.next
            count += 1
        return None

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            self.head = previous

    # Function for Task 8
    def to_list(self):
        python_list = []
        current = self.head
        while current:
            python_list.append(current.value)
            current = current.next
        return python_list

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))
