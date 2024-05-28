class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(
            self.username, self.name, self.email
        )

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


aakash = User("aakash", "Aakash Rai", "aakash@example.com")
biraj = User("biraj", "Biraj Das", "biraj@example.com")
hemanth = User("hemanth", "Hemanth Jain", "hemanth@example.com")
jadhesh = User("jadhesh", "Jadhesh Verma", "jadhesh@example.com")
siddhant = User("siddhant", "Siddhant Sinha", "siddhant@example.com")
sonaksh = User("sonaksh", "Sonaksh Kumar", "sonaksh@example.com")
vishal = User("vishal", "Vishal Goel", "vishal@example.com")

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]


def display_keys(node, space="\t", level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space * level + "∅")
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return BSTNode.to_tuple(self.left), self.key, BSTNode.to_tuple(self.right)

    def __str__(self):
        return "BSTNode <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BSTNode <{}>".format(self.to_tuple())

    def height(self):
        if self is None:
            return 0
        return 1 + max(BSTNode.height(self.left), BSTNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + BSTNode.size(self.left) + BSTNode.size(self.right)


def insert(node, key, value):
    # print(">>> node input:", node)
    # print(1)
    if node is None:
        # print(2)
        node = BSTNode(key, value)
        # print(3)
    elif key < node.key:
        # print(4)
        node.left = insert(node.left, key, value)
        # print(5)
        node.left.parent = node
        # print(6)
    elif key > node.key:
        # print(7)
        node.right = insert(node.right, key, value)
        # print(8)
        node.right.parent = node
        # print(9)

    # print(">>> node output:", node)
    # print()
    return node


def find(node, key):
    if node is None:
        return None
    if node.key == key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height


# tree = insert(None, jadhesh.username, jadhesh)
# insert(tree, biraj.username, biraj)
# insert(tree, sonaksh.username, sonaksh)
# insert(tree, aakash.username, aakash)
# insert(tree, hemanth.username, hemanth)
# insert(tree, siddhant.username, siddhant)
# insert(tree, vishal.username, siddhant)

# display_keys(tree)
# print(tree.height())
# print(tree.size())

# tree2 = insert(None, aakash.username, aakash)
# insert(tree2, biraj.username, biraj)
# insert(tree2, hemanth.username, hemanth)
# insert(tree2, jadhesh.username, jadhesh)
# insert(tree2, siddhant.username, siddhant)
# insert(tree2, sonaksh.username, sonaksh)
# insert(tree2, vishal.username, vishal)

# display_keys(tree2)
# print(tree2.height())
# print(tree2.size())

# node = find(tree, "hemanth")
# print(node.key, node.value)

# update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
# node = find(tree, "hemanth")
# print(node.key, node.value)


# print(list_all(tree))

# print(is_balanced(tree))
# print(is_balanced(tree2))


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)

    return root


# data = [(user.username, user) for user in users]
# print(data)

# tree = make_balanced_bst(data)
# display_keys(tree)


def balance_bst(node):
    return make_balanced_bst(list_all(node))


tree1 = None
for user in users:
    tree1 = insert(tree1, user.username, user)

display_keys(tree1)


tree2 = balance_bst(tree1)
display_keys(tree2)
