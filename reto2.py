n = int (input())

# Definir variables fuera de ciclo

acumulado = 0
admitido = 0
sinreconocimiento = 0 
afrodescendiente = 0   
indigena = 0   
raizal = 0  
palenquero = 0   
gitano = 0   

for n in range (0, n, 1):
    
    reconocimiento = str(input())
    estrato = int(input())
    salario = int(input())
    minimo = 908526

    # If reconocimiento étnico

    if (reconocimiento == str("sin reconocimiento")):
        acumulado = acumulado + 0
        sinreconocimiento = sinreconocimiento + 1
    elif (reconocimiento == str("afrodescendiente")):
        acumulado = acumulado + 9
        afrodescendiente = afrodescendiente + 1
    elif (reconocimiento == str("indigena")):
        acumulado = acumulado + 10
        indigena = indigena + 1 
    elif (reconocimiento == str("raizal")):
        acumulado = acumulado + 11
        raizal = raizal + 1
    elif (reconocimiento == str("palenquero")):
        acumulado = acumulado + 12
        palenquero = palenquero + 1
    elif (reconocimiento == str("gitano")):
        acumulado = acumulado + 13
        gitano = gitano + 1
    else:
        continue


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
        if (reconocimiento == str("sin reconocimiento")):
            sinreconocimiento = sinreconocimiento - 1
        elif (reconocimiento == str("afrodescendiente")):
            afrodescendiente = afrodescendiente + 1
        elif (reconocimiento == str("indigena")):
            indigena = indigena - 1 
        elif (reconocimiento == str("raizal")):
            raizal = raizal - 1
        elif (reconocimiento == str("palenquero")):
            palenquero = palenquero - 1
        elif (reconocimiento == str("gitano")):
            gitano = gitano + 1
        continue

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

    # Resultados

    if (acumulado >= 30):
        admitido = admitido + 1
    acumulado = 0

# Salidas

print(admitido)

# Candidatos por etnia
    
print("sin reconocimiento" , sinreconocimiento ) 
print("afrodescendiente" , afrodescendiente ) 
print("indigena" , indigena ) 
print("raizal" , raizal ) 
print("palenquero" , palenquero ) 
print("gitano" , gitano ) 