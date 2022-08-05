from a6_include import (DynamicArray, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(None)

        self._capacity = capacity
        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Hash the key into the array and insert the value at the index hashed from key
        """
        if self.table_load() >= 0.5:
            self.resize_table(self._capacity * 2)

        # calculate the hash index
        hash_index = self._hash_function(key) % self._capacity

        # if the index is None, insert a HashEntry object into that index position
        if self._buckets.get_at_index(hash_index) is None:
            self._buckets.set_at_index(hash_index, HashEntry(key, value))
        # else, checks if the HashEntry is deleted (is_tombstone is True) and replace with a new HashEntry
        elif self._buckets.get_at_index(hash_index) and self._buckets.get_at_index(hash_index).is_tombstone is True:
            self._buckets.set_at_index(hash_index, HashEntry(key, value))
        # else, if the key already exists and is not a tombstone, update its value
        elif self._buckets.get_at_index(hash_index) and self._buckets.get_at_index(hash_index).key == key:
            self._buckets.get_at_index(hash_index).value = value
            return
        # else, check for collision
        else:
            j = 1
            next_index = hash_index
            while self._buckets.get_at_index(next_index) and self._buckets.get_at_index(next_index).is_tombstone is False:
                if self._buckets.get_at_index(next_index).key == key:
                    self._buckets.get_at_index(next_index).value = value
                    return
                next_index = (hash_index + j**2) % self._capacity
                j += 1
            self._buckets.set_at_index(next_index, HashEntry(key, value))

        self._size += 1

    def table_load(self) -> float:
        """
        Returns the current hash table load factor
        """
        # load factor is calculates as size / capacity
        lf = self._size / self._capacity
        return lf

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table
        """
        # empty buckets are elements that are either None or has is_tombstone = True
        empty_buckets = 0
        for i in range(self._capacity):
            if self._buckets.get_at_index(i) is None or self._buckets.get_at_index(i).is_tombstone is True:
                empty_buckets += 1

        return empty_buckets

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table. All existing key / value pairs will be
        rehashed in the new hash map. If "new_capacity" is less than 1, or less than the current number
        of elements in the map, the method does nothing
        """
        # check if new_capacity is valid
        if new_capacity < 1 or new_capacity < self._size:
            return
        # check if new_capacity can maintain a lf ratio of < 0.5
        while self._size / new_capacity >= 0.5:
            new_capacity *= 2

        new_hashmap = DynamicArray()
        for _ in range(new_capacity):
            new_hashmap.append(None)

        keys_list = self.get_keys()

        for i in range(keys_list.length()):
            key = keys_list[i]
            hash_index = self._hash_function(key) % new_capacity
            if new_hashmap[hash_index] is None:
                new_hashmap.set_at_index(hash_index, HashEntry(key, self.get(key)))
            else:
                j = 1
                next_index = hash_index
                while new_hashmap.get_at_index(next_index):
                    if new_hashmap.get_at_index(next_index).key == key:
                        new_hashmap.get_at_index(next_index).value = self.get(key)
                    next_index = (hash_index + j ** 2) % new_capacity
                    j += 1
                new_hashmap.set_at_index(next_index, HashEntry(key, self.get(key)))

        self._buckets = new_hashmap
        self._capacity = new_capacity

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key. If the key is not in the hash map, returns None
        """
        # calculate the hash index
        hash_index = self._hash_function(key) % self._capacity
        next_index = hash_index
        j = 1
        while self._buckets.get_at_index(next_index) and self._buckets.get_at_index(next_index).is_tombstone is False:
            if self._buckets.get_at_index(next_index).key == key:
                return self._buckets.get_at_index(next_index).value
            else:
                next_index = (hash_index + j ** 2) % self._capacity
                j += 1

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the hash map. Returns False otherwise.
        An empty hash map does not contain any keys
        """
        # check if the hash map is empty
        if self._size == 0:
            return False

        # calculate the hash index
        hash_index = self._hash_function(key) % self._capacity
        next_index = hash_index
        j = 1
        while self._buckets.get_at_index(next_index) and self._buckets.get_at_index(next_index).is_tombstone is False:
            if self._buckets.get_at_index(next_index).key == key:
                return True
            else:
                next_index = (hash_index + j ** 2) % self._capacity
                j += 1

        return False

    def remove(self, key: str) -> None:
        """
        Removes the given key and its associated value from the hash map. If the key is not in the hash map,
        the method does nothing and no exception is raised.
        """
        # calculate the hash index
        hash_index = self._hash_function(key) % self._capacity
        next_index = hash_index
        j = 1
        while self._buckets.get_at_index(next_index):
            if self._buckets.get_at_index(next_index).key == key:
                if self._buckets.get_at_index(next_index).is_tombstone is False:
                    self._buckets.get_at_index(next_index).is_tombstone = True
                    self._size -= 1
                return
            else:
                next_index = (hash_index + j ** 2) % self._capacity
                j += 1

    def clear(self) -> None:
        """
        Clears the content of the hash map without changing the hash map capacity
        """
        for i in range(self._capacity):
            self._buckets.set_at_index(i, None)
        self._size = 0

    def get_keys(self) -> DynamicArray:
        """
        Returns a DynamicArray that contains all the keys stored in the hash map.
        """
        keys_list = DynamicArray()
        array_size = 0

        for i in range(self._capacity):
            if array_size == self._size:
                break
            elif self._buckets.get_at_index(i) and self._buckets.get_at_index(i).is_tombstone is False:
                keys_list.append(self._buckets.get_at_index(i).key)
                array_size += 1

        return keys_list

# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() >= 0.5:
            print("Check that capacity gets updated during resize(); "
                  "don't wait until the next put()")

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
