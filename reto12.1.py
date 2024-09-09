#Procesar el archivo y extraer: Cantidad de vocales

#Se abre el archivo
file = open('mbox.txt', "r")
#Vocales en un str
vocales = "aAeEiIoOuU"
#Cantidad de vocales
cantidad = 0

for line in file.readlines(): #Recorre todas lineas del archivo
    for caracter in line: #Recorre todas los caracteres de cada linea
        if caracter in vocales: #Si el caracter esta en vocales suma 1
            cantidad += 1

#Imprime la cantidad
print(f"L cantidad de vocales que hay es: {cantidad}")