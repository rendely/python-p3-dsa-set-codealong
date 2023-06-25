class MySet:

    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    def has(self, val):
        return self.dictionary.get(val, False)

    def add(self, val):
        self.dictionary[val] = True
        return self

    def delete(self, val):
        self.dictionary.pop(val, None)
        return self

    def size(self):
        return len(self.dictionary)