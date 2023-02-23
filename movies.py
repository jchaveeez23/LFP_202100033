import graphviz
import random
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
    # Crear el grafo
    graph = graphviz.Digraph()

    # Agregar los nodos y aristas
    graph.node('The Avengers', shape='hexagon', style='filled', fillcolor='lightblue')
    graph.node('Año 2012', shape='pentagon', style='filled', fillcolor='pink')
    graph.node('Año 2014', shape='pentagon', style='filled', fillcolor='pink')
    graph.node('Año 2018', shape='pentagon', style='filled', fillcolor='pink')
    graph.node('Año 2002', shape='pentagon', style='filled', fillcolor='pink')
    graph.node('Año 2017', shape='pentagon', style='filled', fillcolor='pink')
    graph.edge('The Avengers','Robert Downey Jr',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('The Avengers', 'Chris Evans',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('The Avengers', 'Chris Hemsworth',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Año 2012', 'The Avengers',color=random.choice(['red', 'orange', 'blue']))
    graph.node('Spiderman', shape='hexagon', style='filled', fillcolor='lightblue')
    graph.edge('Spiderman', 'Tobey Maguire',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Spiderman', 'Kirsten Dunst',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Spiderman', 'Willem Dafoe',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Año 2002', 'Spiderman',color=random.choice(['red', 'orange', 'blue']))
    graph.node('The Amazing Spiderman', shape='hexagon', style='filled', fillcolor='lightblue')
    graph.edge('The Amazing Spiderman', 'Andrew Garfield',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('The Amazing Spiderman', 'Emma Stone',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Año 2012', 'The Amazing Spiderman',color=random.choice(['red', 'orange', 'blue']))
    graph.node('The Amazing Spiderman 2', shape='hexagon', style='filled', fillcolor='lightblue')
    graph.edge('The Amazing Spiderman 2', 'Andrew Garfield',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('The Amazing Spiderman 2', 'Emma Stone',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Año 2014', 'The Amazing Spiderman 2',color=random.choice(['red', 'orange', 'blue']))
    graph.node('Spiderman Homecoming', shape='hexagon', style='filled', fillcolor='lightblue')
    graph.edge('Spiderman Homecoming', 'Tom Holland',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Spiderman Homecoming', 'Zendaya',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Año 2017', 'Spiderman Homecoming',color=random.choice(['red', 'orange', 'blue']))
    graph.node('Avengers Infinity War', shape='hexagon', style='filled', fillcolor='lightblue')
    graph.edge('Avengers Infinity War', 'Robert Downey Jr',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Avengers Infinity War', 'Tom Holland',color=random.choice(['red', 'orange', 'blue']))
    graph.edge('Año 2018', 'Avengers Infinity War',color=random.choice(['red', 'orange', 'blue']))

    # Establecer los atributos del grafo
    graph.attr('graph')
    graph.attr('node', shape='rectangle')
    graph.attr('edge', dir='none')

    # Generar el archivo PDF
    graph.render('grafo', format='pdf')
    graph.view()






