class Node(object):
    #树节点的定义
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.data = data #表示数据域
        self.lchild = lchild#表示左子树
        self.rchild = rchild#表示右子树
#建立树的两种方法：遍历建树与层次建树，这两种分别是基于堆栈和队列来实现的

class Tree(object):
    def __init__(self):
        self.root = Node()#表示结点
        self.myQueue = []

    #按层次生成树
    def add(self,elem):
        node = Node(elem)
        #根节点
        if self.root.data == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]#记录结点
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                self.myQueue.pop(0)#弹出已经处理好的左右子树的父节点

    #递归建树
    def tree_digui(self,root):
        data = input()
        if data is "#":
            return None
        else:
            root.data = data
            root.lchild = self.tree_digui(root.lchild)
            root.rchild = self.tree_digui(root.rchild)
        return root

    #前序遍历输出
    def front_digui(self,root):
        if root is None:
            return
        print(root.data)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self,root):
        if root is None:
            return
        self.middle_digui(root.lchild)
        print(root.data)
        self.middle_digui(root.rchild)

    def later_digui(self,root):
        if root is None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.data)


if __name__ == "__main__":
    elems = range(10)#生成10个数据作为树节点
    tree = Tree()#新建树对象
    for i in elems:
        tree.add(i)#逐个添加树节点
    print("\n\n递归实现先序遍历：")
    tree.front_digui(tree.root)
    print("\n\n递归实现中序遍历：")
    tree.middle_digui(tree.root)
    print("\n\n递归实现后序遍历：")
    tree.later_digui(tree.root)









