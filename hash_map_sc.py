from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(LinkedList())

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
        Updates the key / value pair in the hash map. If the given key already exists in
        the hash map, its associated value is replaced with the new value.
        If the given key is not in the hash map, a key / value pair is added.
        """
        # get the hash index by dividing the hash value by the capacity and getting the remainder
        hash_index = self._hash_function(key) % self._capacity

        if self._buckets[hash_index].contains(key):
            self._buckets[hash_index].contains(key).value = value
        else:
            self._buckets[hash_index].insert(key, value)
            self._size += 1

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table
        """
        # empty buckets = any index that has size == 0 within the hash table
        empty_buckets = 0
        for i in range(self._capacity):
            if self._buckets[i].length() == 0:
                empty_buckets += 1

        return empty_buckets

    def table_load(self) -> float:
        """
        Returns the current hash table load factor.
        Load factor is calculated by dividing the number of elements (filled buckets) in the hash table
        by the total number of buckets.
        """
        lf = self._size / self._capacity
        return lf

    def clear(self) -> None:
        """
        Clears the contents of the hash map without changing the underlying capacity
        """
        for i in range(self._capacity):
            self._buckets[i] = LinkedList()
        self._size = 0

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table and rehashing all table
        key / value pairs with their respective hash table links.
        If new_capacity is less than 1, the method does nothing
        """
        if new_capacity < 1:
            return

        new_hashmap = DynamicArray()
        for _ in range(new_capacity):
            new_hashmap.append(LinkedList())

        keys_array = self.get_keys()

        # iterate through filled_buckets until all keys are hashed to new table
        for i in range(self._size):
            key = keys_array.pop()
            hash_index = self._hash_function(key) % new_capacity
            new_hashmap[hash_index].insert(key, self.get(key))

        self._buckets = new_hashmap
        self._capacity = new_capacity

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key. If the key is not in the hash
        map, returns None
        """
        # get the hash index by dividing the hash value by the capacity and getting the remainder
        hash_index = self._hash_function(key) % self._capacity

        if self._buckets[hash_index].contains(key):
            return self._buckets[hash_index].contains(key).value

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the hash map. Returns False otherwise
        An empty hash map does not contain any keys
        """
        # get the hash index by dividing the hash value by the capacity and getting the remainder
        hash_index = self._hash_function(key) % self._capacity
        # check if hash map is empty
        if self._size == 0:
            return False

        if self._buckets[hash_index].contains(key):
            return True
        return False

    def remove(self, key: str) -> None:
        """
        Removes the given ey and its value from the hash map. If the key is not
        in the hash map, the method does nothing and no exception is raised.
        """
        # get the hash index by dividing the hash value by the capacity and getting the remainder
        hash_index = self._hash_function(key) % self._capacity

        if self._buckets[hash_index].remove(key) is True:
            self._size -= 1

    def get_keys(self) -> DynamicArray:
        """
        Returns a Dynamic Array that contains all the keys stored in the hash map.
        """
        keys_array = DynamicArray()
        array_size = 0

        for i in range(self._capacity):
            if array_size == self._size:
                break
            elif self._buckets[i].length() > 0:
                for node in self._buckets[i]:
                    keys_array.append(node.key)
                    array_size += 1

        return keys_array

def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    Returns a tuple containing a DynamicArray containing the mode value(s) within "da" DynamicArray, and an integer
    that represents the highest frequency they appear.
    The input array "da" will contain at least one element, and all values stored in the array will be string.
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap(da.length() // 3, hash_function_1)
    mode_val = DynamicArray()

    for i in range(da.length()):
        if map.contains_key(da[i]):
            map.put(da[i], map.get(da[i]) + 1)
        else:
            map.put(da[i], 1)

    max_freq = 0
    keys_list = map.get_keys()

    for i in range(keys_list.length()):
        if map.get(keys_list[i]) > max_freq:
            max_freq = map.get(keys_list[i])

    for i in range(keys_list.length()):
        if map.get(keys_list[i]) == max_freq:
            mode_val.append(keys_list[i])

    return mode_val, max_freq


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

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "melon", "peach"])
    map = HashMap(da.length() // 3, hash_function_1)
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        map = HashMap(da.length() // 3, hash_function_2)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}\n")
