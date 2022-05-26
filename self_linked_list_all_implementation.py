from operator import ne


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self , value):
        new_node = Node(value)
        new_node.next=self.head
        self.head = new_node

    def insert_at_end(self , value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = Node(value)

    def insert_another_list(self , data_list):
        for i in data_list:
            self.insert_at_end(i)

    def length_of_linked_list(self):
        count=0
        current = self.head
        while(current):
            current = current.next
            count+=1
        return count

    def remove_an_element_at_a_given_index(self , index):
        if index<0 or index>self.length_of_linked_list():
            raise Exception("Invalid Index")
        if self.head is None:
            print("Linked List is Empty ")
        
        current = self.head
        i=1
        if index==1:
            self.head=current.next
        else:
            while(i!=index-1):
                current = current.next
                i+=1
            current.next=current.next.next
        
    def insert_at_a_given_index(self,value,index):
        if index<0 or index>self.length_of_linked_list():
            raise Exception("Invalid Index")
        current = self.head
        i=1
        if self.head:
            if index==1:
                self.insert_at_begining(value)
                # new_element=Node(value)
                # new_element.next=self.head
                # self.head=new_element
            else:
                while(i!=index-1):
                    current = current.next
                    i+=1
                new_element=Node(value)
                new_element.next=current.next
                current.next=new_element
                
    def insert_after_a_given_value(self,after_value,insert_value): 
        current = self.head
        if self.head:
            while(current.data != after_value):
                current = current.next
            new_element=Node(insert_value)
            new_element.next=current.next
            current.next=new_element

    def delete_by_value(self,value): 
        current = self.head
        if self.head:
            if self.head.data==value:
                self.head=current.next
            else:
                while(current.next.data != value):
                    current = current.next
                current.next=current.next.next

                     

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is Empty ")
            return
        current = self.head
        llist = ''
        while(current):
            llist+=str(current.data)+'-->'
            current=current.next
        print(llist)
if __name__=="__main__":
    ll = LinkedList()
    ll.insert_at_begining(3)
    ll.insert_at_begining(4)
    ll.print_linked_list()
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.print_linked_list()
    ll.insert_another_list(["Abhinav","Shonty"])
    ll.print_linked_list()
    print(ll.length_of_linked_list())
    ll.remove_an_element_at_a_given_index(2)
    ll.print_linked_list()
    print(ll.length_of_linked_list())
    ll.insert_at_a_given_index("ANkit",1)
    ll.print_linked_list()
    print(ll.length_of_linked_list())
    ll.insert_after_a_given_value("Shonty","Geek")
    ll.print_linked_list()
    print(ll.length_of_linked_list())
    ll.delete_by_value("chinki")
    ll.print_linked_list()
    print(ll.length_of_linked_list())




        
