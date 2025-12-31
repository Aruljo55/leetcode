class Solution:
    def maximumSum(self, nums):
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        digit_map = {}
        max_sum = -1
        
        for num in nums:
            d_sum = digit_sum(num)
            if d_sum in digit_map:
                max_sum = max(max_sum, num + digit_map[d_sum])
                digit_map[d_sum] = max(digit_map[d_sum], num)
            else:
                digit_map[d_sum] = num
        
        return max_sum
    
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2