class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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