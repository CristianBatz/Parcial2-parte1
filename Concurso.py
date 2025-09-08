class Calificacion:
    def __init__(self,jurado,candidata, cultura,proyeccion,entrevista,promedio):
        self.jurado = jurado
        self.candidata = candidata
        self.cultura = cultura
        self.proyeccion = proyeccion
        self.entrevista = entrevista
        self.promedio = float(promedio)

    def promedio(self):
        promedio = (self.cultura + self.proyeccion + self.entrevista) / 3
        return promedio


class Concurso:
    def __init__(self):
        self.jurado = {}
        self.candidata = {}
