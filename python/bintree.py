class BinTree(object):
    def __init__(self,root):
        self.root = root
        self.left = None
        self.right = None

    def preorder(self, root):
        if root is None:
            return

        stack = []
        node = root
        while node or stack:
            while node:
                print(node.root)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    def midorder(self,root):
        if root is None:
            return
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.root)
            node = node.right

    def backorder(self, root):
        if root is None:
            return
        mystack1 = []
        mystack2 = []
        node = root
        mystack1.append(node)
        while mystack1:
            node = mystack1.pop()
            if node.left:
                mystack1.append(node.left)
            if node.right:
                mystack1.append(node.right)
            mystack2.append(node)
        while mystack2:
            print(mystack2.pop().root)


root = BinTree('F')
root.left = BinTree('B')
root.right = BinTree('G')
root.left.left = BinTree('A')
root.left.right = BinTree('D')
root.left.right.left = BinTree('C')
root.left.right.right = BinTree('E')
root.right.right = BinTree('I')
root.right.right.left = BinTree('H')

root.backorder(root)