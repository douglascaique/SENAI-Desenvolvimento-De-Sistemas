salario = float(input("Digite o salário: "))
base = salario
imposto = 0

if base > 3000:
    imposto = (base - 3000) * 0.35
    base = 3000
elif base > 1000:
    imposto = (base - 1000) * 0.20

print(f"Salário: R${salario:.2f} Imposto a pagar: R${imposto:.2f}")