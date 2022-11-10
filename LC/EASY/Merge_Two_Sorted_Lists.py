# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode() #here we are creating a dummy of the type list node
        tail = dummy #also we are pointing tail to the dummy
        while list1 and list2: # now we are iterating through both lists until one of them becomes null
            if list1.val<list2.val: #if value of list 1 is smaller 
                tail.next=list1 #we assign that node to the next of tail
                list1 = list1.next #then we move the list1 pointer ot next
            else:
                tail.next=list2 #else we assign list2 node to the next of tail
                list2 = list2.next #then we move the list2 pointer ot next
            tail = tail.next #in either case we move the tail pointer to next
        if list1: # if list 2 gets null and list 1 still has elements , the we simply put remaining ele in tail.next since they are already in sort
            tail.next=list1
        else:
            tail.next=list2 # if list 1 gets null and list 2 still has elements , the we simply put remaining ele in tail.next since they are already in sort
        return dummy.next # then we return the head of dummy
