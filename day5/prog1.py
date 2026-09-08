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

    def isInRange(val: int):
        node = head.next
        while node.next:
            if node.start > val:
                return False
            if node.start <= val <= node.end:
                return True
            node = node.next
        return False

    fresh_ingridients_amount = 0
    with open("input.txt", "r", encoding="utf8") as f:
        ranges_reading = True
        for line in f.readlines():
            line = line.strip()
            if ranges_reading:
                if not line:
                    ranges_reading = False
                    continue
                start, end = line.split("-")
                addRange(int(start), int(end))
            
            else:
                if isInRange(int(line)):
                    fresh_ingridients_amount += 1

    print(fresh_ingridients_amount)
                

if __name__ == "__main__":
    main()