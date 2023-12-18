# linked_list.py


class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Cell(None)
        global count
        count = 0

    def insert(self, value):
        global count
        front = self.head
        rear = front.next
        if count > 2 :
            i = 0
            while i in range(2):
                front = rear
                rear = rear.next
                i+=1
        else :
            while rear :
                front = rear
                rear = rear.next

        #while rear and value > rear.value:
        #    
        #    front = rear
        #    rear = rear.next
        cell = Cell(value)
        cell.next = rear
        front.next = cell
        count += 1

    def delete(self, value):
        front = self.head
        rear = front.next
        while rear:
            if rear.value == value:
                break
            front = rear
            rear = rear.next
        if not rear:
            print("[*] Data not found")
            return
        front.next = rear.next
        rear = None

    def show(self):
        tmp = self.head.next
        while tmp:
            print(tmp.value)
            tmp = tmp.next

l = LinkedList()
print('insert 3, 5, 1...')
l.insert(3)
l.insert(5)
l.insert(1)
l.insert(7)
l.insert(9)
l.insert(0)
print('print data')
l.show()
print('delete 3...')
l.delete(3)
print('print data')
l.show()