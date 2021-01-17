from typing import Any


class HashMap:
    """ Hashmap implementation
    search O(1)
    insert O(1)
    lookup O(1)
    delete O(1)
    """

    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key: str) -> int:
        """
        Args:
            key: hash key
        Returns: hashed key
        """
        hash_key = 0

        for char in key:
            hash_key += ord(char)

        return hash_key % self.size

    def set(self, key: str, value: Any):
        """
        Args:
            key: str
            value: Any
        """
        hash_key = self._get_hash(key)

        if not self.map[hash_key]:
            self.map[hash_key] = [[key, value]]
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[hash_key].append([key, value])
        return None

    def get(self, key: str) -> Any:
        """
        Args:
            key:
        Returns:
        """
        hash_key = self._get_hash(key)

        if self.map[hash_key]:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]

        return None

    def delete(self, key: str):
        """
        Args:
            key:
        """
        hash_key = self._get_hash(key)
        item = self.map[hash_key]

        if item:
            for i in range(len(item)):
                if item[i][0] == key:
                    del item[i]
                    # item.pop(i)

    def keys(self):
        """
        Returns:
        """
        keys = []

        for item in self.map:
            if item is not None:
                # solving the collision
                if len(item) > 1:
                    for i in item:
                        keys.append(i[0])
                else:
                    keys.append(item[0][0])

        return keys

    def __str__(self):
        return str(self.__dict__)


hash_map = HashMap(5)
hash_map.set('Almaty', 1)
hash_map.set('Almate', 2)
hash_map.set('Almate', 3)
hash_map.set('Almatee', 4)
print(hash_map.get('Almate'))
print(hash_map)
hash_map.delete('Almate')
print(hash_map)
hash_map.set('Almate', 3)
print(hash_map.keys())
