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

# database = UserDatabase()

# database.insert(hemanth)
# database.insert(aakash)
# database.insert(siddhant)

# print(database.list_all())

# database.update(
#     User(username="siddhant", name="Siddhant Uuuu", email="siddhantuuuuuu@example.com")
# )

# print(database.list_all())

# database.insert(biraj)

# print(database.list_all())


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (
            TreeNode.traverse_in_order(self.left)
            + [self.key]
            + TreeNode.traverse_in_order(self.right)
        )

    def display_keys(self, space="\t", level=0):
        # If the node is empty
        if self is None:
            print(space * level + "∅")
            return

        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has children
        TreeNode.display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        TreeNode.display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node


# node0 = TreeNode(3)
# node1 = TreeNode(4)
# node2 = TreeNode(5)

# node0.left = node1
# node0.right = node2

# tree = node0
# print(tree.key)
# print(tree.left.key)
# print(tree.right.key)


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_tuple(tree_tuple)

# print(tree.size())
tree.display_keys('  ')


def parse_tuple(data):
    # print("data:", data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree2 = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))


def tree_to_tuples(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return node.key
    return tree_to_tuples(node.left), node.key, "aaa", tree_to_tuples(node.right)


# print(tree_to_tuples(tree2))


# print(tree2.key)
# print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key)


# def display_keys(node, space="\t", level=0):
#     # print(node.key if node else None, level)

#     # If the node is empty
#     if node is None:
#         print(space * level + "∅")
#         return

#     # If the node is a leaf
#     if node.left is None and node.right is None:
#         print(space * level + str(node.key))
#         return

#     # If the node has children
#     display_keys(node.right, space, level + 1)
#     print(space * level + str(node.key))
#     display_keys(node.left, space, level + 1)


# display_keys(tree2, "   ")


def traverse_in_order(node):
    if node is None:
        return []
    return traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right)


def pre_order(node, L):
    if node is None:
        return

    L.append(node.key)

    pre_order(node.left, L)
    pre_order(node.right, L)

    return L


def post_order(node, L):
    if node is None:
        return

    L.append(node.key)

    post_order(node.right, L)
    post_order(node.left, L)

    return L


# print(traverse_in_order(tree2))
# print(pre_order(tree2, []))
# print(post_order(tree2, []))
