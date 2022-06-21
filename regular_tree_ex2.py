# exercise 2
# Extent tree class built in our main tutorial Now modify print_tree method to take tree level as input. And that should print tree only upto that level as shown below,

from posixpath import basename


class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
            


        


    def get_level(self):
        level=0
        p  =self.parent
        while p:
            level+=1
            p=p.parent
        return level

def make_tree_of_given_items():
    root = TreeNode("Global")

    india = TreeNode("INDIA")
    gujrat = TreeNode("Gujrat")
    karnataka = TreeNode("Karnataka")
    india.add_child(gujrat)
    india.add_child(karnataka)
    ahemdabad = TreeNode("Ahemdabad")
    vadodra = TreeNode("Vadodra")
    gujrat.add_child(ahemdabad)
    gujrat.add_child(vadodra)
    bangluru = TreeNode("Bangluru")
    mysore = TreeNode("Mysore")
    karnataka.add_child(bangluru)
    karnataka.add_child(mysore)

    usa = TreeNode("USA")
    new_jersy = TreeNode("New Jersy")
    california = TreeNode("California")
    usa.add_child(new_jersy)
    usa.add_child(california)
    princeton = TreeNode("Princeton")
    trenston = TreeNode("Trenston")
    new_jersy.add_child(princeton)
    new_jersy.add_child(trenston)
    san_fransisco = TreeNode("San Fransisco")
    mount_view = TreeNode("Mount View")
    palo_alto = TreeNode("Palo Alto")
    california.add_child(san_fransisco)
    california.add_child(mount_view)
    california.add_child(palo_alto)

    root.add_child(india)
    root.add_child(usa)

    return root




if __name__ == "__main__":
    root = make_tree_of_given_items()
    root.print_tree(3)
