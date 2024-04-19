# %%
macas = float(1.30)
macaDuzia = int(1)
compra = float(input("quantas macas meu senhor?"))
calc1 = macas * compra
calc2 = macaDuzia * compra
if compra >= 12:
    print(f"{compra} maçãs dá R${calc2}!")
else:
    print(f"{compra} maçãs dá R${calc1}!")