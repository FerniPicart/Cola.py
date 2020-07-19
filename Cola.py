from tda_cola_dinamico import Cola, arribo, atencion, cola_vacia, tamanio, frente, mover_final
from tda_dinamico_pila import Pila, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint, choice
from time import sleep
from datetime import datetime
from copy import copy
from math import acos, cos, sin, radians

cola = Cola()
def cola_numerica(cola):
    while tamanio(cola) < 10:
        dato = int(randint(0,50))
        arribo(cola,dato)
    print('cola')
    for i in range (tamanio(cola)):
        print(frente(cola))
        mover_final(cola)
    print('Tamaño cola: ' + str (tamanio(cola)))

def cola_numerica_negativos(cola):
    while tamanio(cola) < 10:
        dato = int(randint(-20,20))
        arribo(cola,dato)
    print('cola')
    for i in range (tamanio(cola)):
        print(frente(cola))
        mover_final(cola)
    print('Tamaño cola: ' + str (tamanio(cola)))

def cola_letras(cola):
    while tamanio(cola) == 0:
        palabra = input('ingrese palabra: ')
        for letra in palabra:
            arribo(cola, letra)
    print('Tamaño cola: ' + str(tamanio(cola)))


#print(cola_numerica(cola))
#print(cola_letras(cola))

#1. Eliminar de una cola de caracteres todas las vocales que aparecen. 
'''
print(cola_letras(cola))
vocales = 'AEIOUaeiou'
for letra in range (tamanio(cola)):
    if (frente(cola) in vocales):
        atencion(cola)
    else:
        mover_final(cola)
print('Cola sin vocales: ')
for i in range (tamanio(cola)):
    print(frente(cola))
    mover_final(cola)
print(str(tamanio(cola)) +' tamanio')
'''
#2. Utilizando operaciones de cola y pila, invertir el contenido de una cola. 
'''
print(cola_numerica(cola))
pila = Pila()
while not cola_vacia(cola):
    x = atencion(cola)
    apilar(pila, x)
print('cola invertida')
while not pila_vacia(pila):
    x = desapilar(pila)
    print(x)
    arribo(cola, x)
'''

#3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo.
'''
cola = Cola()
pila = Pila()
palabra = (input('escriba una cadena de caracteres: '))
while (tamanio(cola) < len(palabra)):
    for i in range(0, len(palabra)):
        arribo(cola, palabra[i])
        apilar(pila, palabra[i])
palindromo = True
while not pila_vacia(pila) and (palindromo == True):
    x = desapilar(pila)
    if (frente(cola) != x):
        palindromo = False
    mover_final(cola)
print('Es palindromo? ' + str(palindromo))
'''

#4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
'''
cola_numerica(cola)
for i in range (tamanio(cola)+1):
    x = frente(cola)
    div = 0
    for j in range (0,x):
        j += 1
        if (x % j == 0):
            div += 1
            if div > 2:
                break
    if div < 3:
        mover_final(cola)
    else:
        atencion(cola)
print('Cola primos')
for i in range (tamanio(cola)):
    print(frente(cola))
    mover_final(cola)
'''

#5. Utilizando operaciones de cola y pila, invertir el contenido de una pila. 
'''
cola = Cola()
pila = Pila()
while tamanio(pila) < 4:
        dato = input('introduce un dato: ')
        apilar(pila, dato)
print('pila')
while not pila_vacia(pila):
    x = desapilar(pila)
    print(x)
    arribo(cola, x)
while not cola_vacia(cola):
    x = atencion(cola)
    apilar(pila, x)
print('pila invertida')
while not pila_vacia(pila):
    x = desapilar(pila)
    print(x)
    arribo(cola, x)
'''
#6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar. 
'''
cola_letras(cola)
bus = input('seleccione elemento a buscar: ')
ocurrencias = 0
for i in range (tamanio(cola)):
    if bus == str(frente(cola)):
        ocurrencias += 1
    mover_final(cola)
print('El objeto buscado aparece ' + str(ocurrencias) + ' veces...')
'''

