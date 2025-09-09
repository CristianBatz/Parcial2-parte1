import tkinter as tk

class Candidatas:
    def __init__(self, codigo, nombre, edad, institucion, municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.institucion = institucion
        self.municipio = municipio

    def mostrar_info(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Edad: {self.edad}"


class GestionCandidata:
    def __init__(self, concurso):
        self.concurso = concurso
        self.cargar_Candidatas()

    def cargar_Candidatas(self):
        try:
            with open("candidatas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo, nombre, edad, institucion, municipio = linea.split(";")
                        self.concurso.agregar_candidata(
                            codigo, nombre, int(edad), institucion, municipio
                        )
            print("Candidatas cargadas.")
        except FileNotFoundError:
            print("No existe el archivo candidatas.txt, se creará al guardar.")

    def guardar_candidata(self):
        with open("candidatas.txt", "w", encoding="utf-8") as archivo:
            for codigo, data in self.concurso.candidata.items():
                archivo.write(
                    f"{codigo};{data['nombre']};{data['edad']};{data['institucion']};{data['municipio']}\n"
                )
    def agregar_candidata(self):
        print("Ingrese los datos de la candidata:")
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))

        if not (20 <= edad <= 30):
            print(f"La candidata no puede participar por tener la edad de {edad}")
            return

        institucion = input("Institución: ")
        municipio = input("Municipio: ")

        self.concurso.agregar_candidata(codigo, nombre, edad, institucion, municipio)
        self.guardar_candidata()
        print(f"Candidata {nombre} registrada con éxito.")

    def mostrar_info(self):
        if not self.concurso.candidata:
            print("No hay candidatas registradas")
        else:
            for codigo, data in self.concurso.candidata.items():
                print(f"Codigo: {codigo} | Nombre: {data['nombre']} | Edad: {data['edad']} | Institución: {data['institucion']} | Municipio: {data['municipio']}")

class Jurado:
    criterios = ["cultura", "proyecciones", "entrevista"]

    def __init__(self, concurso):
        self.concurso = concurso
        self.cargar_jurado()

    def cargar_jurado(self):
        try:
            with open("Jurado.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nombre, especialidad = linea.split(";")
                        self.concurso.agregar_jurado(nombre, especialidad)
            print("Jurados cargados.")
        except FileNotFoundError:
            print("No existe el archivo Jurado.txt, se creará uno nuevo al guardar.")

    def guardar_jurado(self):
        with open("Jurado.txt", "w", encoding="utf-8") as archivo:
            for nombre, data in self.concurso.jurado.items():
                archivo.write(f"{nombre};{data['especialidad']}\n")

    def registro_puntaje(self, nombre_jurado, codigo_candidata):
        print(f"Registrando puntuajes de {nombre_jurado} para candidata {codigo_candidata}")
        try:
            cultura = int(input("Puntaje cultura: "))
            proyeccion = int(input("Puntaje proyecciones: "))
            entrevista = int(input("Puntaje entrevista: "))
            self.concurso.agregar_puntaje(nombre_jurado, codigo_candidata, cultura, proyeccion, entrevista)
        except ValueError:
            print("Error: ingrese solo números enteros para los puntajes.")

class Calificacion:
    def __init__(self,jurado,candidata, cultura,proyeccion,entrevista):
        self.jurado = jurado
        self.candidata = candidata
        self.cultura = cultura
        self.proyeccion = proyeccion
        self.entrevista = entrevista

    def calcular_promedio(self):
        return (self.cultura + self.proyeccion + self.entrevista) / 3

class Concurso:
    def __init__(self):
        self.jurado = {}
        self.candidata = {}
        self.calificaciones = []

    def agregar_candidata(self,codigo, nombre, edad, institucion, municipio):
        self.candidata[codigo]={
            "nombre": nombre,
            "edad": edad,
            "institucion": institucion,
            "municipio": municipio,
            "calificaciones": []
        }


    def agregar_jurado(self,nombre,especialidad):
        self.jurado[nombre]={
            "especialidad": especialidad
        }

    def agregar_puntaje(self,nombre_jurado, codigo_candidata, cultura, proyeccion, entrevista):
        if nombre_jurado not in self.jurado:
            print(f"Jurado {nombre_jurado} no esta registrado")
            return

        if codigo_candidata not in self.candidata:
            print(f"La candidata {codigo_candidata} no esta registrada")
            return

        jurado_info = self.jurado[nombre_jurado]
        candidata_info = self.candidata[codigo_candidata]

        calificacion = Calificacion(jurado_info, candidata_info, cultura, proyeccion, entrevista)

        self.candidata[codigo_candidata]["calificaciones"].append(calificacion)

    def puntaje_total_candidata(self, codigo):
        calificaciones_total = self.candidata[codigo]["calificaciones"]
        if not calificaciones_total:
            return 0
        total = sum(c.calcular_promedio() for c in calificaciones_total)
        return total / len(calificaciones_total)

    def mostrar_ranking(self):
        ranking = []
        for codigo in self.candidata:
            nombre = self.candidata[codigo]["nombre"]
            puntaje = self.puntaje_total_candidata(codigo)
            ranking.append((nombre, puntaje))

        ordenamiento = Ordenamiento()
        ranking_ordenado = ordenamiento.quick_sort(ranking)

        if not ranking_ordenado:
            print("No hay candidatas registradas en el ranking.")
            return

        print("=== Ranking ===")
        for i,(nombre,puntaje) in enumerate(ranking_ordenado,start = 1):
            print(f"{i},{nombre}, Puntaje {puntaje:.2f}")

        if ranking_ordenado:
            print(f"\n🏆 GANADORA: {ranking_ordenado[0][0]} con {ranking_ordenado[0][1]:.2f} puntos")


class Ordenamiento:
    def quick_sort(self,candidata):
        if len(candidata) <= 1:
            return candidata

        pivote = candidata[0]
        mayores = [b for b in candidata[1:] if b[1] > pivote[1]]
        iguales = [b for b in candidata[1:] if b[1] == pivote[1]]
        menores = [b for b in candidata[1:] if b[1] < pivote[1]]

        return self.quick_sort(mayores) + [pivote] + iguales + self.quick_sort(menores)

class ConcursoApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Reinas de Independencia - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()
        self.concurso = Concurso()
        self.gestion_candidata = GestionCandidata(self.concurso)
        self.gestion_jurado = Jurado(self.concurso)

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Reinas de Independencia\nConcurso 2025- Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir candidata", command=self.inscribir_candidata)
        opciones.add_command(label="Registrar jurado", command=self.inscribir_jurado)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Candidatas", command=self.listar_candidatas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_candidata(self):
        print("Se abrió la ventana: Inscribir candidata")
        ventana_inscripcion1 = tk.Toplevel(self.ventana)
        ventana_inscripcion1.title("Inscribir candidata")
        ventana_inscripcion1.geometry("450x300")
        tk.Label(ventana_inscripcion1,text="Nombre de la candidata").place(x=30, y=30)
        entrada_nombre = tk.Entry(ventana_inscripcion1)
        entrada_nombre.place(x=180, y=30)

        tk.Label(ventana_inscripcion1,text="Edad de la candidata").place(x=30, y=70)
        entrada_edad = tk.Entry(ventana_inscripcion1)
        entrada_edad.place(x=180, y=70)

        tk.Label(ventana_inscripcion1,text="Instituto de la candidata").place(x=30, y=110)
        instituto = tk.Entry(ventana_inscripcion1)
        instituto.place(x=180, y=110)

        tk.Label(ventana_inscripcion1,text="Municipio de la candidata").place(x=30, y=150)
        municipio = tk.Entry(ventana_inscripcion1)
        municipio.place(x=180, y=150)

        def guardar():
            nombre = entrada_nombre.get()
            try:
                edad = int(entrada_edad.get())
            except ValueError:
                print("Edad inválida")
                return
            institucion = instituto.get()
            municipios = municipio.get()

            if not (20 <= edad <= 30):
                print(f"La candidata no puede participar por tener {edad} años")
                return

            codigo = str(len(self.concurso.candidata) + 1)  # autogenerado
            self.concurso.agregar_candidata(codigo, nombre, edad, institucion, municipio)
            self.gestion_candidata.guardar_candidata()
            print(f"Candidata inscrita: {nombre}")
            ventana_inscripcion1.destroy()

        tk.Button(ventana_inscripcion1, text="Guardar", command=guardar,bg="#4a90e2", relief="raised", bd=4,activebackground="#357ABD", activeforeground="white").place(x=200, y=200)

    def inscribir_jurado(self):
        print("Se abrio la ventana: Registrar Jurado")
        ventana_inscripcion2 = tk.Toplevel(self.ventana)
        ventana_inscripcion2.title("Registrar Jurado")
        ventana_inscripcion2.geometry("500x300")
        tk.Label(ventana_inscripcion2,text="Nombre del jurado").pack(pady=5)
        entrada_nombre = tk.Entry(ventana_inscripcion2)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_inscripcion2,text="Especialidad del jurado").pack(pady=5)
        entrada_especialidad = tk.Entry(ventana_inscripcion2)
        entrada_especialidad.pack(pady=5)

        def guardar():
            nombre = entrada_nombre.get()
            especialidad = entrada_especialidad.get()
            self.concurso.agregar_jurado(nombre, especialidad)
            self.gestion_jurado.guardar_jurado()
            print(f"Jurado inscrito: {nombre}")
            ventana_inscripcion2.destroy()

        tk.Button(ventana_inscripcion2, text="Guardar", command=guardar,
                  bg="#4a90e2", relief="raised", bd=4,
                  activebackground="#357ABD", activeforeground="white").pack(pady = 5)

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_inscripcion3 = tk.Toplevel(self.ventana)
        ventana_inscripcion3.title("Registrar evaluacion")
        ventana_inscripcion3.geometry("500x350")
        tk.Label(ventana_inscripcion3, text="Nombre del jurado").pack(pady=5)
        entrada_jurado = tk.Entry(ventana_inscripcion3)
        entrada_jurado.pack()

        tk.Label(ventana_inscripcion3, text="Código de la candidata").pack(pady=5)
        entrada_codigo = tk.Entry(ventana_inscripcion3)
        entrada_codigo.pack()

        tk.Label(ventana_inscripcion3,text="Puntuacion Cultura").pack(pady=5)
        entrada_Cultura = tk.Entry(ventana_inscripcion3)
        entrada_Cultura.pack(pady=5)

        tk.Label(ventana_inscripcion3,text="Puntuacion Proyecciones").pack(pady=5)
        entrada_Proyecciones = tk.Entry(ventana_inscripcion3)
        entrada_Proyecciones.pack(pady=5)

        tk.Label(ventana_inscripcion3,text="Puntuacion Entrevista").pack(pady=5)
        entrada_entrevista = tk.Entry(ventana_inscripcion3)
        entrada_entrevista.pack(pady=5)

        def guardar():
            nombre_jurado = entrada_jurado.get()
            codigo_candidata = entrada_codigo.get()
            try:
                cultura = int(entrada_Cultura.get())
                proyeccion = int(entrada_Proyecciones.get())
                entrevista = int(entrada_entrevista.get())
                self.concurso.agregar_puntaje(nombre_jurado, codigo_candidata, cultura, proyeccion, entrevista)
                print(f"Evaluación registrada para candidata {codigo_candidata}")
            except ValueError:
                print("Error: ingrese solo números")

            ventana_inscripcion3.destroy()

        tk.Button(ventana_inscripcion3, text="Guardar", command=guardar,bg="#4a90e2", relief="raised", bd=4,activebackground="#357ABD", activeforeground="white").pack(pady=10)



    def listar_candidatas(self):
        print("Se abrió la ventana: Listado de candidatas")
        ventana_listar = tk.Toplevel(self.ventana)
        ventana_listar.title("Listado de Candidatas")
        ventana_listar.geometry("500x400")

        tk.Label(ventana_listar,text="--- Candidatas Inscritas ---",font=("Arial", 12, "bold")).pack(pady=5)

        if not self.concurso.candidata:
            tk.Label(ventana_listar, text="No hay candidatas registradas.").pack()
        else:
            for c in self.concurso.candidata.values():
                info = f"Código: {c.codigo}, Nombre: {c.nombre}, Edad: {c.edad}, Institución: {c.institucion}, Municipio: {c.municipio}, Puntaje: {c.promedio}"
                tk.Label(ventana_listar, text=info,).pack(pady=2)

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking de Candidatas")
        ventana_ranking.geometry("500x400")

        tk.Label(ventana_ranking,text="--- Ranking Final ---",font=("Arial", 12, "bold")).pack(pady=5)

        if not self.concurso.candidata:
            tk.Label(ventana_ranking, text="No hay candidatas evaluadas.").pack()
        else:
            ordenador = Ordenamiento()
            candidatas_ordenadas = ordenador.quick_sort(list(self.concurso.candidata.values()))
            candidatas_ordenadas.reverse()

            for idx, c in enumerate(candidatas_ordenadas, start=1):
                info = f"{idx}. {c.nombre} - Puntaje: {c.promedio}"
                tk.Label(ventana_ranking, text=info).pack(pady=2)

if __name__ == "__main__":
    ConcursoApp()









