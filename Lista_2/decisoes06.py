# %%
num1 = int(input("Digite um valor:"))
num2 = int(input("Digite outro valor:"))
list = [num1,num2]
list.sort()
if num1 == num2:
    print("Sem números iguais!")
else:
    print(list)