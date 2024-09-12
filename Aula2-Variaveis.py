john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=", ")
total_apples = john+mary+adam
print("Total:", total_apples) #Ex 1, Listar as maças e somar

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles") #Ex 2, usando a função round

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+") #Replicando uma string

a=float(input("Digite o primeiro número: "))
b=float(input("Digite o segundo número: "))

print("Soma: ", a+b)
print("Subtração: ", a-b)
print("Multiplicação: ", a*b)
print("Divisão: ", a/b)

print("\nThat's all, folks!") #Ex 3, 4 operações básicas

hora = int(input("Starting time (hours): "))
min = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

horaf = (hora+(min+dura)//60)%24 #verifica quantas horas se passaram com a divisão exata, e depois converte no modelo de 24 horas com o resto
minf = (min+dura)%60 #soma os minutos que se passaram e converte no modelo de 60 minutos por hora com o resto

print("Hora final", horaf, minf, sep=":") #Ex 4, conversão de minutos em horas