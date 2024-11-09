import threading
from queue import Queue
from random import randint
from time import sleep, time


class Table:
    def __init__(self, number, guest= None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    #
    def run(self):
        sleep(randint(3,10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        q = Queue()
        for guest in guests:
            q.put(guest)
        while not q.empty():
            for Table in tables:
                if Table.guest == None:
                    Table.guest = q.get()
                    print(f'{Table.guest.name} сел(-а) за стол номер {Table.number}')
                    Table.guest.start(), Table.guest.join()
                    print(threading.current_thread())
            q_guest = q.get()
            sleep(0.5)
            print(f'{q_guest.name} в очередь')
            cafe.queue.put(q_guest)


    def discuss_guests(self):
        while not cafe.queue.empty():
            for Table in tables:
                if Table.guest == None:
                    Table.guest = cafe.queue.get()
                    Table.guest.start(), Table.guest.join()
                    print(f'{Table.guest.name} сел(-а) за стол номер {Table.number}')






# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
# cafe.discuss_guests()
