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
    def __init__(self):
        self.candidatas = {}
        self.cargar_Candidatas()

    def cargar_Candidatas(self):
        try:
            with open("candidatas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo, nombre, edad, institucion, municipio = linea.split(";")
                        self.candidatas[codigo] = Candidatas(
                            codigo, nombre, int(edad), institucion, municipio
                        )
            print("Candidatas cargadas.")
        except FileNotFoundError:
            print("No existe el archivo candidatas.txt, se creará al guardar.")

    def guardar_candidata(self):
        with open("candidatas.txt", "w", encoding="utf-8") as archivo:
            for candidata in self.candidatas.values():
                archivo.write(f"{candidata.codigo};{candidata.nombre};{candidata.edad};{candidata.institucion};{candidata.municipio}\n")

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

        self.candidatas[codigo] = Candidatas(codigo, nombre, edad, institucion, municipio)
        self.guardar_candidata()
        print(f"Candidata {nombre} registrada con éxito.")

    def mostrar_info(self):
        if not self.candidatas:
            print("No hay candidatas registradas")
        else:
            for candidata in self.candidatas.values():
                print(f"Codigo: {candidata.codigo} | Nombre: {candidata.nombre} | Edad: {candidata.edad} | Institución: {candidata.institucion} | Municipio: {candidata.municipio}")


class Jurado:
    criterios = ["cultura", "proyecciones", "entrevista"]

    def __init__(self, codigo_Jurado, nombre):
        self.nombre = nombre
        self.codigo_Jurado = codigo_Jurado
        self.jurado = {}
        self.puntuaje = {}
        self.cargar_jurado()

    def cargar_jurado(self):
        try:
            with open("Jurado.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo_Jurado, nombre = linea.split(";")
                        self.jurado[codigo_Jurado] = {"nombre": nombre}
        except FileNotFoundError:
            print("No existe el archivo Jurado.txt, se creará uno nuevo al guardar.")

    def registro_puntuaje(self):
        for criterio in self.criterios:
            puntaje = int(input(f"Ingrese la puntuación para {criterio}: "))
            self.puntuaje[criterio] = puntaje

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

        return self.quick_sort(menores) + [pivote] + iguales + self.quick_sort(mayores)

class ConcursoApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Reinas de Independencia - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

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
        ventana_inscripcion1.geometry("500x300")
        tk.Label(ventana_inscripcion1,text="Nombre de la candidata").pack(pady=5)
        entrada_nombre = tk.Entry(ventana_inscripcion1)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_inscripcion1,text="Edad de la candidata").pack(pady=5)
        entrada_edad = tk.Entry(ventana_inscripcion1)
        entrada_edad.pack(pady=5)

        tk.Label(ventana_inscripcion1,text="Instituto de la candidata").pack(pady=5)
        instituto = tk.Entry(ventana_inscripcion1)
        instituto.pack(pady=5)

        tk.Label(ventana_inscripcion1,text="Municipio de la candidata").pack(pady=5)
        municipio = tk.Entry(ventana_inscripcion1)
        municipio.pack(pady=5)


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

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_inscripcion3 = tk.Toplevel(self.ventana)
        ventana_inscripcion3.title("Registrar evaluacion")
        ventana_inscripcion3.geometry("500x300")
        tk.Label(ventana_inscripcion3,text="Cultura").pack(pady=5)
        entrada_Cultura = tk.Entry(ventana_inscripcion3)
        entrada_Cultura.pack(pady=5)

        tk.Label(ventana_inscripcion3,text="Proyecciones").pack(pady=5)
        entrada_Proyecciones = tk.Entry(ventana_inscripcion3)
        entrada_Proyecciones.pack(pady=5)

        tk.Label(ventana_inscripcion3,text="Entrevista").pack(pady=5)
        entrada_entrevista = tk.Entry(ventana_inscripcion3)
        entrada_entrevista.pack(pady=5)



    def listar_candidatas(self):
        print("Se abrió la ventana: Listado de candidatas")
        tk.Toplevel(self.ventana).title("Listado de candidatas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoApp()









