# from factory.abstractfactory import AbstractFactory


class Bike():
    def __init__(self,factory_name):
        self.factory_name = factory_name
    def createWheel(self,abs_wheel):
        self.bike = abs_wheel()
        self.bike.say_hi(self.factory_name)