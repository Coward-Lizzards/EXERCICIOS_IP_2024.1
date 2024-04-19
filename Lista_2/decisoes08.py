# %%
stok = int(input("Insira estoque atual:"))
stokMax = int(input("Capacidade max de estoque:"))
stokMin = int(input("Capacidade min de estoque:"))
media = ((stokMax + stokMin) / 2)
if stok >= media:
    print("Não efetuar Compra!")
else:
    print("Efetuar Compra!")