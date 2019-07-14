import datetime
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.value = None
        
    def PrintList(self):
        printvalue = self.value
        while printvalue is not None:
            print(printvalue.value)
            printvalue = printvalue.next
            
            
        def insertFirst(self, data):
            newNode = Node(data)
            newNode.next = self.value
            self.value = newNode
            
        def insertLast(self, data):
            newNode = Node(data)
            if self.value is None:
                self.value = newNode
                return
            temp = self.value
            while(temp.next):
                temp = temp.next
            temp.next = newNode
            
        def InsertInBetween(self, mid, data):
            if mid is None:
                print("No Node Available")
                return
            newNode = Node(data)
            newNode.next = mid.next
            mid.next = newNode
            
        def delete(self, nodevalue):
            removevalue = self.value
            if removevalue is not None:
                if removevalue.value is nodevalue:
                    self.value = removevalue.next
                    removevalue = None
                    return
                while removevalue is not None:
                    if removevalue.value == nodevalue:
                        break
                    prev = removevalue
                    removevalue = removevalue.next
                    
                    if removevalue is None:
                        return
                    
                    prev.next = removevalue.next
                    removevalue= None
List1 = LinkedList()

List1.value = Node(datetime.datetime(2019, 6, 12))
data2 = Node(datetime.datetime(2019, 7, 12))
data3 = Node(datetime.datetime(2019, 8, 12))
data4 = Node(datetime.datetime(2019, 9, 12))
data5 = Node(datetime.datetime(2019, 7, 16))
List1.value.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
print(data2.value)
print(data2.next.value)
List1.insertFirst(datetime.datetime(2019, 1, 16))
List1.isertLast(datetime.datetime(2019, 12, 16))
List1.insertInBetween(data3, datetime.datetime(2020, 12, 16))
List1.insertInBetween(data2, datetime.datetime(2020, 12, 16))
List1.printList()
List1.delete(datetime.datetime(2020, 12 , 16))
List1.printList()

                    

