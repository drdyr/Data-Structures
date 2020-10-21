class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.root
        self.root = new_node

    def print(self):
        if not self.root:
            return
        res = ""
        cur = self.root
        res += str(cur.value) + "->"

        while cur.next:
            cur = cur.next
            res += str(cur.value) + "->"

        res += "None"

        return res

    def delete(self, value):
        temp = self.root

        if temp and temp.value == value:
            self.root = temp.next
            return

        while temp:
            if temp.value == value:
                break
            prev = temp
            temp = temp.next

        if not temp:    #  if key was not present
            return

        prev.next = temp.next

        temp = None



lol = LinkedList()

lol.insert(5)
lol.insert(3)
lol.insert(4)
lol.insert(7)

print(lol.print())