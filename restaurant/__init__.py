from restaurant.cash_desk import CashDesk
from restaurant.give_away import GiveAway
from restaurant.kitchen import Kitchen
from restaurant.manager import Manager
from restaurant.order import Order

if __name__ == '__main__':
    #Tworzenie instancji klasy - obiektów
    cash_desk = CashDesk(None)
    give_away = GiveAway(None)
    kitchen = Kitchen(None)

    #Tworzenie obieku klasy manager i przkeazanie prametrów
    manager = Manager(cash_desk, kitchen, give_away)

    #przekazanie obiektu manager do pozostałych obiektów
    cash_desk.manager = manager
    kitchen.manager = manager
    give_away.manager = manager
    #koniec setupu

    #nowe zamówienie
    lista=['Pizza', 'Burger', 'Kotlet']
    for meal in lista:
        cash_desk.new_order(Order(meal))

    cash_desk.new_order(Order('Pizza Quatro'))
