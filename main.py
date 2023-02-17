from movies import leerarchivo
from movies import MostrarPelicula
from movies import MostrarActores
from movies import filtrar_por_actor
from movies import filtrar_por_anio
from movies import filtrar_por_genero

ListaMovies = []
lista_peliculas = []

print('---------------------------------------')
print('LENGUAJES FORMALES Y DE PROGRAMACION B-')
print('JOSUE DANIEL CHAVEZ PORTILLO')
print('CARNÉ: 202100033')
print('---------------------------------------')
print('')
print('---------------------------------------')
print('BIENVENIDO A CINEFLICK')
print('PRESIONE ENTER PARA CONTINUAR...')
print('---------------------------------------')
input()

op = 0
while op != 5:
    print('---------------------------------------')
    print("MENU PRINCIPAL")
    print("1 Carga")
    print("2 Gestion")
    print("3 Filtro")
    print("4 Grafico")
    print("5 Salir")
    print('---------------------------------------')
    print("1Elija una opcion de 1 a 5:")
    op = int(input())
    if op == 1:
        # CARGA DE ARCHIVOS
        print('----------------CARGA DE ARCHIVOS---------------')
        leerarchivo(ListaMovies)
        print("CARGO EXITOSAMENTE\n")
        input()
    elif op == 2:
        # GESTION
         print('----------------GESTIÓN---------------')
         print('1. Mostrar Peliculas')
         print('2. Mostrar Actores')
         opcion = input("Seleccione una opción:")
         if opcion == "1":
            MostrarPelicula()
            input()
         elif opcion == "2":
            MostrarActores()
            input()
         else:
            print("Opción inválida.")
            input()
    elif op == 3:
        # FILTRO
        print('----------------FILTRO---------------')
        print('1. Filtrar por Actor')
        print('2. Filtrar Por Año')
        print('3. Filtrar Por Genero')
        opcion = input("Seleccione una opción:")
        if opcion == "1":
            filtrar_por_actor()
            input()
        elif opcion == "2":
            filtrar_por_anio()
            input()
        elif opcion == '3':
            filtrar_por_genero()
            input()
        else:
            print("Opción inválida.")
            input()
    elif op == 4:
        # GRAFICO
        print("GRAFICO")
        pass
    elif op == 5:
        # SALIDA
        print("GRACIAS POR PREFERIRNOS!, HASTA LUEGO...")
        break
