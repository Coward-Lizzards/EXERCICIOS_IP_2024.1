# %%
num1 = int(input("Digite um valor:"))
num2 = int(input("Digite outro valor:"))
for i in (num1,num2):
    if num1 == num2:
        print("Sem números iguais!")
        break
    elif num1 > num2 and num1 != num2:
        print(f"{num1} é maior.")
        break
    elif num1 < num2 and num1 != num2:
        print(f"{num2} é maior.")
        break