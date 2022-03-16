"""
Hashmap
    - key/value mapping
    - constant O(1) insertion and lookup

We will implement using the built-in python
hash(value: any) -> int function. They can take any
immutable input and returns a unique 64 bit int
that corresponds to it.

One implementation strategy could be to create a
list 2**64 elements long and store each element
at an appropriate place. This is infeasible
because of memory restrictions, so can make
a fixed length array and take the
modulo(array_len, radix) to get the place to
store the element.
"""


class MyHashMap:
    def __init__(self, exp=3, initial=None):
        if initial is None:
            initial = {}

        self.radix = 2 ** exp
        self.keys = [None] * self.radix
        self.values = [None] * self.radix

        for k, v in initial.items():
            self[k] = v

    def rehash(self):
        self.radix *= 2
        new_keys = [None] * self.radix
        new_values = [None] * self.radix

        for idx, key in enumerate(self.keys):
            if not key:
                continue

            hashed_key = hash(key) % self.radix
            new_keys[hashed_key] = key
            new_values[hashed_key] = self.values[idx]

        self.keys = new_keys
        self.values = new_values

    def __getitem__(self, key):
        return self.values[hash(key) % self.radix]

    def __setitem__(self, key, value):
        hashed_key = hash(key) % self.radix

        while self.values[hashed_key] is not None:
            self.rehash()

        self.keys[hashed_key] = key
        self.values[hashed_key] = value

    def __str__(self):
        return str(dict(zip(self.keys, self.values)))

    def __repr__(self):
        return self.__str__()

    def __contains__(self, key):
        return self.keys[hash(key) % self.radix] == key


def main():
    hash_map = MyHashMap(initial={
        "hello": 1,
        "how": 2,
        "are": 3,
        "you": 4,
        "I": 2,
        "am": 3,
        "hampter": 1,
        "frog": 0,
        "aghghgh": 1,
        "me when": 1
    })
    print(list(filter(lambda x: x is not None, hash_map.keys)))
    print(list(filter(lambda x: x is not None, hash_map.values)))


if __name__ == "__main__":
    main()
