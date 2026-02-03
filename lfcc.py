from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_map = {}                     # key -> [value, freq]
        self.freq_map = defaultdict(OrderedDict)  # freq -> OrderedDict

    def _update_freq(self, key):
        value, freq = self.key_map[key]

        # Remove key from current frequency list
        del self.freq_map[freq][key]

        # If this was the last key with min_freq, update min_freq
        if not self.freq_map[freq] and freq == self.min_freq:
            self.min_freq += 1

        # Add key to next frequency
        self.freq_map[freq + 1][key] = None
        self.key_map[key] = [value, freq + 1]

    def get(self, key):
        if key not in self.key_map:
            return -1

        self._update_freq(key)
        return self.key_map[key][0]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_map:
            self.key_map[key][0] = value
            self._update_freq(key)
            return

        # Eviction if capacity full
        if self.size == self.capacity:
            lru_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[lru_key]
            self.size -= 1

        # Insert new key
        self.key_map[key] = [value, 1]
        self.freq_map[1][key] = None
        self.min_freq = 1
        self.size += 1
