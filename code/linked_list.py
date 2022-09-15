class LinkedList:
    """
    Defines class implementation of a linked list data structure with methods for prepending, appending, and inserting
    before and after a specified value
    """

    def __init__(self, collection=None):
        self.head = None
        self.size = 0
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)
        self.size += 1

    def pop(self):
        if self.head is not None:
            first_item = self.head
            self.head = self.head.next
            first_item.next = None
            self.size -= 1
            return first_item
        else:
            return False

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
        self.size += 1

    def insert_before(self, val, new_val):
        if len(self) == 0:
            raise TargetError
        elif self.head.value == val:
            self.head = Node(new_val, self.head)
            self.size += 1
        else:
            for node in self:
                if node.next and node.next.value == val:
                    node.next = Node(new_val, node.next)
                    self.size +=1
                    return
            raise TargetError

    def insert_after(self, val, new_val):
        for node in self:
            if node.value == val:
                node.next = Node(new_val, node.next)
                return
        raise TargetError

    def kth_from_end(self, k):
        if k >= len(self) or k < 0:
            raise TargetError
        return self[0]

    def sum_odd(self):
        odd_sum = 0
        for node in self:
            if node.value % 2 == 1:
                odd_sum += node.value
        return odd_sum

    def includes(self, value):
        for node in self:
            if node.value == value:
                return True
        return False

    def to_list(self):
        return [val for val in self]

    def __str__(self):
        output = ""
        for value in self:
            output += "{ " + str(value) + " } -> "
        output += "None"
        return output

    def __iter__(self):
        def values():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return values()

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError

        for i, node in enumerate(self):
            if i == index:
                return node

    def __eq__(self, other):
        return list(self) == list(other)

    def __bool__(self):
        return True


class Node:
    """
    Defines a class that behaves as the node for singly linked list
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class TargetError(Exception):
    pass

if __name__ == "__main__":

    foods = LinkedList(["apple","banana","cucumber"])

    first_food = foods[0]

    for food in foods:
        print(food)
