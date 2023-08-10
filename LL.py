class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList :
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None 
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
       
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None 
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next =  self.head
            self.head =  new_node
        self.length +=1
        return True    
    
    def pop_first(self):
        temp = self.head
        
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
             
        else:

            self.head = self.head.next
            temp.next = None
            self.length -=1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False 

    def insert(self,index, value):       
        if index < 0 or index >self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >self.length:
            return False
        if index == 0:
           return self.pop_first()
        if index == self.length-1:
            return self.pop()

        prev = self.get(index-1)
        temp =  prev.next
        prev.next = temp.next 
        temp.next = None
        self.length -= 1 
        return temp 

    def reverse(self):
       temp = self.head
       after = temp.next
       before = None
       self.head = self.tail
       self.tail = temp
       for _ in range(self.length):
           after = temp.next 
           temp.next = before
           before = temp
           temp = after
           
        

         

    # def insert(self,index, value):
    #     if index <0 or index >self.length:
    #         return False
    #     if index == 0:
    #         return self.prepend(value)
    #     if index == self.length:
    #         return self.append(value)
    #     temp = self.head
    #     post = self.head
    #     new_node = Node(value)
    #     for _ in range(index-1):
    #         temp = temp.next
    #         post = temp.next
    #     temp.next = new_node
    #     new_node.next = post
    #     self.length +=1
    #     return True

# my_linked_list = LinkedList(4)
# my_linked_list.append(3)
# my_linked_list.append(5)  
# my_linked_list.prepend(2)
# my_linked_list.print_list()

# print('-------------------------------------')
# # my_linked_list.pop_first()


# print(f'Length of my linked list is {my_linked_list.length}')

# # my_linked_list.pop_first()
# # my_linked_list.pop_first()
# # my_linked_list.pop_first()
# print('-------------------------------------')
# my_linked_list.print_list()

# print(f'Length of my linked list is {my_linked_list.length}')

# my_linked_list.insert(3,77)
# print('-------------------------------------')
# my_linked_list.print_list()

# my_linked_list.remove(3)
# print('-------------------------------------')
# my_linked_list.print_list()
