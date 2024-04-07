def calcular_idade(data_nasicmento, dia_de_hoje):
  #corpo função
  idade = dia_de_hoje - data_nasicmento
  return idade
  #fimfuncao

def saber_maioridade():
  resultado_do_calculo = calcular_idade(2000,2023)
  
  saber_maioridade = resultado_do_calculo >= 18

  if saber_maioridade:
    print("Usuário maior de Idade")
  else:
    print("Usuário menor de Idade")


#Codigo principal
saber_maioridade()