https://leetcode.com/problems/add-two-numbers/
2. Add Two Numbers

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f=""
        s=""
        while l1:
            f+=str(l1.val)
            l1=l1.next
        while l2:
            s+=str(l2.val)
            l2=l2.next
        ans = str(int(f[::-1])+int(s[::-1]))
        l3=cur=ListNode()
        for i in ans[::-1]:
            a = ListNode(int(i))
            l3.next=a
            l3=l3.next
        return cur.next
