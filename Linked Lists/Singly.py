class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion Form The Begin ==========================
    def insertAtBegin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    # Insertion From The End ==========================
    def insertAtEnd(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newnode
        temp = newnode

    # Insertion From The Position ============================
    def insertPosi(self, posi, data):
        _len = self.getLen()
        if posi >= _len:
            print("Invalid Position")

        elif posi == 0:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

        else:
            newnode = Node(data)
            temp = self.head
            i = 0
            while i < posi-1:
                i += 1
                temp = temp.next

            newnode.next = temp.next
            temp.next = newnode

    # Deletion By The Key ===============================
    def deleteKey(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        prev = self.head
        while temp is not None:
            if temp.data == key:
                break

            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    # Get Length Function ==============================
    def getLen(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    # Display ==================================
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ =='__main__':
    # Start with the empty list
    l_list = LinkedList()

    # Insert 10, 20 at begin
    l_list.insertAtBegin(10)
    l_list.insertAtBegin(20)

    # Insert 30, 40 at end
    l_list.insertAtEnd(30)
    l_list.insertAtEnd(40)

    # Insert 50, 60 at 2, 1 position
    l_list.insertPosi(2, 50)
    l_list.insertPosi(1, 60)

    # Delete 10, 20
    l_list.deleteKey(10)
    l_list.deleteKey(20)

    # Display
    print("Linked List = ", end=" ")
    l_list.display()








