class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedChain:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def getLength(self):
        return self.length

    def _getNode(self, pos):
        if pos < 1 or pos > self.length:
            return None
        current = self.head
        for _ in range(pos - 1):
            current = current.next
        return current

    def retrieve(self, pos):
    	node = self._getNode(pos)
    	if node is None:
        	return False, False
    	return node.value, True

    def insert(self, pos, item):
        if pos < 1 or pos > self.length + 1:
            return False

        new_node = Node(item)

        if self.isEmpty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node

        elif pos == 1:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

        else:
            prev_node = self._getNode(pos - 1)
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = next_node
            next_node.prev = new_node

        self.length += 1
        return True

    def delete(self, pos):
        if pos < 1 or pos > self.length:
            return False

        if self.length == 1:
            self.head = None

        else:
            node = self._getNode(pos)
            node.prev.next = node.next
            node.next.prev = node.prev
            if pos == 1:
                self.head = node.next

        self.length -= 1
        return True

    def save(self):
    	result = []

    	if self.isEmpty():
        	return result

    	current = self.head
    	for _ in range(self.length):
        	result.append(current.value)
        	current = current.next

    	return result

    def load(self, lst):
        self.head = None
        self.length = 0
        for i, item in enumerate(lst, start=1):
            self.insert(i, item)