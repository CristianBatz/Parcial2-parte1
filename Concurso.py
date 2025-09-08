class Candidatas:
    def __init__(self, codigo, nombre, edad, institucion, municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.institucion = institucion
        self.municipio = municipio

    def mostrar_info(self):
        return f" La candidata con el Codigo: {self.codigo} | Nombre: {self.nombre} | Edad: {self.edad} "


class GestionCandidata:
    def __init__(self, codigo):
        self.candidatas = {}
        self.codigo = codigo
        self.cargar_Candidatas

    def cargar_Candidatas(self):
        try:
            with open("candidatas.txt", "r", encodig="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo, nombre, edad, institucion, municipio = linea.split(";")
                        self.candidatas[codigo] = Candidatas(
                            codigo=codigo,
                            nombre=nombre,
                            edad=edad,
                            institucion=institucion,
                            municipio=municipio
                        )
            print("Candidata registrada")
        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará uno nuevo al guardar.")
        except ValueError:
            print("Error al leer el archivo. Verifique el formato de las líneas.")

    def guardar_candidata(self):
        with open("candidatas.text", "w", encodig="utf-8") as archivo:
            for codigo, datos in self.candidatas.itemas():
                archivo.write(f"Codigo: {codigo}, Nombre: {nombre}, Edad: {edad}")

    def agregar_candidata(self):
        print("Ingrese los datos que se le piden para registrar a las candidats")
        codigo = input("Ingrese el codigo de la candidata: ")
        nombre = input("Ingrese el nombre de la candidata: ")
        edad = int(input("Ingrese la edad de la candidata: "))
        if 20 <= edad <= 30:
            print(f"La candidata no puede participar por tener la edad de {edad}")
        institucion = input("Ingrese la institucion educativa de donde proviene: ")
        municipio = input("Ingrese de que municipio proviene la candidata: ")

        self.candidatas[codigo] = Candidatas(
            codigo=codigo,
            nombre=nombre,
            edad=edad,
            institucion=institucion,
            municipio=municipio
        )
        self.guardar_candidata()
        print(f"La candidata {nombre} del establecimiento {institucion} y del municipio de {municipio}")

    def mostrar_info(self):
        if not self.candidatas:
            print("No hay candidatas registradas")
            return
        for p in self.candidatas.values():
            print(f"Codigo: {codigo}| Nombre: {nombre}| Edad:{edad}| Municipio:{municipio}")

class Jurado:
    criterios=["cultura","proyecciones","escencia","entrevista"]
    def __init__(self,codigo_Jurado,nombre):
        self.nombre=nombre
        self.codigo_Jurado=codigo_Jurado
        self.jurado={}
        self.puntuaje={}
        self.cargar_jurado()

    def cargar_jurado(self):
       try:
        with open("Jurado.txt", "r", econdig="utf-8") as archivo:
            for linea in archivo:
                linea=linea.strip()
                if linea:
                    codigo_Jurado,nombre=linea.split(";")
                    jurado[codigo_Jurado]={
                        "nombre" ,nombre
                    }