#7. Eliminar el i-ésimo elemento después del frente de la cola. 
'''
cola_numerica(cola)
elemento = int(input('Ingrese el elemento numerico que quiere eliminar: '))
elim = False
for i in range (tamanio(cola)):
    if elemento == frente(cola):
        x = atencion(cola)
        elim = True
    mover_final(cola)
if (elim == False):
    print('El elemento no ha sido encontrado.')
else:
    print('Se ha eliminado el elemento: ' + str(x))
    print('cola nueva')
    for i in range (tamanio(cola)):
        x = frente(cola)
        print(x)
        mover_final(cola)
    print('Tamaño cola: ' + str(tamanio(cola)))
'''

#8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, 
# utilizando solo una cola como estructura auxiliar. 
'''
while (tamanio(cola) < 10):
    dato = int(input("Ingrese un número "))
    if(cola_vacia(cola)):
        arribo(cola, dato)
    elif(dato < frente(cola)):
        arribo(cola, dato)
        for i in range (1, tamanio(cola)):
            mover_final(cola)
    else:
        cont = 0
        while (frente(cola) < dato and cont < tamanio(cola)):
            mover_final(cola)
            cont += 1
        arribo(cola, dato)
        for i in range(cont, tamanio(cola)-1):
            mover_final(cola)
print('cola ordenada: ')
for i in range (tamanio(cola)):
    x = frente(cola)
    print(x)
    mover_final(cola)
print('Tamaño cola final: ' + str(tamanio(cola)))
'''

#9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.
'''
cola_numerica_negativos(cola)
menor = None
mayor = None
neg = 0
for i in range (tamanio(cola)):
    x = frente(cola)
    mover_final(cola)
    if (mayor == None) and (menor == None):
        mayor = x
        menor = x
    if (x > mayor):
        mayor = x
    if (x < menor):
        menor = x
    if (x < 0):
        neg += 1
print('El mayor de la lista es: ' + str(mayor))
print('El menor de la lista es: ' + str(menor))
print('Hay ' + str(neg) +' cantidad de negativos')
'''
#10. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades: 
#a. mostrar los personajes del planeta Alderaan, Endor y Tatooine 
#b. indicar el plantea natal de Luke Skywalker y Han Solo 
#c. insertar un nuevo personaje antes del maestro Yoda 
#d. eliminar el personaje ubicado después de Jar Jar Binks 
'''
personajes = ['Luke Skywalker', 'Han Solo', 'Maestro Yoda', 'Jar Jar Binks', 'Otro PJ']
planeta = ['Alderaan', 'Endor', 'Tatooine', 'Otro']
while (tamanio(cola) < 10):
    dato = ['','']
    dato[0] = choice(personajes)
    dato[1] = choice(planeta)
    arribo(cola,dato)
print('cola comun')
for i in range (tamanio(cola)):
    x = frente(cola)
    print(x)
    mover_final(cola)
print('--------')
# Pertenecientes a cada planeta
print('Planeta Alderaan')
for i in range (tamanio(cola)):
    if (frente(cola)[1] == 'Alderaan'):
        x = frente(cola)
        print(x)
    mover_final(cola)
print('--------')
print('Planeta Endor')
for i in range (tamanio(cola)):
    if (frente(cola)[1] == 'Endor'):
        x = frente(cola)
        print(x)
    mover_final(cola)
print('--------')
print('planeta Tatooine')
for i in range (tamanio(cola)):
    if (frente(cola)[1] == 'Tatooine'):
        x = frente(cola)
        print(x)
    mover_final(cola)
# Planeta natal de Luke Skywalker y Han Solo 
print('<<<<<<<')
print('Planeta natal de Luke Skywalker y Han Solo: ')
for i in range (tamanio(cola)):
    x = frente(cola)
    if (x[0] == 'Luke Skywalker'):
        print('Planeta natal de Luke Skywalker')
        print(x[1])
    elif (x[0] == 'Han Solo'):
        print('Planeta natal de Han Solo')
        print(x[1])
# nuevo personaje antes del maestro Yoda 
for i in range(tamanio(cola)):
    if (frente(cola)[0] == 'Maestro Yoda'):
        i -= 1
        dato = ['','']
        dato[0] = 'Personaje nuevo'
        dato[1] = 'Otro Planeta'
        arribo(cola,dato)
        print('>>> el personaje fue agregado a la cola <<<')
    mover_final(cola)
# eliminar el personaje ubicado después de Jar Jar Binks
for i in range(tamanio(cola)):
    if frente(cola)[0] == 'Jar Jar Binks':
        mover_final(cola)
        atencion(cola)
    else:
        mover_final(cola)
print('                 ')
print('¡¡¡ Cola Final !!!')
for i in range(tamanio(cola)):
    print(frente(cola))
    mover_final(cola)
'''

