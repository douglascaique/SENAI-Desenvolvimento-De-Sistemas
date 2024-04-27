class Clientes:
    def __init__(self, nome, idade, cpf, limite):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.limite = limite


    def nome(self):
        return f'{self.__nome}'

    def exibir(self):
        return (f"Nome: {self.nome}")
        return (f"Idade: {self.idade}")
        return (f"CPF: {self.cpf}")
        return (f"Limite: {self.limite}")

# cliente1 = Clientes("João", 30, "123.456.789-00", 1000)
# print(cliente1.exibir)





class Funcionarios:
    def __init__(self, nome, idade, cpf, salario):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.salario = salario

    def nome(self):
        return f'{self.__nome}'

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Salário: {self.salario}")


funcionario1 = Funcionarios("Maria", 25, "987.654.321-00", 2000)
print(funcionario1.nome)


