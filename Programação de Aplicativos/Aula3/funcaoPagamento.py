def calcularPagamento(qtdHoras, valorHora):
    horas = float(qtdHoras);
    valorHora = float(valorHora)


    if horas <= 40:
        salario = horas * valorHora
    else:
        extra = horas - 40
        salario = 40 * valorHora + (extra * (1.5 * valorHora))
    return salario

