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
