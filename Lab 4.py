#Question 1 
#Implementation of Stack

print("===============================================================================")
class Stack:
    def __init__(self):
        self.values = []

    def pop(self):
        if self.isempty():
            return None
        return self.values.pop()
        #return self.values.pop(0)

    def push(self, item):
        self.values.append(item)
        #self.values = [item] + self.values

    def isempty(self):
        return len(self.values) == 0

    def peek(self):
        if self.isempty():
            return None
        return self.values[-1]

    def size(self):
        return len(self.values)

    def __str__(self):
        return str(self.values)


st = Stack()
print("Is stack empty?", st.isempty()) 
st.push("Abdulah")
st.push("Age : 20")
st.push(33)
st.push("Computer Network")
print("Is stack empty?", st.isempty()) 
print("Size of stack is:", st.size())
print("Top of stack is:", st.peek())
print("Stack is:", st)
print("Popped : ",st.pop())
print("Popped : ",st.pop())

print("Top of stack is:", st.peek())
print("Stack is:", st)

print("===============================================================================")

#Question 2 
#Implementation of Queue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


q = Queue()
print("Is queue empty?", q.is_empty()) 

q.enqueue("Asadulllah")
q.enqueue("Age : 20")
q.enqueue(1400)
q.enqueue("Fashion Designer")

print("Is queue empty?", q.is_empty()) 
print("Size of queue is:", q.size())
print("Peek of queue is:", q.peek())
print("Queue is:", q)

print("Dequeued : ",q.dequeue())
print("Dequeued : ",q.dequeue())

print("Peek of queue is:", q.peek())
print("Queue is:", q)

print("===============================================================================")

#Question 3 
#Binary search
#Iterative method

def find(start, end, val, list):
    while start <= end:
        mid = (start + end) // 2
        if val == list[mid]:
            return mid
        elif val > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.")

#recursive method
""" def find(start, end, val, list):
    if start > end:
        return -1
    mid = (start + end) // 2
    if val == list[mid]:
        return mid
    elif val > list[mid]:
        return find(mid + 1, end, val, list)
    else:
        return find(start, mid - 1, val, list)

list = [1, 2, 3, 4, 5, 6, 7, 8]
start = 0
end = len(list) - 1
val = int(input("Enter value to find: "))
index = find(start, end, val, list)

if index != -1:
    print(f"Value found at Index: {index}")
else:
    print("Value not found in the list.") """

print("===============================================================================")
