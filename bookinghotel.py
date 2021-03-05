#proceso de reserva en un hotel
#se piden los datos al cliente y se muestran por pantalla
nombre = input("Nombre ")
apellidos = input("Apellidos ")
clientes = ["Alvaroto Nomedicenada", "Alvaroto Quierequeadivinelascosas", "Alvaroto Secreequesoymedium"]
clientes.append(nombre + " " + apellidos)
clientes.remove("Alvaroto Nomedicenada")
print(clientes)
print("Bienvenido a Hotelpavi " + nombre, apellidos, sep=" ")
#el cliente tiene que introducir los datos de su reserva
noches = input("Introduzca el número de noches que desea reservar ")
preciohab = input ("Elija el precio de la habitacion por noche ")
propina = input ("Introduzca la propina que desea dejar ")
print("Recuerde que Hotelpavi se queda el precio equivalente a 1 noche como comisión")
#calculo del precio total de la reserva para imprimir por pantalla la factura
totalhab = int(noches)* int(preciohab)
total = int(totalhab) + int(propina) + int(preciohab)
print("DESGLOSE DE PRECIOS")
print("Precio total habitacion " + str(totalhab))
print("Propina " + str(propina))
print("Comisión de 1 noche " + str(preciohab))
print("TOTAL " + str(total))
#a partir de aqui empieza lo relativo al tipo de pension
print("Ahora indique que tipo de pension desea: pension completa, todo incluido o media pension")
#el cliente tiene que indicar la pension que desea
regimenPension = ["todo incluido", "pension completa", "media pension", "alojamiento y desayuno", "alojamiento"]
pension = input("¿Que tipo de pension desea? ")
pension = pension.lower()
if regimenPension[0] == pension:
    total = total*1.3
elif regimenPension[1] == pension:
   total = total*1.2
elif regimenPension[2] == pension:
    total = total*1.1

print("Ha seleccionado 'todo incluido', se le añadira un coste del 30% a su tarifa")
print("...")
print("Calculando")
print("...")
print("El precio total por su estancia en Hotelpavi es de " + str(total) + " euros")
