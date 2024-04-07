import os

nomeAluno = input("Insira seu nome: ")
os.system('clsD')

nota1Unidade = float(input("Insira a nota da sua 1º unidade: "))
os.system('clsD')

nota2Unidade = float(input("Insira a nota da sua 2º unidade: "))
os.system('clsD')

nota3Unidade = float(input("Insira a nota da sua 3º unidade: "))
os.system('clsD')




mediaGeral = (nota1Unidade+nota1Unidade+nota3Unidade)/3

if mediaGeral>= 5:
    print("Parabéns", nomeAluno, "você foi APROVADO")
else:
    print(f'`{nomeAluno} você está em RECUPERAÇÃO. Sua média: {mediaGeral:.1f}')
    