# 11. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una nueva cola. 
#Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, ni métodos de ordenamiento. 
'''
cola = Cola()
cola_aux = Cola()
print('cargar primera cola')
while tamanio(cola) < 5:
    dato = int(input("ingrese un número: "))
    arribo(cola, dato)
print('cargar segunda cola')
while tamanio(cola_aux) < 5:
    dato = int(input("ingrese un número: "))
    arribo(cola_aux, dato)
cant = tamanio(cola)
for i in range (0, cant):
    if(frente(cola) < frente(cola_aux)):
        mover_final(cola)
    else:
        while(frente(cola) > frente(cola_aux)):
            dato = atencion(cola_aux)
            arribo(cola, dato)
        mover_final(cola)
while(not cola_vacia(cola_aux)):
    dato = atencion(cola_aux)
    arribo(cola, dato)
for i in range(0, tamanio(cola)):
    print(mover_final(cola))
'''

# 12. Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes actividades: 
# a. separarla en dos colas una con dígitos y otra con el resto de los caracteres. 
# b. determinar cuántas letras hay en la segunda cola.  
# c. determinar además si existen los caracteres “?” y “#”. 
'''
numeros = '0123456789'
letras = 'abcdefghijklmnopqrstuvwxyz'
cola_digitos = Cola()
cola_letras = Cola()
i = 0
while tamanio(cola) < 10:
    i += 1
    dato = randint(0,50)
    arribo(cola,dato)
    aux = choice(letras)
    arribo(cola, aux)
    print(dato)
    print(aux)
for i in range(tamanio(cola)):
    if (str(frente(cola)) in letras):
        arribo(cola_digitos, frente(cola))
        atencion(cola)
    else:
        arribo(cola_letras, frente(cola))
        atencion(cola)
print('cola digitos')
for i in range(tamanio(cola_digitos)):
    print(frente(cola_digitos))
    mover_final(cola_digitos)
print('Tamaño cola digitos ' + str(tamanio(cola_digitos)))
print('Cola letras')
for i in range(tamanio(cola_letras)):
    print(frente(cola_letras))
    mover_final(cola_letras)
print('Tamanio cola letras' + str(tamanio(cola_letras)))
'''

#13 no se hace

# Ej 14.
'''
archivo = open('bases rebeldes')
linea = archivo.readline()
Bases_rebeldes = Cola()
latitud = float(input('Ingrese la latitud desde su punto actual: '))
longitud = float(input('Ingrese la longitud desde su punto actual: '))
punto_actual = [latitud, longitud]
base = ['',0,0,0]
base2 = ['',0,0,0]
mayor_flota = 0
while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = int(linea[1])
    linea[2] = float(linea[2])
    linea[3] = float(linea[3])
    arribo(Bases_rebeldes, linea)
    linea = archivo.readline()
for i in range(tamanio(Bases_rebeldes)):
    lat = frente(Bases_rebeldes)[2]
    lon = frente(Bases_rebeldes)[3]
    puntox = [lat, lon]
    punto_actual = (radians(punto_actual[0]), radians(punto_actual[1]))
    puntox = (radians(puntox[0]), radians(puntox[1]))
    distancia = acos(sin(punto_actual[0])*sin(puntox[0]) + cos(punto_actual[0])*cos(puntox[0])*cos(punto_actual[1] - puntox[1]))
    distancia * 6371.01
    if(i == 0):
        menor_distancia = distancia
        base = frente(Bases_rebeldes)
    elif(distancia < menor_distancia):
        menor_distancia = distancia
        base = frente(Bases_rebeldes)
    if (mayor_flota < frente(Bases_rebeldes)[1]):
        mayor_flota = frente(Bases_rebeldes)[1]
        base2 = frente(Bases_rebeldes)
    mover_final(Bases_rebeldes)
lati = base2[2]
longi = base2[3]
punto_x = [lati, longi]
puntox = (radians(punto_x[0]), radians(punto_x[1]))
distancia1 = acos(sin(punto_actual[0])*sin(punto_x[0]) + cos(punto_actual[0])*cos(punto_x[0])*cos(punto_actual[1] - punto_x[1]))
distancia1 * 6371.01
print('La base rebelde mas cercana es desde su punto actual es',base[0],'con latitud',base[2], 'y con longitud',base[3])
print('La base rebelde con la mayor flota es',base2[0],'con',base2[1],'flota')
print('La distancia entre el punto actual y la base con mayor flota es de',distancia1)
'''

