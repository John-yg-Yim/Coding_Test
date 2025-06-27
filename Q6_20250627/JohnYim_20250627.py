# 노드 정의
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 클래스
class Solution:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.head1 = self.list2linked(self.list1)
        self.head2 = self.list2linked(self.list2)

    def list2linked(self, arr):
        dummy = ListNode()
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    def merge2lists(self):
        dummy = ListNode()
        curr = dummy
        l1, l2 = self.head1, self.head2

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next

    def printlinkedlist(self, head):
        result = []
        while head:
            result.append(str(head.val))
            head = head.next
        print(",".join(result) if result else "Empty")

# main 함수
def main():
    ex1_list1, ex1_list2 = [1, 2, 4], [1, 3, 4]
    ex2_list1, ex2_list2 = [], []
    ex3_list1, ex3_list2 = [], [0]

    print("Example 1:")
    sol1 = Solution(ex1_list1, ex1_list2)
    merged1 = sol1.merge2lists()
    sol1.printlinkedlist(merged1)

    print("\nExample 2:")
    sol2 = Solution(ex2_list1, ex2_list2)
    merged2 = sol2.merge2lists()
    sol2.printlinkedlist(merged2)

    print("\nExample 3:")
    sol3 = Solution(ex3_list1, ex3_list2)
    merged3 = sol3.merge2lists()
    sol3.printlinkedlist(merged3)

# 엔트리 포인트
if __name__ == "__main__":
    main()