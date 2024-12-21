from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Initialize a min-heap
        min_heap = []
        
        # Add the head of each list to the min-heap
        for idx, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, idx, node))
        
        # Create a dummy node to help build the result linked list
        dummy = ListNode()
        current = dummy
        
        # While there are elements in the heap
        while min_heap:
            # Pop the smallest element from the heap
            val, idx, node = heappop(min_heap)
            # Add this node to the result
            current.next = node
            current = current.next
            
            # If there is a next node in the list, push it to the heap
            if node.next:
                heappush(min_heap, (node.next.val, idx, node.next))
        
        # Return the head of the merged list
        return dummy.next
