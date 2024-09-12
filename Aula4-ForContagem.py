import time

for contagem in range (1,6):
    print(contagem, "mississipi")
    time.sleep(1) #Mostra na tela a cada 1 segundo

print("Pronto ou não, lá vou eu!")

# break - exemplo

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break #Break: Força a saída
    print("Dentro do laço.", i)
print("Fora do loop.")


# continue - exemplo

print("The continue instrução:")
for f in range(1, 6):
    if f == 3:
        continue #Continue: Pula essa etapa
    print("Dentro do laço.", f)
print("Fora do loop.")