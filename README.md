# Reto-No.12

## 1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

## 2. Procesar el archivo y extraer:
* Cantidad de vocales
```python
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
print(cantidad)
```

* Cantidad de consonantes
```python
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
print(cantidad)
```

* Listado de las 50 palabras que más se repiten
```python
```
