#https://leetcode.com/problems/add-two-numbers/description/
                return head
            l1 = l1.next
        
        return head
# while both -> sum and handle co
# while no longer both -> append l2 to l1 if l2 is longer
# while l1 -> handle sum and co
# while co -> handle co
                l1.next = l2.next
                l1 = l1.next
                break
            if not l1.next and not l2.next and co:
                l1.next = ListNode(co)
                return head
            l1 = l1.next
            l2 = l2.next
        while l1 and co:
            val = co + l1.val
            l1.val = val % 10
            co = val // 10
            if not l1.next and co:
                l1.next = ListNode(co)