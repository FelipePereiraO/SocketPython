class Produto():

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self) -> str:
        return str(self.__class__) + ": "+ str(self.__dict__)