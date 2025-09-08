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
