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


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

tree = node0
# print(tree.key)
# print(tree.left.key)
# print(tree.right.key)


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


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


# print(tree2.key)
# print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key)
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


display_keys(tree2, '   ')
