from time import time, sleep, ctime

from restaurant.logs import Logger


class GiveAway:

    def __init__(self, manager):
        self.manager = manager
        self.logs = Logger('giveaway.log')

    def call_customer(self, order):
        print(f'4. Wydawka wzywa klienta:{ctime(time())}')
        self.logs.log(f'4. Wydawka wzywa klienta:{ctime(time())}')
        sleep(2)
        self.customer_collected_order(order)

    def customer_collected_order(self, order):
        order._collected_at = time()
        print(f'5. Klient odebrał order: {ctime(time())}')
        self.logs.log(f'4. Wydawka wzywa klienta:{ctime(time())}')
        self.manager.customer_collected_order(order)
