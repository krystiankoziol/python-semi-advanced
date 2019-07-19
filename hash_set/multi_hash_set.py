class MultiHashSet:
    INITIAL_BUCKETS_SIZE = 4
    INCREASE_FACTOR = 2

    def __init__(self, payload_factor=0.75, increse=2, size=4):
        self.INITIAL_BUCKETS_SIZE = size
        self.INCREASE_FACTOR = increse
        self.buckets = [[] for i in range(self.INITIAL_BUCKETS_SIZE)]
        self.payload_factor = payload_factor
        self.length = 0

    def clear(self):
        for bucket in self.buckets
            bucket.clear()
        self.length = 0

    def add(self, new_entry):
        if self.length / len(self.buckets) >= self.payload_factor:
            self._increase_buckets_count(self.buckets * self.INCREASE_FACTOR)
        new_entry_hash = hash(new_entry)
        buckets_idx = new_entry_hash % len(self.buckets)
        self.buckets[buckets_idx].append(new_entry)

    def add_all(self, elements):
        size_after_insertion = self.length + len(elements)
        self._increase_buckets_count(int(size_after_insertion / self.payload_factor) + 1)
        for element in elements:
            self.add(element)

    def _increase_buckets_count(self, target_bucket_size):
        new_buckets = [[] for i in range(target_bucket_size)]
        for old_buckets in self.buckets:
            for element in old_buckets:
                new_buckets_index = hash(element) % len(new_buckets)
                new_buckets[new_buckets_index].append(element)
        self.buckets = new_buckets

    def contains(self, item):
        item_bucket_index = hash(item) % len(self.buckets)
        return item in self.buckets[item_bucket_index]

    def __contains__(self, item):
        return self.contains(item)

    def remove(self, item):
        item_bucket = hash(item) % len(self.buckets)
        bucket = self.buckets[item_bucket]
        self.buckets[item_bucket] = [x for x in bucket if x != item]
        self.length -= len(bucket) - len(self.buckets[item_bucket])

    def __len__(self):
        return self.length

    def __str__(self) -> str:
        result = '{'
        for bucket in self.buckets:
            for element in bucket:
                result += str(element)
                result += ','
        result += '}'
        return result

    def __hash__(self):

    def _groups_elements(self, mhs):
        elements = []
        for bucket in mhs.buckets:
            for element in bucket:
                elements.append(element)
        elements_gruped_by = dict()
        for element in elements:
            if element not in elements_gruped_by
                elements_gruped_by[element] = 0
            elements_gruped_by[element] += 1
        return elements_gruped_by

    def __eq__(self, other):
        this = self._groups_elements(self)
        that = self._groups_elements(other)
        return this == that
