class LinkedListNode:
    __slots__ = ['value', 'prev_node', 'next_node']
    def __init__(self, v, p, n):
        self.value = v
        self.prev_node = p
        self.next_node = n

class LinkedList:
    def __init__(self, items):
        first_node = None
        prev_node = None
        self.value_map = {}
        for item in items:
            node = LinkedListNode(item, prev_node, first_node)
            if first_node is None:
                first_node = node
            elif prev_node is not None:
                prev_node.next_node = node
            prev_node = node
            self.value_map[item] = node
        first_node.prev_node = node

    def value_after(self, value):
        node = self.value_map[value]
        return node.next_node.value

    def move(self, current):
        node = self.value_map[current]
        a = node.next_node
        b = a.next_node
        c = b.next_node
        tmp = c.next_node
        node.next_node = tmp
        tmp.prev_node = node

        destination = current
        while True:
            destination -= 1
            if destination == a.value:
                continue
            if destination == b.value:
                continue
            if destination == c.value:
                continue
            if destination < 1:
                destination = len(self.value_map) + 1
                continue
            break

        node = self.value_map[destination]
        tmp = node.next_node
        c.next_node = tmp
        tmp.prev_node = c
        node.next_node = a
        a.prev_node = node

        return self.value_after(current)

def part1(cups):
    current = cups[0]
    lst = LinkedList(cups)
    for i in range(100):
        current = lst.move(current)
    x = 1
    for _ in range(8):
        x = lst.value_after(x)
        print(x, end='')
    print()

def part2(cups):
    def _iterator():
        for cup in cups:
            yield cup
        for i in range(10, 1000001):
            yield i
    current = cups[0]
    lst = LinkedList(_iterator())
    for i in range(10000000):
        current = lst.move(current)
    a = lst.value_after(1)
    b = lst.value_after(a)
    print(a * b)

cups = [int(c) for c in '643719258']
part1(cups)
part2(cups)
