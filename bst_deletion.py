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



    def minimum_element(self,root):
        while 1:
            if root.left is None:
                return root.data
                break
            else:
                root=root.left
                
    def maximum_element(self,root):
        while 1:
            if root.right is None:
                return root.data
                break
            else:
                root=root.right


    def delete_a_node(self,root,value):
        if value<root.data:
            if root.left:
                root.left = self.delete_a_node(root.left,value)
        elif value>root.data:
            if root.right:
                root.right = self.delete_a_node(root.right,value)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # min_value = self.minimum_element(root.right)
            # root.data = min_value
            # root.right = self.delete_a_node(root.right,min_value)
            # or
            max_value = self.maximum_element(root.left)
            root.data = max_value
            root.left = self.delete_a_node(root.left,max_value)
        return root

        


if __name__=="__main__""
  tree = Tree()
  root = tree.createNode(5)
  ele = [5,2,10,7,15,12,20,30,6,8]
  for i in range(1,len(ele)):
      tree.insertNode(root,ele[i])

  tree.delete_a_node(root,15)
  tree.inorderTraverse(root)



    
