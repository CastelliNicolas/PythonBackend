class ParesInfinitos:
    def __init__(self):
        self.numero = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.numero += 2
        return self.numero


pares = ParesInfinitos()

for i in range(10):
    print(next(pares))