#15. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio 
#(1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la siguiente situación:
#a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
#b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#c. cargue dos documentos del staff de TI.
#d. cargue un documento del gerente.
#e. imprima los dos primeros documentos de la cola.
#f. cargue dos documentos de empleados y uno de gerente.
#g. imprima todos los documentos de la cola de impresión.

'''
nombre = ''
documento = 0
categoria = ''
cola_aux = Cola()
while (tamanio(cola_aux) < 7):
    categoria = input('Ingrese categoria ("empleado", "staff TI", "gerente"): ')

    while (categoria.lower() == 'empleado' and tamanio(cola_aux) < 7):
        nombre = input('Ingrese nombre y apellido: ')
        documento = int(input('Ingrese numero de documento(solo numeros): '))
        dato = [nombre, documento, categoria]
        arribo(cola_aux, dato)
        categoria = input('Ingrese siguiente categoria a cargar("empleados", "staff TI", "gerente"): ')

    while (categoria.lower() == 'staff ti' and tamanio(cola_aux) < 7):
        nombre = input('Ingrese nombre y apellido: ')
        documento = int(input('Ingrese numero de documento(solo numeros): '))
        dato = [nombre, documento, categoria]
        arribo(cola_aux, dato)
        categoria = input('Ingrese siguiente categoria a cargar("empleados", "staff TI", "gerente"): ')

    while (categoria.lower() == 'gerente' and tamanio(cola_aux) < 7):
        nombre = input('Ingrese su nombre y apellido: ')
        documento = int(input('Ingrese su numero de documento(sin puntos): '))
        dato = [nombre, documento, categoria]
        arribo(cola_aux, dato)
        categoria = input('Ingrese siguiente categoria a cargar(empleados, staff TI, gerente): ')

for i in range(tamanio(cola_aux)):
    if (frente(cola_aux)[2].lower() == 'empleado'):
        arribo(cola, frente(cola_aux))
        mover_final(cola_aux)
    else:
        mover_final(cola_aux)
for i in range(tamanio(cola_aux)):
    if (frente(cola_aux)[2].lower() == 'staff ti'):
        arribo(cola, frente(cola_aux))
        mover_final(cola_aux)
    else:
        mover_final(cola_aux)
for i in range(tamanio(cola_aux)):
    if (frente(cola_aux)[2].lower() == 'gerente'):
        arribo(cola, frente(cola_aux))
        mover_final(cola_aux)
    else:
        mover_final(cola_aux)

print('Nombre del primer documento de la cola')
print(frente(cola)[0])
print('Los dos primeros documentos de la cola son ')
for i in range(tamanio(cola)):
    if (i < 2):
        print(frente(cola)[0] + ' : ' + str(frente(cola)[1]))
        mover_final(cola)
    else:
        mover_final(cola)
print('-- Imprimiendo Cola por prioridad --: ')
for i in range(tamanio(cola)):
    print(frente(cola))
    sleep(3)
    mover_final(cola)
'''
# 16. Desarrollar un algoritmo que permita cargar procesos a la cola de ejecución de un procesador, de los 
# cuales se conoce id del proceso y tiempo de ejecución. Resuelva lassiguientes situaciones:
# a. simular la atención de los procesos de la cola transcurriendo su tiempo –utilizando la 
# función time.sleep (segundos) – hasta que se vacíe la cola.
# b. considerar que el quantum de tiempo asignado por el procesador a cada proceso es como máximo 
# 4.5 segundos –si el proceso no terminó su ejecución deberá volver a la cola con el tiempo restante para 
# terminar su ejecución–.
# c. cuando se realiza el cambio de proceso, porque finalizó su ejecución o porque se le agotó el 
# quantum de tiempo, se pueden ingresar nuevos procesos a la cola por el usuario.
# d. no se aplican criterios de prioridad en los procesos.
'''
id = 0
while tamanio(cola) < 7:
    id += 1
    dato =[0,0]
    dato[0] = id
    dato[1] = randint(1,8)
    arribo(cola, dato)

while not cola_vacia(cola):
    if (frente(cola)[1] > 4.5 ):
        sleep(4.5)
        frente(cola)[1] -= 4.5
        print('el proceso '+ str(frente(cola)[0]) +' fue arribado por exceso de tiempo ')
        mover_final(cola)
    else:
        sleep(frente(cola)[1])
        x = atencion(cola)
        print(x)
    # agregar?
    otro = input('Quiere agregar otro proceso a la cola? Si/No: ')
    if (otro.lower() == 'si'):
        id += 1
        dato[0] = id
        dato[1] = randint(1,8)
'''

