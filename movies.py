
class Movies():
    #Constructor
    def __init__(self,titulo,actores,anio,genero):
        self.titulo = titulo
        self.actores = actores
        self.anio = anio
        self.genero = genero
    
    #Printeo en Pantalla
    def printearInfo(self):
        print('Título: ',self.titulo, " Actores: ",self.actores, " Año De Lanzamiento: ",self.anio, " Genero: ",self.genero)
    
ListaMovies = []
#FUNCION LEER ARCHIVO
def leerarchivo(lista):
    ruta = input('Escriba la ruta del archivo a cargar: ')
    archivo = open(ruta,'r')
    lineas = archivo.readlines()
    

    for line in lineas:
        # Eliminar el carácter de nueva línea al final de la línea
        line = line.strip()
        # Dividir la línea en sus campos utilizando el separador ';'
        campos = line.split(';')
        # Almacenar los campos en variables separadas
        nombre = campos[0]
        actores = campos[1].split(',')
        año = (campos[2])
        genero = [campos[3]]
        # Crear un diccionario para almacenar los datos de la película
        pelicula = {
            'nombre': nombre,
            'actores': actores,
            'año': año,
            'genero': genero
        }
        # Agregar la película a la lista de películas
        ListaMovies.append(pelicula)
        # Imprimir la lista de películas
        print(ListaMovies)

def MostrarPelicula():
    #Recorrer todas las películas y mostrar la información de cada una de ellas
    for pelicula in ListaMovies:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Actores: {', '.join(pelicula['actores'])}")
        print(f"Año: {pelicula['año']}")
        print(f"Género: {pelicula['genero']}")
        print()

def MostrarActores():
    # Mostrar la lista de películas disponibles para seleccionar
    print("Seleccione una película:")
    for i, pelicula in enumerate(ListaMovies):
        print(f"{i+1}. {pelicula['nombre']}")
    # Solicitar al usuario que seleccione una película
    seleccion = input()
    # Mostrar los actores de la película seleccionada
    pelicula_seleccionada = ListaMovies[int(seleccion)-1]
    print(f"Actores de {pelicula_seleccionada['nombre']}:")
    for actor in pelicula_seleccionada['actores']:
        print(actor)

def filtrar_por_actor(actor):
    for pelicula in ListaMovies:
        if actor in pelicula['actores']:
            print(pelicula['nombre'])

def filtrar_por_anio(año):
   for pelicula in ListaMovies:
        if año in pelicula['año']:
            print(pelicula['nombre'],pelicula['genero'])

def filtrar_por_genero(genero):
    for pelicula in ListaMovies:
        if genero in pelicula['genero']:
            print(pelicula['nombre'],pelicula['año'])

def graficar():
    pass
