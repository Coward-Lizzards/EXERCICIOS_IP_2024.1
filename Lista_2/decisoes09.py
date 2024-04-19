# %%
n1 = float(input("nota 1:"))
n2 = float(input("nota 2:"))
media = ((n1 + n2) / 2)
if media < 4:
    print(f"Suas notas foram {n1} e {n2}, sua média é {media}. \n Você caiu no conceito E e está Reprovado!")
elif media >= 4 and media < 6:
    print(f"Suas notas foram {n1} e {n2}, sua média é {media}. \n Você caiu no conceito D e está Reprovado!")
elif media >= 6 and media <= 7.5:
    print(f"Suas notas foram {n1} e {n2}, sua média é {media}. \n Você caiu no conceito C e está Aprovado!")
elif media > 7.5 and media < 9:
    print(f"Suas notas foram {n1} e {n2}, sua média é {media}. \n Você caiu no conceito B e está Aprovado!")
elif media >= 9 and media <= 10:
    print(f"Suas notas foram {n1} e {n2}, sua média é {media}. \n Você caiu no conceito A e está Aprovado!")