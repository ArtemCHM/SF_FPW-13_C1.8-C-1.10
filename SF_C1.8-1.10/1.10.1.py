class Rectangle:

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f' x = {self.x} \n y = {self.y} \n width = {self.width} \n height = {self.height}'

rectangle = Rectangle(5,10,50,100)
print(rectangle)

#    return f'x = {self.x}, ' \
#               f'y = {self.y}, ' \
#               f'width = {self.width}, ' \
#               f'height = {self.height}'