#17. Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una letra de 
# la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo que resuelva 
# las siguientes situaciones:
# a. cargar 1000 turnos de manera aleatoria a la cola.
# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C y F, y 
# la cola_2 con el resto de los turnos (B, D y E).
# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras tiene mayor cantidad.
# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea mayor que 506.
'''
letras = ['A','B','C','D','E','F']
cola_ACF = Cola()
cola_BDE = Cola()
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
while tamanio(cola) < 10: #00 :
    dato = ['',0]
    dato[0] = choice(letras)
    dato[1] = randint(0,999)
    arribo(cola,dato)

print('Cola de turnos mayores a 506:')
while not cola_vacia(cola):
    if frente(cola)[1] > (506):
        print(frente(cola))
    # Separo colas
    if (frente(cola)[0] in 'ACF'):
        if frente(cola)[0] == 'A':
            A += 1
        elif frente(cola)[0] == 'C':
            C += 1
        else:
            F += 1
        x = atencion(cola)
        arribo(cola_ACF, x)
    else:
        if frente(cola)[0] == 'B':
            B += 1
        elif frente(cola)[0] == 'D':
            D += 1
        else:
            E += 1
        x = atencion(cola)
        arribo(cola_BDE, x)

if tamanio(cola_ACF) < tamanio(cola_BDE):
    print('La cola de mayor tamaño es "Cola_BDE" con: '+ str(tamanio(cola_BDE)))
    if (B > D) and (B > E):
        print('"B" es la letra con mayor cantidad de turnos: ' + str(B))
    elif D > E:
        print('"D" es la letra con mayor cantidad de turnos: ' + str(D))
    else:
        print('"E" es la letra con mayor cantidad de turnos: ' + str(E))
else:
    print('La cola de mayor tamaño es "Cola_ACF" con: '+ str(tamanio(cola_ACF)))
    if (A > C) and (A > F):
        print('"A" es la letra con mayor cantidad de turnos: ' + str(A))
    elif (C > F):
        print('"C" es la letra con mayor cantidad de turnos: ' + str(C))
    else:
        print('"F" es la letra con mayor cantidad de turnos: ' + str(F))
'''
# 18 no se hace.

