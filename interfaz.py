from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from movies import Movies
import csv
import re
# PANTALLA INICIAL DEL PROGRAMA 
ventana_principal = Tk()
ventana_principal.title("Practica1")
ventana_principal.geometry("380x320+500+130") 
nom_curso = Label(ventana_principal, text="Nombre del curso: Lenguajes Formales y de Programación B-").grid(row=1, column=1, pady=7, columnspan=5, ipadx=30)
nom_est = Label(ventana_principal, text="Nombre del estudiante: Josué Daniel Chavez Portillo").grid(row=2, column=1, pady=7, columnspan=3, ipadx=30)
carnet = Label(ventana_principal, text="Carnet del estudiante: 202100033").grid(row=3, column=1, pady=7, ipadx=7)
contenedor_movies,uni,unicos = [],[],[]
arch = StringVar()

#VENTANA PARA CARGAR ARCHIVO
def seleccionar_archivo():
    ventana_principal.withdraw()
    ventana_cargar = Toplevel()
    ventana_cargar.title("Seleccionar archivo")
    ventana_cargar.geometry("400x190+500+150")
    regex1 = re.compile(r'[0-9]{1,}')
    def regresar():
        ventana_cargar.withdraw()
        ventana_principal.deiconify()
    def Cargar_archivo():
        try:
            if arch.get() == '': 
                mensaje_espacio = messagebox.showerror(title="Mensaje de Alerta", message="No puede dejar en blanco el cuadro de texto")
            else: 
                archivo_csv = open(arch.get(), 'r', encoding='UTF-8')
                lector = csv.reader(archivo_csv, delimiter=",")
                arch.set("")
                msg = 0
                for linea in lector:
                    try:
                        titulo,actor1,actor2,actor3,anio,genero = linea[0],linea[1],linea[2],linea[3],int(linea[4]),linea[5]
                        info = Movies(titulo,actor1,actor2,actor3,anio,genero)
                    except: mensaje_espacio = messagebox.showerror(title="Mensaje de Alerta", message="El Año debe ser un valor numerico por ende la Pelicula: " + titulo + " no se ha agregado")
                    if anio <=2023:
                        contenedor_movies.append(info)                
                        print('agregada')
                        msg = 0
                    else:
                        mensaje_estat = messagebox.showerror(title="Mensaje de Alerta", message="El Año esta fuera de rango por lo tanto la pelicula no se ha agregado")
                if msg == 0:
                    mensaje_exito = messagebox.showinfo(title="Mensaje de notificación", message="La carga de archivos ha sido satisfactoria")
                print(len(contenedor_movies))
                count = 0
                for i in contenedor_movies:
                    tit = contenedor_movies[count].get_titulo()
                    uni.append(tit)
                    count += 1
                print(len(contenedor_movies))
                archivo_csv.close() 
        except FileNotFoundError:     
            arch_no_encontrado = messagebox.showerror(title="Mensaje de Error", message="No se ha encontrado la ruta del archivo ingresado")                    
            arch.set("")
    label_ruta = Label(ventana_cargar, text="Ruta").place(x=80, y =40) 
    archivo_ruta = Entry(ventana_cargar, textvariable=arch, width=30).place(x=150, y =40)
    btn_seleccionar = Button(ventana_cargar, text="Seleccionar", command=Cargar_archivo).place(x=160, y =120)
    btn_regresar = Button(ventana_cargar, text="Regresar", command=regresar).place(x=280, y=120)

