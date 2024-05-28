MAX_HASH_TABLE_SIZE = 4096

data_list = [None] * MAX_HASH_TABLE_SIZE

# print(len(data_list))

# for item in data_list:
#     assert item == None


def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0

    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number

    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index


# INSERT
key, value = "Aakash", "7878787878"
idx = get_index(data_list, key)

data_list[idx] = (key, value)
data_list[get_index(data_list, "Hemanth")] = ("Hemanth", "9595949494")

# FIND
key, value = data_list[idx]
# print(value)

# LIST
pairs = [kv[0] for kv in data_list if kv is not None]
# print(pairs)


class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]


basic_table = BasicHashTable(max_size=1024)
# print(len(basic_table.data_list) == 1024)

# Insert sone values
basic_table.insert("Aakash", "9999999999")
basic_table.insert("Hemanth", "8888888888")

# Find value
# print(basic_table.find("Hemanth") == "8888888888")

# Update value
# basic_table.update("Aakash", "7777777777")

# Check the updated value
# print(basic_table.find("Aakash") == "7777777777")

# Get the list of keys
# print(basic_table.list_all())


def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv is None:
            return idx

        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx

        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0


# Create an empty hash table
data_list2 = [None] * MAX_HASH_TABLE_SIZE
# New key 'listen' should return expected index
# print(get_valid_index(data_list2, 'listen') == 655)


# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, "listen")] = ("listen", 99)

# Colliding key 'silent' should return next index
# print(get_valid_index(data_list2, 'silent') == 656)


class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value

    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]

    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]


# Create a new hash table
probing_table = ProbingHashTable()

# Insert a value
probing_table.insert("listen", 99)

# Check the value
# print(probing_table.find("listen") == 99)

# Insert a colliding key
probing_table.insert("silent", 200)

# Check the new and old keys
# print(probing_table.find("listen") == 99 and probing_table.find("silent") == 200)

# Update a key
probing_table.update("listen", 101)

# Check the value
# print(probing_table.find("listen") == 101)

# print(probing_table.list_all() == ["listen", "silent"])


class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def get_valid_index(self, key):
        # Use Python's in-built `hash` function and implement linear probing
        return hash(key)

    def __getitem__(self, key):
        # Implement the logic for "find" here        idx = self.data_list9
        pass  # change this

    def __setitem__(self, key, value):
        # Implement the logic for "insert/update" here
        pass  # change this

    def __iter__(self):
        return (x for x in self.data_list if x is not None)

    def __len__(self):
        return len([x for x in self])

    def __repr__(self):
        from textwrap import indent

        pairs = [
            indent("{} : {}".format(repr(kv[0]), repr(kv[1])), "  ") for kv in self
        ]
        return "{\n" + "{}".format(",\n".join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)
