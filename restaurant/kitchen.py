from time import time, sleep, ctime


class Kitchen:

    def __init__(self, manager):
        self.manager = manager

    def prepare_meal(self, order):
        print(f'2. Kuchnia przyjeła zamówienie:{ctime(time())}')
        self.save_massage_log(f'2. Kuchnia przyjeła zamówienie:{ctime(time())}')
        sleep(1)
        self.meal_ready(order)

    def meal_ready(self, order):
        order._ready_at = time()
        print(f'3. Kuchnia wydała order:{ctime(time())}')
        self.save_massage_log(f'3. Kuchnia wydała order:{ctime(time())}')
        self.manager.meal_ready(order)
    #stayczna metoda zapisu
    @staticmethod
    def save_massage_log(message):
        with open('kitchen.log', 'a', encoding='UTF-8') as f:
            f.write(message + '\n')
