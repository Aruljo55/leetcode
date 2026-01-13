class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}

    def _add_node_after(self, prev_node, new_node):
        nxt = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = nxt
        nxt.prev = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key not in self.key_to_node:
            if self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._add_node_after(self.head, node)
            node.keys.add(key)
            self.key_to_node[key] = node
        else:
            node = self.key_to_node[key]
            nxt_count = node.count + 1
            if node.next.count == nxt_count:
                nxt = node.next
            else:
                nxt = Node(nxt_count)
                self._add_node_after(node, nxt)
            nxt.keys.add(key)
            self.key_to_node[key] = nxt
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)

    def dec(self, key):
        node = self.key_to_node[key]
        if node.count == 1:
            del self.key_to_node[key]
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)
        else:
            prev_count = node.count - 1
            if node.prev.count == prev_count:
                prev = node.prev
            else:
                prev = Node(prev_count)
                self._add_node_after(node.prev, prev)
            prev.keys.add(key)
            self.key_to_node[key] = prev
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
