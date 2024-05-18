print("Digite os valores a somar seguidos de [ENTER].")
print("Para encerrar apenas [ENTER].")

total = 0
while 1:
    try:
        n = float(input(':'))
        total = total + n
    except:
        break
    print(f'Total: {total}')

# Loops simples
i = 0 
while i < 10:
    print(i)
    i += 1

for i in range(1,11):
    print(i)