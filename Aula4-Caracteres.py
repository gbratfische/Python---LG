email=input("Digite o seu email: ")
for letras in email:
    if letras == "@":
        break
    print(letras, end="")