class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self,a):
        self.a = a
    def get_area_square(self):
        return self.a**2

class Circle:
    def __init__(self,a,pi = 3.14):
        self.a = a
        self.pi = pi
    def get_area_circle(self):
        return self.pi * self.a **2

#class Circle:
#   def __init__(self,a):
#        self.a = a
#   def get_area_circle(self):
#      return 3.14 * self.a **2

#Поясните пожалуйста этот вариант, почему так неправлиьно, и выдает ошибку.