class ChocoladeType:
    def __init__(self, type):
        self.type = None
        if type == 'wit':
            self.type = type
        elif type == 'bruin':
            self.type = type
        elif type == 'melk':
            self.type = type
        elif type == 'zwart':
            self.type = type
        else:
            print("Error: Incorrect 'Chocolade type!'")


class Item:
    def __init__(self, id):
        self.id = id



class Chocolademelk(Item):
    def __init__(self, id):
        super().__init__(id)
        self.price = 2


class Chocoladeshot(Item):
    def __init__(self, id, Ctype, exp):
        super().__init__(id)
        self.Ctype = Ctype #link to Ctype
        self.exp = exp


class User:
    def __init__(self, id, fname, lname, email):
        self.id = id
        self.fname = fname
        self.lname = lname

        self.email = None
        if not email:
            pass
            # if email does not contain @ ->error
        self.email = email


class Topping(Item):
    def __init__(self, id, exp, price):
        super().__init__(id)
        self.exp = exp
        self.price = price

class Honing(Topping):
    def __init__(self, id, exp):
        super().__init__(id, exp, 0.5)


class Chilipeper(Topping):
    def __init__(self, id, exp):
        super().__init__(id, exp, 0.25)

class Marshmallow(Topping):
    def __init__(self, id, exp):
        super().__init__(id, exp, 0,75)


class Stock:
    def __init__(self, type):
        #create checking type
        self.stock = BST()


    def add_item(self, id):
        # check if item type is correct
        self.stock.Insert(id) #could be somthing else
    def remove_item(self, id):
        # check if item type is correct
        self.stock.Delete(id)




class BST:
    def __init__(self):
        self.root = None

    def Insert(self, node):
        if self.isEmpty():
            self.root = node
            return True

        current = self.root
        while True:
            if node.key <= current.key:
                if not current.left_child:
                    current.left_child = node
                    node.parent = current
                    return True
                current = current.left_child
            if node.key > current.key:
                if not current.right_child:
                    current.right_child = node
                    node.parent = current
                    return True
                current = current.right_child

    def isEmpty(self):
        if self.root is None:
            return True
        return False

    def Retrieve(self, key):
        if self.getNodeAt(key)[1]:
            return [self.getNodeAt(key)[0].data, True]
        return [None, False]

    def getNodeAt(self, key):
        if self.isEmpty():
            return [None, False]
        current = self.root
        while True:
            if key == current.key:
                return [current, True]
            elif key < current.key:
                if not current.left_child:
                    break
                current = current.left_child
            else:
                if not current.right_child:
                    break
                current = current.right_child
        return [None, False]

    def inorderTraverse(self, flag):
        if not self.isEmpty():
            self.root.inorder(flag)

    def save(self):
        return self.root.save()

    def load(self, tree):
        root = tree.get('root')
        if root:
            self.root = Node(tree['root'], tree['root'])
            self.root.load(tree)

    def Delete(self, key):
        check = self.getNodeAt(key)
        if check[1]:
            target = check[0]

            if not target.left_child and not target.right_child:
                if target.isLeftChild():
                    target.parent.left_child = None
                elif target.isRightChild():
                    target.parent.right_child = None

            elif target.left_child and not target.right_child:
                successor = target.left_child
                if target.isLeftChild():
                    target.parent.left_child = successor
                elif target.isRightChild():
                    target.parent.right_child = successor
                successor.parent = target.parent

            elif target.right_child and not target.left_child:
                successor = target.right_child
                if target.isLeftChild():
                    target.parent.left_child = successor
                elif target.isRightChild():
                    target.parent.right_child = successor
                successor.parent = target.parent

            else:
                successor = target.inOrderSuccessor()
                if successor.isLeftChild():
                    successor.parent.left_child = None
                elif successor.isRightChild():
                    successor.parent.right_child = None
                successor.left_child = target.left_child
                successor.left_child.parent = successor
                successor.right_child = target.right_child
                successor.right_child.parent = successor

                if not target.parent:
                    successor.parent = None
                    self.root = successor
                else:
                    if target.isLeftChild():
                        target.parent.left_child = successor
                        successor.parent = target.parent
                    elif target.isRightChild():
                        target.parent.right_child = successor
                        successor.parent = target.parent
            return True

        else:
            return False

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

    def inorder(self, flag):
        if self.left_child:
            self.left_child.inorder(flag)
        if flag:
            print(self.data)
        if self.right_child:
            self.right_child.inorder(flag)

    def inOrderSuccessor(self):
        if self.right_child:
            current = self.right_child
            while current.left_child:
                current = current.left_child
            return current

        current = self
        parent = self.parent

        while parent and current == parent.right_child:
            current = parent
            parent = parent.parent

        return parent

    def isLeftChild(self):
        if self.parent.left_child == self:
            return True
        return False

    def isRightChild(self):
        if self.parent.right_child == self:
            return True
        return False

    def save(self):
        result = {'root': self.data}
        if self.left_child or self.right_child:
            children = [None, None]
            if self.left_child:
                children[0] = self.left_child.save()
            if self.right_child:
                children[1] = self.right_child.save()
            result['children'] = children

        return result

    def load(self, tree):
        children = tree.get('children')
        if children:
            left_tree = children[0]
            right_tree = children[1]
            if left_tree:
                if left_tree.get('root'):
                    self.left_child = Node(left_tree['root'], left_tree['root'])
                    self.left_child.parent = self
                    self.left_child.load(left_tree)
            if right_tree:
                if right_tree.get('root'):
                    self.right_child = Node(right_tree['root'], right_tree['root'])
                    self.right_child.parent = self
                    self.right_child.load(right_tree)

def createTreeItem(key, data):
    node = Node(key, data)
    return node
