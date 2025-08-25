class Element:
    def __init__(self, action, ticket_id = None, new_ticket=None, old_ticket= None):
        self.action= action
        self.ticket_id = ticket_id
        self.new_ticket = new_ticket
        self.old_ticket = old_ticket
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

    def delete(self, ticket_id):
        current = self.head
        previous = None
        while current:
            if current.ticket_id == ticket_id:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    def find(self, ticket_id):
        current = self.head
        while current:
            if current.ticket_id == ticket_id:
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

    def to_list(self):
        python_list = []
        current = self.head
        while current:
            python_list.append(current.value)
            current = current.next
        return python_list

    def display_history(self):
        if not self.head:
            print("No ticket history found.")
            return
        
        current = self.head
        print("\n===== Ticket History =====")
        while current:
            print(f"Ticket ID: {current.ticket_id} | Action: {current.action} | Details: {current.details}")
            current = current.next
        print("==========================\n")
