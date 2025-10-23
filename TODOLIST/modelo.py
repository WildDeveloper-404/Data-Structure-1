class NodoTarea:
    """Nodo que representa una tarea en la lista enlazada."""
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = "Pendiente"
        self.siguiente = None


class ListaTareas:
    """Lista enlazada para manejar las tareas."""
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, descripcion, al_final=True):
        """Agrega una tarea al inicio o al final."""
        nueva_tarea = NodoTarea(descripcion)
        if not self.cabeza:
            self.cabeza = nueva_tarea
            return

        if al_final:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
        else:
            nueva_tarea.siguiente = self.cabeza
            self.cabeza = nueva_tarea

    def marcar_completada(self, descripcion):
        """Marca una tarea como completada."""
        actual = self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                actual.estado = "Completada"
                return True
            actual = actual.siguiente
        return False

    def eliminar_tarea(self, descripcion):
        """Elimina una tarea por su descripción."""
        actual = self.cabeza
        previo = None
        while actual:
            if actual.descripcion == descripcion:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def obtener_tareas(self):
        """Devuelve todas las tareas como lista de tuplas (descripcion, estado)."""
        tareas = []
        actual = self.cabeza
        while actual:
            tareas.append((actual.descripcion, actual.estado))
            actual = actual.siguiente
        return tareas
