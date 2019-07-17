from time import ctime
'''
Klasa przechowuje:
    nazwa
    godzina złożenia
    godz wykonia
    godz odbioru
'''
from time import time

class Order:
    def __init__(self, order_name: str):
        self.order_name = order_name
        self._created_at = time()
        self._ready_at = None
        self._collected_at = None

    def __str__(self):
        return f'Order: {self.order_name}, {ctime(self._collected_at)}, {ctime(self._ready_at)}, {ctime(self._created_at)}'
