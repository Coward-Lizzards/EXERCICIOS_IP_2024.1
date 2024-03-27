# %%
n_a = int(input("Me dê um número:"))
n_c = 8 - n_a
n_b = 8 - n_a + n_c
soma = n_a + n_b - n_c
print(f"{n_a} + {n_b} - {n_c} =", soma)

# o print da soma pode sair confuso se uma das variaveis for negativa
# update: descobri f-strings
# depois de mais testes eu percebi que ainda tenho o mesmo problema
# %%
n_a = float(input("Me dê um número:"))
n_b != 0
n_c = (8 * n_b) / n_a
soma = (n_a / n_b) * n_c
print(f"({n_a} / {n_b}) * {n_c} =", soma)

# %%
