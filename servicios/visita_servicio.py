# Lógica del sistema (CRUD)

from modelos.visitante import Visitante


class VisitaServicio:

    def __init__(self):
        # lista privada de visitantes
        self._visitantes = []

    # CREATE
    def registrar_visitante(self, cedula, nombre, motivo):

        # validar duplicados
        for v in self._visitantes:
            if v.cedula == cedula:
                return False

        visitante = Visitante(cedula, nombre, motivo)
        self._visitantes.append(visitante)
        return True

    # READ
    def obtener_visitantes(self):
        return self._visitantes

    # DELETE
    def eliminar_visitante(self, cedula):

        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                return True

        return False
