class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(title={self.title!r}, author={self.author!r})"

    def __str__(self):
        return f'"{self.title}" by {self.author}'


odyssey = Book("The Odyssey", "Homer")

# print(odyssey)
# print(id(odyssey))
# print(repr(odyssey))
# print(str(odyssey))


# users = ["aakash", "biraj", "hemanth", "jadhesh", "siddhant", "sonaksh", "vishal"]

# users.insert(-2, "aaaaaaa")


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
        pass

    def list_all(self):
        pass


aakash = User("aakash", "Aakash Rai", "aakash@example.com")
biraj = User("biraj", "Biraj Das", "biraj@example.com")
hemanth = User("hemanth", "Hemanth Jain", "hemanth@example.com")
jadhesh = User("jadhesh", "Jadhesh Verma", "jadhesh@example.com")
siddhant = User("siddhant", "Siddhant Sinha", "siddhant@example.com")
sonaksh = User("sonaksh", "Sonaksh Kumar", "sonaksh@example.com")
vishal = User("vishal", "Vishal Goel", "vishal@example.com")

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]


def find_index(target):
    index = 0
    while index < len(users):
        if users[index] > target:
            break
        index += 1

    return index


def find_user(username):
    for user in users:
        if user.username == username:
            print(user)
            return user


def update(user: User):
    target = find_user(user.username)
    target.name = user.name
    target.email = user.email


print(users)

target = users[1]
new_target = User(username=target.username, name=target.name, email=target.email)
new_target.username = "hhhhhhhhhh"


print(users)
print(new_target)
