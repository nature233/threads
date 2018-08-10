# from factory.abstractwheel import AbstractWheel
import factory.bike as bike


class Mobai():
    def __init__(self):
        self.name = "摩拜单车"

    def say_hi(self, factory_name):
        print("hi~我是%s生产出来的%s" % (factory_name, self.name))


class OfO():
    def __init__(self):
        self.name = "ofo单车"

    def say_hi(self, factory_name):
        print("hi~我是%s生产出来的%s" % (factory_name, self.name))


if __name__ == '__main__':
    bike = bike.Bike('自行车厂')
    mobai = bike.createWheel(Mobai)
    ofo = bike.createWheel(OfO)
