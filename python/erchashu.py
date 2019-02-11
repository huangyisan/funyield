class BinNode(object):
    def __init__(self, val):
        self.lchild = None
        self.rchild = None
        self.val = val

    def preOrder(self, root):
        if root is None:
            return
        mystack = []
        node = root
        while node or mystack:
            while node:
                # 从根节点开始，一直找它的左子树
                print(node.val)
                mystack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = mystack.pop()
            # 开始查看它的右子树
            node = node.rchild

root = BinNode('root')
root.lchild = BinNode('left')
root.rchild = BinNode('right')
root.rchild.lchild = BinNode('rl')
root.rchild.rchild = BinNode('rr')
root.preOrder(root)