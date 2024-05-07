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

    def get_info(self):
        return "User(username='{}', name='{}', email='{}')".format(
            self.username, self.name, self.email
        )


user4 = User("jane", "Jane Doe", "jane@doe.com")

# print(user4)

import datetime
today = datetime.datetime.now()

print(repr(today))
'datetime.datetime(2023, 2, 18, 18, 40, 2, 160890)'

print(today.__repr__())
'datetime.datetime(2023, 2, 18, 18, 40, 2, 160890)'

print(str(today))
'2023-02-18 18:40:02.160890'

print(today.__str__())
'2023-02-18 18:40:02.160890'

print(today)