class Item:
    def __init__(self, key, value):
        self.key = key
        sel.value = value


class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def get(self, key: int) -> int:
        index = self.hash(key)
        for item in self.table[index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def set(self, key: int, value) -> None:
        index = self.hash(key)
        for item in self.table[index]:
            if item.key == key:
                item.value = value
                return
        
        self.table[index].append(Item(key, value))

    def remove(self, key: int) -> None:
        index = self.table[index]
        for item in self.table[index]:
            if item.key == key:
                self.table[index].pop(key)
                return
        raise KeyError('Key not found')
