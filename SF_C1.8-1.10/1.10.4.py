class Client:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def purse(self):
        return f'Клиент: {self.name}. Баланс: {self.money} руб.'

class Guest(Client):
    def __init__(self, name, city, status):
        super().__init__(name)
        self.city = city
        self.status = status

    def __str__(self):
        return f'«{self.name}, г. {self.city}, статус "{self.status}"»'


if __name__ == '__main__':
    db = [{'name': 'Иван Петров', 'city': 'Тверь', 'status': 'Наставник'},
          {'name': 'Олег Сохин', 'city': 'Калининград', 'status': 'Руководитель'},
          {'name': 'Николас Дейл', 'city': 'Нови-Сад', 'status': 'Иностранный коллега'}]

    clients = [Guest(**item) for item in db]
    for client in clients:
        print(client)