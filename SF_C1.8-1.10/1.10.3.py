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

clients = Client('Ivan Petrov', 50)
print(clients.purse())