#VENTANA PARA GESTIONAR PELICULAS
def Gestionar_pelis():
    ventana_principal.withdraw()
    ventana_pelis = Toplevel()
    ventana_pelis.title("Gestionar Peliculas")
    ventana_pelis.geometry("380x340+500+130")
    def regresar2():
        ventana_pelis.withdraw()
        ventana_principal.deiconify()
    def Mostrar_pelis():
        ventana_pelis.withdraw()
        ventana_mp = Toplevel()
        ventana_mp.title('Mostar Peliculas')
        ventana_mp.geometry("490x390+500+150")
        tit,a1,a2,a3,year,gen =  StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
        def regre():
            ventana_mp.withdraw()
            ventana_pelis.deiconify()
        def serch():
            titulo = tit.get()
            count_mp = 0
            v_mp = 1
            for linea in contenedor_movies:
                valor_tit = contenedor_movies[count_mp].get_titulo()
                count_mp += 1
                v_mp = 0
                if titulo == valor_tit:
                    a1.set(contenedor_movies[count_mp-1].get_actor1())
                    a2.set(contenedor_movies[count_mp-1].get_actor2())
                    a3.set(contenedor_movies[count_mp-1].get_actor3())
                    year.set(contenedor_movies[count_mp-1].get_anio())
                    gen.set(contenedor_movies[count_mp-1].get_genero())
                    campo_titulo.config(state=DISABLED)
                    btn_busc.config(state=DISABLED)
                    break
                else:
                    v_mp = 1
            if v_mp == 1:
                mensaje_error = messagebox.showerror(title="Mensaje de Error", message="La Pelicula No está registrada")
                tit.set("")
        label_titulo = Label(ventana_mp, text="Titulo de la Pelicula").place(x=50, y=30)
        campo_titulo = Entry(ventana_mp, width=30, textvariable=tit)
        campo_titulo.place(x=180, y=30)
        campo_titulo.config(state=NORMAL)

        label_a1 = Label(ventana_mp, text="Actor").place(x=50, y=70)
        campo_a1 = Entry(ventana_mp, state=DISABLED, width=30, textvariable=a1).place(x=180, y=70)

        label_a2 = Label(ventana_mp, text="Actor").place(x=50, y=110)
        campo_a2 = Entry(ventana_mp, state=DISABLED, width=30, textvariable=a2).place(x=180, y=110)

        label_a3 = Label(ventana_mp, text="Actor").place(x=50, y=150)
        campo_a3 = Entry(ventana_mp, state=DISABLED, width=30, textvariable=a3).place(x=180, y=150)

        label_anio = Label(ventana_mp, text="Año").place(x=50, y=190)
        campo_anio = Entry(ventana_mp, state=DISABLED, width=30, textvariable=year).place(x=180, y=190)

        label_gen = Label(ventana_mp, text="Genero").place(x=50, y=230)
        campo_gen = Entry(ventana_mp, state=DISABLED, width=30, textvariable=gen).place(x=180, y=230)

        def Mostrar_actores():
            pass


        btn_busc = Button(ventana_mp, text="Buscar", command= serch, width=9)
        btn_busc.place(x=380, y=25)
        btn_busc.config(state=NORMAL)
        btn_regr = Button(ventana_mp, text="Regresar", command= regre, width=9).place(x=315, y=330)
    
    btn_mostrarpelis = Button(ventana_pelis,text="Mostrar Peliculas", command=Mostrar_pelis).place(x=160, y =25)
    btn_mostraractores = Button(ventana_pelis,text="Mostrar Curso", command=Mostrar_pelis).place(x=160, y=75)
    btn_regresar2 = Button(ventana_pelis,text="Regresar", command=regresar2).place(x=160, y=125)



def salir_programa():
    ventana_principal.destroy() 
# AQUI TODOS LOS VALORES PERTENECEN A LA PRIMERA VENTANA, LA VENTANA PRINCIPAL
btn_cargar = Button(ventana_principal, text="Cargar archivo", command=seleccionar_archivo)
btn_cargar.grid(row=9, column=1, padx=90, pady= 15, columnspan=6)
btn_gestionar = Button(ventana_principal, text="Gestionar Cursos", command=Gestionar_pelis)
btn_gestionar.grid(row=10, column=1, padx=90, pady= 5, columnspan=6)
btn_salir = Button(ventana_principal, text="Salir", command=salir_programa)
btn_salir.grid(row=12, column=1, padx=90, pady= 5, columnspan=6)
btn_salir.config(width=10)
ventana_principal.mainloop() # ESTA LINEA DE CÓDIGO SIEMPRE DEBE IR HASTA ABAJO