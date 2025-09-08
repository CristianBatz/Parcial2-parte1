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
    criterios = ["cultura", "proyecciones", "escenica", "entrevista"]

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

class Ordenamiento:
    def quick_sort(self,candidata):
        if len(candidata) <= 1:
            return candidata

        pivote = candidata[0]
        mayores = [b for b in candidata[1:] if b.promedio > pivote.promedio]
        iguales = [b for b in candidata[1:] if b.promedio == pivote.promedio]
        menores = [b for b in candidata[1:] if b.promedio < pivote.promedio]

        return self.quick_sort(menores) + [pivote] + iguales + self.quick_sort(mayores)









