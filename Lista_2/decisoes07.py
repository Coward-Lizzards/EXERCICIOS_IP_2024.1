# %%
accNum = float(input("Insira o número da conta:"))
saldo = float(input("Insira o saldo da conta:"))
debito = float(input("Insira o débito da conta:"))
credito = float(input("Insira o crédito da conta:"))
saldoAtual = (saldo - debito + credito)
print(f"Saldo Atual: R${saldoAtual}")

if saldoAtual > 0:
    print("Saldo Positivo!")
else:
    print("Saldo Negativo!")