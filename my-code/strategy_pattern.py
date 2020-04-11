class Order(object):

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value


class CalculateShipping(object):

    def execute_calculation(self, order):
        total = order.value * 0.05
        print(total)
