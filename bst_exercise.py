class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class Tree:
    def createNode(self,data):
        return Node(data)

    def insertNode(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data :
            node.left = self.insertNode(node.left,data)
        else :
            node.right = self.insertNode(node.right,data)
        return node
    
    def inorderTraverse(self,root):
        if root is not None:
            self.inorderTraverse(root.left)
            print(root.data)
            self.inorderTraverse(root.right)

    def preorderTraverse(self,root):
        if root is not None:
            print(root.data)
            self.inorderTraverse(root.left)
            self.inorderTraverse(root.right)

    def postorderTraverse(self,root):
        if root is not None:
            self.inorderTraverse(root.left)
            self.inorderTraverse(root.right)
            print(root.data)

    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1

    def minimum_element(self,root):
        while 1:
            if root.left is None:
                print(root.data)
                break
            else:
                root=root.left
                
    def maximum_element(self,root):
        while 1:
            if root.right is None:
                print(root.data)
                break
            else:
                root=root.right

    
    total=0
    def sum_of_all_elements(self,root):
        if root is not None:
            self.sum_of_all_elements(root.left)
            self.total+=root.data
            self.sum_of_all_elements(root.right)
        return self.total

        



tree = Tree()
root = tree.createNode(5)
ele = [5,2,10,7,15,12,20,30,6,8]
for i in range(1,len(ele)):
    tree.insertNode(root,ele[i])

# print("Inorder Traversal : ")
# tree.inorderTraverse(root)

# print("PreOrder Traversal : ")
# tree.preorderTraverse(root)

# print("Postorder Traversal : ")
# tree.postorderTraverse(root)

print("Minimum Element :")
tree.minimum_element(root)

print("Maximum Element :")
tree.maximum_element(root)

print("Sum" , tree.sum_of_all_elements(root))


# print("Height is : ", tree.height(root))

    
