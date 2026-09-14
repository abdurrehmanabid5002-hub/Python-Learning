class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True

            current = current.next

        return False

    def delete(self, value):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted.")
            return

        current = self.head

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                print("Node deleted.")
                return

            current = current.next

        print("Value not found.")

    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


numbers = LinkedList()

while True:
    print("\nLinked List")
    print("1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Insert at Beginning")
    print("6. Reverse")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = int(input("Enter value: "))
        numbers.add(value)
        print("Value added.")

    elif choice == "2":
        numbers.display()

    elif choice == "3":
        value = int(input("Enter value to search: "))

        if numbers.search(value):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == "4":
        value = int(input("Enter value to delete: "))
        numbers.delete(value)

    elif choice == "5":
        value = int(input("Enter value: "))
        numbers.insert_at_beginning(value)
        print("Value added at beginning.")

    elif choice == "6":
        numbers.reverse()
        print("Linked list reversed.")

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")