# 19. Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de
# cobro), que resuelva las siguientes actividades:
# a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son los siguientes:
# i. automóviles (tarifa $47);
# ii. camionetas (tarifa $59);
# iii. camiones (tarifa $71);
# iv. colectivos (tarifa $64).
# b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
# c. determinar qué cabina recaudó mayor cantidad de pesos ($).
# d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.
'''
vehiculos = ['automovil', 'camioneta', 'camion', 'colectivo']
costo = [45, 60, 70, 65]
puesto_1 = Cola()
puesto_2 = Cola()
puesto_3 = Cola()
cant_1  = [0, 0, 0, 0]
cant_2  = [0, 0, 0, 0]
cant_3  = [0, 0, 0, 0]
total_1 = 0
total_2 = 0
total_3 = 0

for i in range (30):
    arribo(puesto_1, (choice(vehiculos)))
    arribo(puesto_2, (choice(vehiculos)))
    arribo(puesto_3, (choice(vehiculos)))
while (not cola_vacia(puesto_1)):
    veh = atencion(puesto_1)
    pos = vehiculos.index(veh)
    total_1 += costo[pos]
    cant_1[pos] += 1
while(not cola_vacia(puesto_2)):
    veh = atencion(puesto_2)
    pos = vehiculos.index(veh)
    total_2 += costo[pos]
    cant_2[pos] += 1
while(not cola_vacia(puesto_3)):
    veh = atencion(puesto_3)
    pos = vehiculos.index(veh)
    total_3 += costo[pos]
    cant_3[pos] += 1
print('')

if ((total_1 > total_2) and (total_1 > total_3)):
    print("La cabina nro 1 es la que recaudo mas cantidad de dinero.")
elif (total_2 > total_3):
    print("La cabina nro 2 es la que recaudo mas cantidad de dinero.")
else:
    print("La cabina nro 3 es la que recaudo mas cantidad de dinero.")
print('Cabina 1 recaudo: '+ str(total_1))
print('Cabina 2 recaudo: '+ str(total_2))
print('Cabina 3 recaudo: '+ str(total_3))

print('')
print('--- Cuántos vehículos de cada tipo se atendieron en cada cola ---')
print("La cabina 1 atendio: " + str(cant_1[0]) + " autos, " + str(cant_1[1]) + " camionetas, " + str(cant_1[2]) + " camiones y " + str(cant_1[3]) + " colectivos.")
print("La cabina 2 atendio: " + str(cant_2[0]) + " autos, " + str(cant_2[1]) + " camionetas, " + str(cant_2[2]) + " camiones y " + str(cant_2[3])+ " colectivos.")
print("La cabina 3 atendio: " + str(cant_3[0]) + " autos, " + str(cant_3[1]) + " camionetas, " + str(cant_3[2]) + " camiones y " + str(cant_3[3]) + " colectivos.")
'''

