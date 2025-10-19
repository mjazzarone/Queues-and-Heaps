class DoctorNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None
    
    def insert(self, doctor_name, nurse_name, side):
        if self.root is None:
            self.root = DoctorNode(doctor_name)
            if side == "left":
                self.root.left = DoctorNode(nurse_name)
            elif side == "right":
                self.root.right = DoctorNode(nurse_name)
        else:
            if self.root.value == doctor_name:
                if side == "left" and self.root.left is None:
                    self.root.left = DoctorNode(nurse_name)
                elif side == "right" and self.root.right is None:
                    self.root.right = DoctorNode(nurse_name)
                else:
                    print(f"{side.capitalize()} side already occupied for {doctor_name}")
            elif self.root.left and self.root.left.value == doctor_name:
                if side == "left" and self.root.left.left is None:
                    self.root.left.left = DoctorNode(nurse_name)
                elif side == "right" and self.root.left.right is None:
                    self.root.left.right = DoctorNode(nurse_name)
                else:
                    print(f"{side.capitalize()} side already occupied for {doctor_name}")
            elif self.root.right and self.root.right.value == doctor_name:
                if side == "left" and self.root.right.left is None:
                    self.root.right.left = DoctorNode(nurse_name)
                elif side == "right" and self.root.right.right is None:
                    self.root.right.right = DoctorNode(nurse_name)
                else:
                    print(f"{side.capitalize()} side already occupied for {doctor_name}")
            else:
                print(f"Doctor {doctor_name} not found at root level.")

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.value] + self._preorder(node.left) + self._preorder(node.right)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.value]

tree = DoctorTree()

tree.insert("Dr. Grey", "Nurse Joy", "left")       
tree.insert("Dr. Grey", "Nurse Sam", "right")     
tree.insert("Nurse Joy", "Intern Mike", "left")    

print("Preorder:", tree.preorder())
print("Inorder:", tree.inorder())
print("Postorder:", tree.postorder())
    




# Test your DoctorTree and DoctorNode classes here
