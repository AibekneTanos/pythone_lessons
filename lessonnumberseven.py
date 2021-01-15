class Worker(object):

    def __init__(self, salary):
        self.zarplata = salary
        self.years = '19'
        self.name = 'Martin'

    def show(self):
        print('Это:', self.name, 'ему:', self.years, 'его зарплата:', self.zarplata)

    def __del__(self):
        print("Сейчас будет удалено")

king = Worker(15000)
king.show()

class Driver(Worker):
    has_car = True


    def __init__(self):
        self.salary = "28 000"
        self.name = "Pudge"
        self.years = '28'


    def show(self):
        print('Это:', self.name, "ему:", self.years, 'его зарплата:', self.salary)

    def __del__(self):
        print("Удалено")

pup = Driver()
pup.show()