HASH_TABLE_SIZE = 1024


class HashTable:
    # def __init__(self, key, value):
    #     self.key = key
    #     self.value = value

    hash_table = []
    bucket = []
    item = []

    def __init__(self):
        pass

    def hash_func(self, key):
        bucket_size = 128
        hash_val = 0
        for ch in key:
            hash_val = (hash_val + ord(ch)) % bucket_size
        return hash_val

    def additem(self, key, value):
        hv = self.hash_func(key)

        self.item.append(key)
        self.item.append(value)

        self.bucket.append(hv)
        self.bucket.append(self.item)

        self.hash_table.append(self.bucket)


ht = HashTable()
ht.additem('H', 'Hydrogen')
ht.additem('O', 'Oxygen')
ht.additem('N', 'Nitrogen')
print ht.hash_table

print ht.hash_table[0]
#print ht.hash_table[1]

# print ht.getvalue('H')
