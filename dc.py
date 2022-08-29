#Datos personales y IMC

def imc(estatura, peso):
    return peso / estatura**2

peso = float(input("Escriba su peso (Kg): "))
estatura = float(input("Escriba su estatura (m): "))

indice = imc(estatura, peso)

print("Su IMC es: {}".format(indice))

if indice >= 0 and indice <=18.5:
    print("Bajo peso")
if indice > 18.5 and indice < 25:
    print("Normal")
if indice >= 25 and indice < 27:
    print("Sobrepeso grado 1")
if indice >= 27 and indice < 30:
    print("Sobrepeso grado 2")
if indice >= 30 and indice < 35:
    print("Obesidad tipo 1")
if indice >= 35 and indice < 40:
    print("Obesidad tipo 2")
if indice >= 40 and indice < 50:
    print("Obesidad tipo 3")
if indice >= 50:
    print("Obesidad tipo 4")
else:
    print("Error, datos incorrectos")



