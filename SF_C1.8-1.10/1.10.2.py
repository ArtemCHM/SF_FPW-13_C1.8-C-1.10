class Rectagle():
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width

    def rectagle_area(self):
        return f'Rectagle data:\nlenght = {self.lenght};'\
               f' width = {self.width}; '\
               f'total = {self.lenght * self.width}'

total_rectagle = Rectagle(6,9)
print(total_rectagle.rectagle_area())