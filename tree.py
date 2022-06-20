class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def print_tree(self):
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


    def get_level(self):
        level=0
        p  =self.parent
        while p:
            level+=1
            p=p.parent
        return level

def make_tree_of_given_items():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Linux"))

    cell_phones = TreeNode("Cell Phones")
    cell_phones.add_child(TreeNode("Android"))
    cell_phones.add_child(TreeNode("Iphones"))
    cell_phones.add_child(TreeNode("Windows"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Normal"))
    tv.add_child(TreeNode("Smart TV"))

    root.add_child(laptop)
    root.add_child(cell_phones)
    root.add_child(tv)

    return root




if __name__ == "__main__":
    root = make_tree_of_given_items()
    root.print_tree()
