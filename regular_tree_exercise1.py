# exercise 1
# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
# Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.

class TreeNode:
    def __init__(self,name,designation):
        self.data=[name,designation]
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def print_tree(self,method):
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""
        if method=="name":
            print(prefix+self.data[0])
        elif method=="designation":
            print(prefix+self.data[1])
        else:
            print(prefix+self.data[0]+" "+"("+self.data[1]+")")
        if self.children:
            for child in self.children:
                child.print_tree(method)


    def get_level(self):
        level=0
        p  =self.parent
        while p:
            level+=1
            p=p.parent
        return level

def build_management_tree():
    root = TreeNode("Nilupul","CEO")

    chinmay = TreeNode("Chinmay","CTO")
    vishwa = TreeNode("Vishwa","Infrastructure Head")
    aamir = TreeNode("Aamir","Application Head")
    chinmay.add_child(vishwa)
    dhawal = TreeNode("Dhawal","Cloud Manager")
    abhijit = TreeNode("Abhijit","App Manager")
    vishwa.add_child(dhawal)
    vishwa.add_child(abhijit)
    chinmay.add_child(aamir)


    gels = TreeNode("Gels","HR Head")
    peter = TreeNode("Peter","Recruitment Manager")
    waqaS = TreeNode("Waqas","Policy Manager")
    gels.add_child(peter)
    gels.add_child(waqaS)

    root.add_child(chinmay)
    root.add_child(gels)

    return root




if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
