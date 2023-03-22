'''1)Data structures:
stack-LIFO,FILO
Queue-FIFO,LILO
Linked list,
Double Linked list,
Trees,
Graphs
2)Searching and Sorting Algos:
Linear Search,
Binary search '''


class Stack:

    def __init__(self):
        self.arr = []
        self.size = 5

    def stack_push(self, element):
        if len(self.arr) == self.size:
            print("stack is Full")
        else:
            self.arr.append(element)

    def stack_pop(self):
        if len(self.arr) == 0:
            print("underflow: stack empty")
        else:
            self.arr.pop()

    def stack_peek(self):
        if len(self.arr) == 0:
            return "stack is empty"
        return self.arr[-1]

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False


s = Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
s.stack_push(50)
print(s.arr)
s2 = Stack()
s2.stack_push(s.stack_pop())
s2.stack_push(s.stack_pop())
s2.stack_push(s.stack_pop())
s2.stack_push(s.stack_pop())
s2.stack_push(s.stack_pop())
print(s2.arr)
'''#print(s.arr)
#s.stack_peek()
#print(s.arr)
s.stack_pop()
s.stack_pop()
s.stack_pop()
print(s.arr)


""" *************** QUEUE *************"""
class Queue:
    arr = []
    size = 5
    def queue_push(self,element):
        if len(self.arr)==self.size:
            print("stack is Full")
        else:
            self.arr.append(element)
    def queue_pop(self):
        if len(self.arr)==0:
            print("underflow: stack empty")
        else:
            self.arr.pop(0)
    def queue_peak(self):
        if len(self.arr)==0:
            return "stack is empty"
        return self.arr[-1]
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False
s=Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
s.stack_push(50)
print(s.arr)
#print(s.arr)
s.stack_pop()
s.stack_pop()
s.stack_pop()
print(s.arr)'''


class queue:
    def __init__(self):
        self.temp = []
        self.original = []

    def enqueue(self, ele):
        self.original.append(ele)

    def dequeue(self):
        return self.original.pop(0)

    def printQueue(self):
        print("Temp: ", self.temp)
        print("original: ", self.original)
        '''queue thoungh stack'''


''''class queue:
    def __init__(self):
        self.temp=[]
        self.original=[]
    def enqueue(self,ele):
        self.temp.append(ele) #step1
        while len(self.original) !=0: #step2
            pop_ele = self.original.pop(0)
    def dequeue(self):
        return self.original.pop(0)
    def printQueue(self):
        print("Temp: ",self.temp)
        print("original: ",self.original) '''


class queue:
    def __init__(self):
        self.temp = []
        self.original = []

    def enqueue(self, ele):
        self.original.append(ele)

    def dequeue(self):
        return self.original.pop(0)

    def printQueue(self):
        print("Temp: ", self.temp)
        print("original: ", self.original)
        '''queue thoungh stack'''


''''class queue:
    def __init__(self):
        self.temp=[]
        self.original=[]
    def enqueue(self,ele):
        self.temp.append(ele) #step1
        while len(self.original) !=0: #step2
            pop_ele = self.original.pop(0)
    def dequeue(self):
        return self.original.pop(0)
    def printQueue(self):
        print("Temp: ",self.temp)
        print("original: ",self.original) '''


class queue:
    def __init__(self):
        self.temp = []
        self.original = []

    def enqueue(self, ele):
        self.temp.append(ele)  # step1
        while len(self.original) != 0:  # step2
            pop_ele = self.original.pop(0)

    def dequeue(self):
        return self.original.pop(0)

    def printQueue(self):
        print("Temp: ", self.temp)
        print("original: ", self.original)


class queue:
    def __init__(self):
        self.temp = []
        self.original = []

    def enqueue(self):
        pass

    def dequeue(self):
        pass

    def printQueue(self):
        print("Temp: ", self.temp)
        print("original: ", self.original)

    temp = []


ori = [5, 4, 3, 2, 1]

5, 4, 3, 2, 1













