# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Andrew Hepworth


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.data = [[]] * self.size

    def __setitem__(self, key, value):
        if self.data[self.hash(key)] and self.data[self.hash(key)][0][0] != key:
            self.data[self.hash(key)].append([key, value])
        else:
            self.data[self.hash(key)] = [[key, value]]

    def __getitem__(self, key):
        if self.data[self.hash(key)] == []:
            return None
        return self.data[self.hash(key)][0][1]

    def hash(self, input):
        return hash(input) % (self.size)

    def delete(self, key):
        self.data[self.hash(key)] = []
    
    def clear(self):
        self.data = [[]] * self.size

    def keys(self):
        key_list = []
        for item in self.data:
            for inner_item in item:
                key_list.append(inner_item[0])
        return key_list

    def values(self):
        value_list = []
        for key in self.keys():
            value_list.append(self.__getitem__(key))
        return value_list


    pass