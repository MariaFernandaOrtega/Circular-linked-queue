# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:53 2023


@author: MariaFernandaOrtega
"""


class CircularQueue:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self.head.element

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        element = self.head.element
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return element

    def enqueue(self, element):
        new_node = self.Node(element)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
        self.size += 1

    def rotate(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        self.tail = self.head
        self.head = self.head.next
