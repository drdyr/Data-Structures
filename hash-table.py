# create node with next pointer for linked list chaining in case of hash collision

import random

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash(self, key):
        hash = 0
        for index, c in enumerate(key):
            hash += (index + len(key)) ** ord(c)
            hash = hash % self.capacity

        return hash


    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)

        node = self.table[index]

        # if this index of table is empty
        if node is None:
            self.table[index] = Node(key, value)
            return

        # if collision iterate to last node in the linked list at the index
        trav = node
        while trav.next:
            trav = trav.next

        trav.next = Node(key, value)

    def find(self, key):
        # calculate hash
        index = self.hash(key)
        trav = self.table[index]

        while trav:
            if trav.key == key:
                return trav.value

        return None

