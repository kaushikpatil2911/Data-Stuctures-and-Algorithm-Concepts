class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node.next == self.head:
                break
            result += ' -> '
        return result       

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail.next = self.head
            self.tail = new_node    
        self.length += 1       


csll = CSLL()
print(csll)
print(csll.head)
print(csll.tail)
print(csll.length)
print("----------------")
csll.append(10)
csll.append(20)
csll.append(30)
print(csll)
print(csll.head)
print(csll.tail)
print(csll.length)
print("----------------")

# Time Complexity -> O(1)
# Space Complexity -> O(1)