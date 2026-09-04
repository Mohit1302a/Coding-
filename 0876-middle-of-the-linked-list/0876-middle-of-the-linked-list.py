class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=[]

        while head:
            node.append(head)
            head=head.next
        return node[len(node)//2]