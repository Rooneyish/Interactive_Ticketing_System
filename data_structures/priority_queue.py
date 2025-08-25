class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self, item, priority):
        new_item = (priority, item)
        if self.is_empty():
            self.items.append(new_item)
        else:
            inserted = False
            for i in range(len(self.items)):
                if priority > self.items[i][0]:
                    self.items.insert(i, new_item)
                    inserted = True
                    break
                if not inserted:
                    self.items.append(new_item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[1] 
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[0][1]
        return None
    
    def size(self):
        return len(self.items)        
