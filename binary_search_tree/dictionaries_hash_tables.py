class HashTable:
    def insert(self, key, value):
        pass

    def find(self, key):
        pass

    def update(self, key, value):
        pass

    def list_all(self):
        pass


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
    print(">>> result: ",result)
    list_index = result % len(data_list)
    return list_index





