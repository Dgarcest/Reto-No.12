# Reto-No.12

## 1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

## Endswith y Startwith
  
Los metodos endswith y startwith verfican si una cadena de texto termina o inicia (end o start) con una subcadena de texto en especifico. Estos metodos devuelven un booleano,
True si esta la subcadena en el final o inicio (depende del metodo), y False si no lo esta

## Isalpha, Isalnum y Isdigit

Estos metodos tambien devuelven un True y un False, en el caso de Isaplha devuelve un True si solo tiene caracteres alfabeticos, osea solo letras, en el caso de Isalnum devolvera
un True si la cadena solo tiene caracteres alfanumericos, osea solo letras y numeros y para Isdigit lo hara si la cadena tiene solo numeros y tiene al menos un caracter, en caso contrario para todos los metodos devolveran un False

## isspace

Este metodo se utiliza para comprobar si en una cadena todos los caracteres son espacios en blanco, o se puede decir si la cadena esta "vacia" devuelve un True si es asi

## istitle

Este metodo comprueba en la cadena si la primera letra de cada palabra esta en mayuculas y los demas caracteres en minusculas, en caso de que sea asi devuelve un True y si no devolvera un False

## islower y isupper

Estos metodos comprueban si todos los caracteres (alfanumericos) de la cadena estan en minuscula (lower) o estan en mayuscula (upper), si es asi devuelve un True y devolvera un False en caso contrario y en caso de que no hayan caracteres alfanumericos

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
#Procesar el archivo y extraer: Listado de las 50 palabras que más se repiten

def solo_palabras():
    numero_linea = 1
    linea_nueva = " "
    global lista_de_lineas_nuevas
    lista_de_lineas_nuevas = []
    
    for line in file.readlines(): #Recorre todas lineas del archivo
        linea_nueva = "" #Se reinicia la linea_nueva
        for caracter in line: #Recorre todas los caracteres de cada linea
            if 65<=ord(caracter)<=90 or 97<=ord(caracter)<=122: #Verifica si el caracter es una letra
                linea_nueva = linea_nueva + caracter #Si es caracter lo pone en la linea nueva
            else: #Si es algun otro caracter, se reemplaza por un espacio (" ")
                linea_nueva = linea_nueva + " "
            
        lista_de_lineas_nuevas.append(linea_nueva) #Se agrega la linea nueva a la lista de lineas nuevas

        numero_linea += 1 #En cada iteracion del for que recorre las lineas se suma 1
        
    return lista_de_lineas_nuevas
    
def palabras_frecuencia():
    todas_las_palabras = []
    for linea in lista_de_lineas_nuevas:
        palabras = linea.split()  #Divide cada línea de la lista en palabras
        todas_las_palabras.extend(palabras)  #Agrega todas las palabras a una lista mas grande
        
    #Una lista para palabras y otra para frecuencias
    lista_palabras = []
    lista_frecuencias = []
    
    for palabra in todas_las_palabras:
        #Si la palabra ya está en la lista encuentra el índice de la palabra y incrementa su frecuencia en la lista
        if palabra in lista_palabras:  
            indice = lista_palabras.index(palabra) 
            lista_frecuencias[indice] += 1
        else: #Si no esta, añade la palabra a la lista y inicia su contador en 1
            lista_palabras.append(palabra)
            lista_frecuencias.append(1)
    
    #Aca se combinan las 2 listas (la palabra y la frecuencia de esta) en una sola lista (que es una lista de listas)
    lista_palabras_frecuencias = [[lista_palabras[i], lista_frecuencias[i]] for i in range(len(lista_palabras))]

    #Se ordena la lista de listas por el segundo elemento (que son las frecuencias de cada palabra) y se pone de mayor a menor
    palabras_y_frecuencias_ordenadas = sorted(lista_palabras_frecuencias, key=lambda x: x[1], reverse=True)
 
    #Las listas donde se van a guardar las palabras mas repetidas y sus frecuencias en orden
    palabras_mas_frecuentes = []
    frecuencias_palabras = []
    
    #En el bucle se agregan las palabras y las frecuencias a las listas en el orden correspondiente
    for i in palabras_y_frecuencias_ordenadas[0:50]:
        palabras_mas_frecuentes.append(i[0])
        frecuencias_palabras.append(i[1])

    return palabras_mas_frecuentes, frecuencias_palabras

if __name__ == "__main__":
    #Se abre el archivo
    file = open('mbox.txt', "r")
    
    #Se quita del archivo todo lo que no son caracteres de letras y las palabras de cada linea se guardan en una lista
    lista_de_lineas_nuevas = solo_palabras()
    
    palabras_mas_frecuentes, frecuencias_palabras = palabras_frecuencia()
    
    #Con el bucle se muestras las 50 palabras
    indice = 1
    for i in range(50):
        print(f"{indice}. '{palabras_mas_frecuentes[i]}', frecuencia: {frecuencias_palabras[i]}")
        indice += 1
```
