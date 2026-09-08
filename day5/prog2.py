from collections import deque

class Node:
    def __init__(self, start: int = -1, end: int = -1):
        self.start = start
        self.end = end
        self.prev = None
        self.next = None

    def merge(self, other: "Node"):
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)

def main():
    head = Node()
    tail = Node(float("inf"), float("inf"))
    head.next, tail.prev = tail, head

    def addRange(start: int, end: int):
        new_node = Node(start, end)
        if head.next.next is None:
            tail.prev = new_node
            new_node.next = tail
            head.next = new_node
            new_node.prev = head
            return


        node = head.next
        while node:
            if node.end < start:
                node = node.next
                continue
            
            if node.start > end:
                node.prev.next, new_node.prev = new_node, node.prev
                node.prev, new_node.next = new_node, node
                return

            if node.start < new_node.start:
                new_node.start = node.start
            if node.end > new_node.end:
                new_node.end = node.end

            node.prev.next, node.next.prev = node.next, node.prev
            node = node.next

    with open("input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                break
            start, end = line.split("-")
            addRange(int(start), int(end))

    fresh_ingridients_ids_amount = 0
    node = head.next
    while node.next:
        fresh_ingridients_ids_amount += node.end - node.start + 1
        node = node.next
    print(fresh_ingridients_ids_amount)
                

if __name__ == "__main__":
    main()