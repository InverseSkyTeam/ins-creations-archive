from typing import List,Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return 'TreeNode{val:' + str(self.val) + ',left:' + str(self.left) + ',right:' + str(self.right) + '}'
    def __reversed__(self):
        root = self.__root
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

class BinaryTree:
    def __init__(self,*args):
        self.__TreeNode = list(args)
        self.__root = self.__TreeNode[0] if self.__TreeNode else None
        print(self.__root)
        self.list = get_list(self.__root)



def isSameTree(p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
    if not p and q:
        return False
    elif p and not q:
        return False
    elif not p and not q:
        return True
    elif p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return []
    res += inorderTraversal(root.left)
    res.append(root.val)
    res += inorderTraversal(root.right)
    return res

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return []
    res.append(root.val)
    res += preorderTraversal(root.left)
    res += preorderTraversal(root.right)
    return res

def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return []
    res += postorderTraversal(root.left)
    res += postorderTraversal(root.right)
    res.append(root.val)
    return res

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root:
        res = [[root.val]]

        def order(nodel):
            qu = []
            qs = []
            for x in nodel:
                q = []
                qr = []
                if x.left:
                    q.append(x.left.val)
                    qr.append(x.left)
                if x.right:
                    q.append(x.right.val)
                    qr.append(x.right)
                if q:
                    qu += q
                if qr:
                    qs += qr
            if qu:
                res.append(qu)
                if qs:
                    order(qs)
                else:
                    return
            else:
                return

        order([root])
        return res
    else:
        return []
def get_list(root: Optional[TreeNode]) -> List[List[int]]:
    if root:
        res = [[root.val]]

        def order(nodel,res):
            qu = []
            qs = []
            for x in nodel:
                q = []
                qr = []
                if x.left:
                    q.append(x.left.val)
                    qr.append(x.left)
                if x.right:
                    q.append(x.right.val)
                    qr.append(x.right)
                if q:
                    qu += q
                if qr:
                    qs += qr
            if qu:
                res += qu
                if qs:
                    order(qs,res)
                else:
                    return
            else:
                return

        order([root],res)
        return res[0] + res[1:]
    else:
        return []
a = TreeNode(1,TreeNode(2))
# print(inorderTraversal(a))
# print(a)
print(BinaryTree(TreeNode(1,TreeNode(2)),TreeNode(2)).list)
# (255,255,255)
# (231,231,230)
# (180,199,231)
# (197,224,180)