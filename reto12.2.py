#Procesar el archivo y extraer: Cantidad de consonantes

#Se abre el archivo
file = open('mbox.txt', "r")
#Consonantes en un str
consonantes = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ"
#Cantidad de consonantes
cantidad = 0

for line in file.readlines(): #Recorre todas lineas del archivo
    for caracter in line: #Recorre todas los caracteres de cada linea
        if caracter in consonantes: #Si el caracter esta en consonantes suma 1
            cantidad += 1

#Imprime la cantidad
print(f"L cantidad de consonantes que hay es: {cantidad}")