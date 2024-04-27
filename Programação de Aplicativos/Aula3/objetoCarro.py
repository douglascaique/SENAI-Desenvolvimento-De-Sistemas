class Carro:
    def __init__(self,nome,marca, ano, velocidade):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.velocidade = velocidade


    def acelerar(self, acelera):
        self.velocidade = self.velocidade + acelera
        print(f'Velocidade atual Acelerando: {self.velocidade} Km/h!')
        if self.velocidade > 110:
            print(f'Seu carro foi MULTADO. {self.velocidade - 100} Km/h acima do permitido!')
            return

    def freiar(self, freia):
        self.velocidade = self.velocidade - freia
        print(f'Velocidade atual Freiando: {self.velocidade} Km/h!')
        return