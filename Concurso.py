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









