class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val


def createTreeItem(key, val):
    return Node(key, val)


class BST:
    def __init__(self):
        self.root = None
        self.leftChild = None
        self.rightChild = None

    def isEmpty(self):
        return self.root is None

    # ---------- INSERT ----------
    def searchTreeInsert(self, treeItem):
        if self.isEmpty():
            self.root = treeItem
            return True

        if treeItem.key < self.root.key:
            if self.leftChild is None:
                self.leftChild = BST()
            return self.leftChild.searchTreeInsert(treeItem)

        if treeItem.key > self.root.key:
            if self.rightChild is None:
                self.rightChild = BST()
            return self.rightChild.searchTreeInsert(treeItem)

        return False  # duplicate key

    # ---------- RETRIEVE ----------
    def searchTreeRetrieve(self, key):
        if self.isEmpty():
            return (None, False)

        if key < self.root.key:
            if self.leftChild:
                return self.leftChild.searchTreeRetrieve(key)
            return (None, False)

        if key > self.root.key:
            if self.rightChild:
                return self.rightChild.searchTreeRetrieve(key)
            return (None, False)

        return (self.root.value, True)

    # ---------- INORDER ----------
    def inorderTraverse(self, visit_function):
        if self.isEmpty():
            return
        if self.leftChild:
            self.leftChild.inorderTraverse(visit_function)
        visit_function(self.root.value)
        if self.rightChild:
            self.rightChild.inorderTraverse(visit_function)

    # ---------- SUCCESSOR ----------
    def successor(self):
        current = self.rightChild
        if current is None or current.isEmpty():
            return None
        while current.leftChild and not current.leftChild.isEmpty():
            current = current.leftChild
        return current

    # ---------- DELETE ----------
    def searchTreeDelete(self, key):
        if self.isEmpty():
            return False

        if key < self.root.key:
            if self.leftChild:
                return self.leftChild.searchTreeDelete(key)
            return False

        if key > self.root.key:
            if self.rightChild:
                return self.rightChild.searchTreeDelete(key)
            return False

        # key gevonden
        # geen kinderen
        if (self.leftChild is None or self.leftChild.isEmpty()) and (
            self.rightChild is None or self.rightChild.isEmpty()
        ):
            self.root = None
            return True

        # enkel rechter kind
        if self.leftChild is None or self.leftChild.isEmpty():
            temp = self.rightChild
            self.root = temp.root
            self.leftChild = temp.leftChild
            self.rightChild = temp.rightChild
            return True

        # enkel linker kind
        if self.rightChild is None or self.rightChild.isEmpty():
            temp = self.leftChild
            self.root = temp.root
            self.leftChild = temp.leftChild
            self.rightChild = temp.rightChild
            return True

        # twee kinderen
        suc = self.successor()
        self.root = suc.root
        self.rightChild.searchTreeDelete(suc.root.key)
        return True

    # ---------- SAVE ----------
    def save(self):
        if self.isEmpty():
            return None

        left = (
            self.leftChild.save()
            if self.leftChild and not self.leftChild.isEmpty()
            else None
        )
        right = (
            self.rightChild.save()
            if self.rightChild and not self.rightChild.isEmpty()
            else None
        )

        if left is None and right is None:
            return {"root": self.root.key}

        return {"root": self.root.key, "children": [left, right]}

    # ---------- LOAD ----------
    def load(self, dictionary):
        if dictionary is None:
            self.root = None
            self.leftChild = None
            self.rightChild = None
            return

        key = dictionary.get("root")
        self.root = createTreeItem(key, key)

        children = dictionary.get("children")

        self.leftChild = BST()
        if children and len(children) > 0 and children[0] is not None:
            self.leftChild.load(children[0])

        self.rightChild = BST()
        if children and len(children) > 1 and children[1] is not None:
            self.rightChild.load(children[1])