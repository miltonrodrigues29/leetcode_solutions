class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
           
        second = slow.next
        prev = slow.next = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        
        first,second = head, prev
        # because second half is shorter than the first half
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2