secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
number=int(input(""))

while number!=777:
    number=int(input("Ha ha! Voce esta preso em meu loop! Digite outro número: "))
print("Muito bem, trouxa! Você está livre agora.")