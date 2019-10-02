import random


class Util:
    __value = 1 # default value

    def __init__(self):
        self.new_weight()

    def get_weight(self):
        return self.__weight

    def new_weight(self):
        self.__weight = random.random() - random.random()

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value
