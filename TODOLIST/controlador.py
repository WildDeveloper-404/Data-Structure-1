class ControladorTareas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def actualizar_vista(self):
        tareas = self.modelo.obtener_tareas()
        self.vista.mostrar_lista_tareas(tareas)

    def agregar_final(self):
        descripcion = self.vista.obtener_datos_tarea()
        if not descripcion:
            self.vista.mostrar_error("Debe ingresar una descripción para la tarea.")
            return
        self.modelo.agregar_tarea(descripcion, al_final=True)
        self.vista.limpiar_entrada()
        self.actualizar_vista()

    def agregar_inicio(self):
        descripcion = self.vista.obtener_datos_tarea()
        if not descripcion:
            self.vista.mostrar_error("Debe ingresar una descripción para la tarea.")
            return
        self.modelo.agregar_tarea(descripcion, al_final=False)
        self.vista.limpiar_entrada()
        self.actualizar_vista()

    def marcar_completada(self):
        seleccion = self.vista.listbox_tareas.curselection()
        if not seleccion:
            self.vista.mostrar_error("Seleccione una tarea para marcar como completada.")
            return
        texto = self.vista.listbox_tareas.get(seleccion[0])
        descripcion = texto.split("  →")[0].strip()
        self.modelo.marcar_completada(descripcion)
        self.actualizar_vista()

    def eliminar_tarea(self):
        seleccion = self.vista.listbox_tareas.curselection()
        if not seleccion:
            self.vista.mostrar_error("Seleccione una tarea para eliminar.")
            return
        texto = self.vista.listbox_tareas.get(seleccion[0])
        descripcion = texto.split("  →")[0].strip()
        self.modelo.eliminar_tarea(descripcion)
        self.actualizar_vista()

