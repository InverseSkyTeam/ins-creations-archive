from typing import Optional

# #节点类(已作废)
# class Node:
#     def __init__(self,value,next=None):
#         self.next = next
#         self.val = value
#     def __str__(self):
#         return "Node{val="+str(self.val)+",next="+str(self.next)+"}"

i1 = -1


# 链表类
class ListNode:
    def __init__(self, *args, next=None) -> None:
        global i1

        # 节点
        if len(args) == 1 or len(args) == 2:
            self.val = args[0]
            self.next = next

        # 空链表
        elif len(args) == 0:
            self.val = None
            self.next = None
            self.head = None
            self.__node = []
            self.__values = []

        # 单向非循环链表
        else:
            self.__values = list(args)
            self.__node = []
            self.head = self.__get_node()
            i1 = -1
            next_node = self.head
            while next_node:
                self.__node.append(next_node)
                next_node = next_node.next
            self.val = self.__values[0]
            self.next = self.__node[1]

    # 就这个还有小bug
    def __len__(self) -> int:
        try:
            head = self.head
        except:
            return 1
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def __str__(self):
        try:
            if self.val == None and self.next.val == None:
                return "None"
        except:
            return "None"
        return 'ListNode{val:' + str(self.val) + ',next:' + str(self.next) + '}'

    def __get_node(self, i=None):
        global i1
        if i:
            i1 = i
        i1 += 1
        try:
            return ListNode(self.__values[i1], next=self.__get_node())
        except:
            return None

    def reverse(self):
        aux = ListNode()
        node = self.head
        while node:
            next = node.next
            node.next = aux.next
            aux.next = node
            node = next
        return aux.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        dum = head
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                head = head.next
                list1 = list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next
        head.next = list1 if list1 else list2
        return dum.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


print("众所周知:c++里有链表(struct)这个基本数据结构,而python却没有,所以我这边做了一个\n目前实现的是单项非循环链表")
print("这里用leetcode的21题和83题演示一下")
sol = Solution().mergeTwoLists(ListNode(1, 2, 4), ListNode(1, 3, 4))
print("\n第21题:合并两个有序链表")
print("网址:https://leetcode.cn/problems/merge-two-sorted-lists/")
print("输入:\nListNode(1,2,4) , ListNode(1,3,4)")
print("输出:")
print(sol)

sol = Solution().deleteDuplicates(ListNode(1, 2, 2, 3, 4, 4))
print("\n第83题:删除链表中的重复项")
print("网址:https://leetcode.cn/problems/remove-duplicates-from-sorted-list/")
print("输入:\nListNode(1,2,2,3,4,4)")
print("输出:")
print(sol)
print("点改编可以调整输入项")