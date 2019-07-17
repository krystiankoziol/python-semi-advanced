from time import time, ctime

from restaurant.logs import Logger


class CashDesk:

    def __init__(self, manager):
        self.manager = manager
        self.logs = Logger('cashdeck.log')

    def new_order(self, order):
        #Przekazanie do managera
        print(f'1. Kasa przyjeła order:{ctime(time())}')
        self.logs.log(f'1. Kasa przyjeła order:{ctime(time())}')
        self.manager.new_order(order)
