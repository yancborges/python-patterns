class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return 'Name: %s - Price: %s' %(self.name, self.price)
    
    @property
    def discount(self, percent):
        return self.price * percent

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))
        self._price = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, text):
        self._name = text.upper()


shirt = Product('shirt', 'R$29.90')
print(shirt)
shirt.price = 85.10
print(shirt)