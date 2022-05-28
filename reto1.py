# Definir variables

reconocimiento = str(input())
estrato = int(input())
salario = int(input())
minimo = 908526

acumulado = 0
    
# If reconocimiento étnico

if (reconocimiento == str("sin reconocimiento")):
    acumulado = acumulado + 0
elif (reconocimiento == str("afrodescendiente")):
    acumulado = acumulado + 9
elif (reconocimiento == str("indigena")):
    acumulado = acumulado + 10
elif (reconocimiento == str("raizal")):
    acumulado = acumulado + 11
elif (reconocimiento == str("palenquero")):
    acumulado = acumulado + 12
elif (reconocimiento == str("gitano")):
    acumulado = acumulado + 13
else:
    print("Se produjo un error")
    quit()


# If estrato

if (estrato == 1):
    acumulado = acumulado + 15
elif (estrato == 2):
    acumulado = acumulado + 13
elif (estrato == 3):
    acumulado = acumulado + 11
elif (estrato == 4):
    acumulado = acumulado + 7
elif (estrato == 5):
    acumulado = acumulado
elif (estrato == 6):
    acumulado = acumulado
else:
    print("Se produjo un error")
    quit()

# If Ingresos

if (salario < minimo):
    acumulado = acumulado + 20
elif (salario >= minimo and salario < minimo*2):
    acumulado = acumulado + 14
elif (salario >= minimo*2 and salario < minimo*4):
    acumulado = acumulado + 12
elif (salario >= minimo*4 and salario < minimo*5):
    acumulado = acumulado + 9
elif (salario >= minimo*5):
    acumulado = acumulado

# Salida de error y resultados

if (acumulado >= 30):
    print("El candidato continua en el proceso de seleccion")
elif (acumulado < 30):
    print("El candidato no continua en el proceso de seleccion")