#20. Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un
# aeropuerto que tiene una pista, contemplando las siguientes actividades:
# a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada,
# aeropuerto de origen, aeropuerto de destino y su tipo (pasajeros, negocios o carga).
# b. utilizar una cola para administrar los despegues, se deben cargan ordenados porh
# horario de salida. Otra para los aterrizajes, se deben agregan a medida que arribanal aeropuerto.
# c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o despegue.
# d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas 
# colas después de realizar una atención.
# e. se debe atender siempre que se pueda a los elementos de la cola de aterrizaje –dado que son aviones 
# que están sobrevolando en la zona de espera–, salvo que sea el horario de salida del primer 
# avión de la cola de despegue, en ese caso sedeberá atender dicho despegue.
# f. cada tipo de avión tiene su tiempo de uso de la pista para la maniobra de
# despegue y aterrizaje –adaptados a segundo para los fines prácticos del ejercicio–:
# i. pasajeros (aterrizaje = 10 segundos, despegue = 5 segundos);
# ii. negocios (aterrizaje = 5 segundos, despegue = 3 segundos);
# iii. carga (aterrizaje = 12 segundos, despegue = 9 segundos).
# g. se debe poder cancelar vuelos de despegue y poder reprogramar un vuelo para más tarde cuando se 
# lo atiende para despegar (en esta caso el horario de salida será mayor que el último de la cola).
'''
tipos_aviones = ['carga', 'negocios', 'pasajeros']
tiempo_despegue = [9, 3, 5]
tiempo_aterrizaje = [12, 5, 10]
c_despegue = Cola()
c_aterrizaje = Cola()
arribo(c_despegue, ['airline', 'argentina', 'chile', 'carga', '07:00', '23:00'])
arribo(c_despegue, ['airline', 'argentina', 'india', 'pasajeros', '07:10', '23:00'])
arribo(c_despegue, ['airline', 'argentina', 'rusia', 'negocios', '07:17', '23:00'])
arribo(c_aterrizaje, ['airline', 'argentina', 'rusia', 'negocios', '07:00', '23:00'])

hora_actual = datetime.now()
while(not cola_vacia(c_despegue) or not cola_vacia(c_aterrizaje)):
    hora_despegue = copy(hora_actual)
    hora_despegue.hour = int(frente(c_despegue)[4][0:2])
    hora_despegue.min =int(frente(c_despegue)[4][3:])
    if(not cola_vacia(c_aterrizaje) and hora_despegue<= hora_actual):
        avion = atencion(c_aterrizaje)
        pos = tipos_aviones.index(avion[3])
        tiempo = tiempo_aterrizaje[pos]
        print('avion aterrizando...')
        sleep(tiempo)
    else:
        avion = atencion(c_despegue)
        pos = tipos_aviones.index(avion[3])
        tiempo = tiempo_despegue[pos]
        print('avion despegando...')
        sleep(tiempo)
hora_actual = datetime().now()

si_no = None
while si_no == None:
    si_no = str(input("Desea seguir ingresando vuelos?  -si/no-: "))
    if (si_no != 'si') or (si_no != 'no'):
        si_no = None
if (si_no == "si"):
    tip = None
    while tip == None:
        tip = str(input("Ingrese el tipo de vuelo:  -despegue/aterrizaje-: "))
        if tip != 'despegue' or (tip != 'aterrizaje'):
            tip = None
    if (tip == "despegue"):
        i = str(input("Ingrese el NOMBRE de la aerolínea: "))
        j = str(input("Ingrese el aeropuerto de ORIGEN: "))
        k = str(input("Ingrese el aeropuerto de DESTINO: "))
        l = (choice(tipos_aviones))
        pos = tipos_aviones.index(l)
        m = tiempo_despegue[pos]
        n = tiempo_aterrizaje[pos]
        dato = [i,j,k,l,m,n]
        arribo(c_despegue,dato)
        print()
    elif (tip == "aterrizaje"):
        i = str(input("Ingrese el NOMBRE de la aerolínea: "))
        j = str(input("Ingrese el aeropuerto de ORIGEN: "))
        k = str(input("Ingrese el aeropuerto de DESTINO: "))
        l = (choice(tipos_aviones))
        pos = tipos_aviones.index(l)
        m = tiempo_despegue[pos]
        n = tiempo_aterrizaje[pos]
        dato = [i,j,k,l,m,n]
        arribo(c_aterrizaje,dato)
        print()
'''
# 21. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce 
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo :
# {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M},
# {Natasha Romanoff, Black Widow, F}, etc., 
# desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
'''
personajes = [['Tony Stark','Iron Man','M'],['Steve Rogers','Capitán América','M'],['Natasha Romanoff', 'Black Widow', 'F'],
                ['Brie Larson','Capitana Marvel','F'],['Scott Lang','Ant-Man','M'],['Tom Holland','Spider-Man','M']]

print('---Personajes COLA---')
for i in range (len(personajes)):
    dato = personajes[i]
    arribo(cola, dato)
    print(dato)

cd = False
print('')
for i in range(tamanio(cola)):
    if (frente(cola)[1] == "Capitana Marvel"):
        print('El nombre real de "Capitana Marvel" es: ' + frente(cola)[0])
    if (frente(cola)[0] == "Scott Lang"):
        print('El nombre del SuperHeroe de "Scott Lang" es: ' + frente(cola)[1])
    if(frente(cola)[0] == "Carol Danvers"):
        cd = True
        pj = frente(cola)[1]
    mover_final(cola)
print('')
print('Superheroes femeninos: ')
for i in range(tamanio(cola)):
    if (frente(cola)[2] == "F"): 
        print(frente(cola))
    mover_final(cola)
print('')
print("Superheroes masculinos:")
for i in range(tamanio(cola)):
    if (frente(cola)[2] == "M"): 
        print(frente(cola))
    mover_final(cola)
print('')
if cd == True:
    print('Carol Danvers se encuentra en la cola y el nombre de su superheroe es: \n' + pj)
else:
    print("El personaje Carol Danvers no se encuentra en la cola")
'''