class Solution:
    def flatten(self, head):
        if not head:
            return head

        def dfs(node):
            curr = node
            last = node

            while curr:
                nxt = curr.next

                if curr.child:
                    child_head = curr.child
                    child_tail = dfs(child_head)

                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None

                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    last = child_tail
                else:
                    last = curr

                curr = nxt

            return last

        dfs(head)
        return head
