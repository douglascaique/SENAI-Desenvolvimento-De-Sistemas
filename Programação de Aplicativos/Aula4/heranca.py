
class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Clientes(Pessoa):
    def __init__(self, nome, cpf, idade, limite):
        super().__init__(nome, cpf, idade)
        self.limite = limite

    def informaLimite(self):
        print(f'Olá {self.nome}, seu limite é de: {self.limite}')


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf)
        self.salario = salario






cliente1 = Clientes("João", 30, "123.456.789-00", 1000)

cliente1.informaLimite()

