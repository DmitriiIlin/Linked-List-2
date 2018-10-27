import unittest
import random
class Node_2():
    # Инициализация э-та двунаправленного списка
    def __init__(self,v):
        self.value=v
        self.prev=None
        self.next=None

class Linked_List_2:
    # Инициализация двунаправленного списка
    def __init__(self):
        self.tail=None
        self.head=None

    def add_in_tail(self,item):
        # Метод добавления э-та в конец двунаправленного списка
        if self.head is None:
            self.head=item
            item.prev=None
            item.next=None
        else:
            self.tail.next=item
            item.prev=self.tail
        self.tail=item

    def print_all_nodes(self):
        # Метод класса L_L_2, позволяющий вывести э-ты L_L_2 
        node=self.head
        while node!=None:
            print(node.value,'Output by print all nodes')
            node=node.next

    def lenght_list(self):
        # Метод класса LL, расчитывающий кол-во э-в класса Node в LL (длина LL)
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l 

    def find_node_2(self,val):
        #Метод, ищет элемент со значением val в LL
        result=None
        node=self.head
        l=0
        while node is not None:
            l+=1
            if node.value==val:
                result=l
                break
            node=node.next
        return result         

    def delete_node(self,val,parametr=1):
        # Метод удаляет узел из списка по значению узла
        node = self.head
        data_Node_2=self.find_node_2(val)
        if data_Node_2 is None:
            print("Linked list doesnt have this Node")
        else:    
            lenght_LL=self.lenght_list()
            while node is not None:
                if (data_Node_2==1):
                    new_head=node.next
                    node.prev=None
                    self.head=new_head
                    parametr=1
                    if parametr==1:
                        break
                elif (data_Node_2==lenght_LL):
                    parametr=1
                    self.tail=self.tail.prev
                    self.tail.next=None
                    if parametr==1:
                        break 
                elif (node.value == val):
                    parametr=1  
                    node_pr=node.prev
                    node_next=node.next
                    node_pr.next=node.next
                    node_next.prev=node_pr.value
                    if parametr==1:
                        break
                node=node.next 

    def insert_node(self,number,val):
        # Метод класса LL позволяющий вставить э-т Node в LL, после э-та number
        count_iteration=self.lenght_list()
        if self.head==None:
            self.tail=self.head=Node_2(val)
        elif number==0:
            new_node=Node_2(val)
            new_node.next=self.head
            self.head=new_node
        elif number>=count_iteration:
            new_node=Node_2(val)
            new_node.next=None
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        else:
            curr_node=self.head
            count=1
            while curr_node != None:
                if count==number:
                    new_node=Node_2(val)
                    next_node=curr_node.next
                    new_node.next=next_node
                    new_node.prev=curr_node
                    curr_node.next=new_node
                    break
                count+=1    
                curr_node=curr_node.next

def initial_data_for_test():
    Values_for_Linked_lists=[]
    Qty=10
    for i in range(0,Qty):
        Value_for_Linked_List=random.randint(0,100000)
        Values_for_Linked_lists.append(Value_for_Linked_List)
    return Values_for_Linked_lists

def value_for_delete(initial_data_for_test):
    number_for_delete=random.randint(0,len(initial_data_for_test))
    value_for_delete=initial_data_for_test[number_for_delete]
    return value_for_delete

def value_for_add():
    Value=random.randint(0,1000000)
    return Value   

def data_after_delete(initial_data_for_test,value_for_delete_2):
    initial_data_for_test.remove(value_for_delete_2)
    return initial_data_for_test

def number(initial_data_for_test):
    N=random.randint(0,len(initial_data_for_test)-1)
    return N

def data_after_insert(initial_data_for_test,N,Value):
    initial_data_for_test.insert(N,Value)
    return initial_data_for_test

class Linked_List_2_Tests(unittest.TestCase):

    def test_delete(self):
         #Тест проверяет работу метода удаления узла из связанного списка
        self.first_list=Linked_List_2()
        self.second_list=Linked_List_2() 
        data_for_first_list=initial_data_for_test()
        data_for_delete=value_for_delete(data_for_first_list)
        for i in range(0, len(data_for_first_list)):
            Linked_List_2_item=Node_2(data_for_first_list[i])
            self.first_list.add_in_tail(Linked_List_2_item)
        self.first_list.delete_node(data_for_delete)
        data_for_list_after_delete=data_after_delete(data_for_first_list,data_for_delete)
        for i in range(0, len(data_for_list_after_delete)):
            Linked_List_2_item=Node_2(data_for_first_list[i])
            self.second_list.add_in_tail(Linked_List_2_item)
        node_1=self.first_list.head
        node_2=self.second_list.head
        for i in range (0,len(data_for_list_after_delete)):
            self.assertEqual(node_1.value, node_2.value)
            node_1=node_1.next
            node_2=node_2.next 
  
    def test_insert(self):
        #Тест проверяет работу метода вставки узла
        self.first_list=Linked_List_2()
        self.second_list=Linked_List_2() 
        data_for_first_list=initial_data_for_test() 
        value_to_add=value_for_add()
        number_for_insert=number(data_for_first_list)
        for i in range(0, len(data_for_first_list)):
            Linked_List_2_item=Node_2(data_for_first_list[i])
            self.first_list.add_in_tail(Linked_List_2_item)     
        self.first_list.insert_node(number_for_insert,value_to_add)
        inserted_data=data_after_insert(data_for_first_list,number_for_insert,value_to_add)
        for i in range(0, len(inserted_data)):
            Linked_List_2_item=Node_2(inserted_data[i])
            self.second_list.add_in_tail(Linked_List_2_item)    
        node_1=self.first_list.head
        node_2=self.second_list.head
        for i in range (0,len(inserted_data)):
            self.assertEqual(node_1.value, node_2.value)
            node_1=node_1.next
            node_2=node_2.next         

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()

