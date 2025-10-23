import tkinter as tk
from tkinter import messagebox
class VistaTareas:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Entrada de texto
        self.entry_tarea = tk.Entry(root, width=50)
        self.entry_tarea.pack(pady=10)

        # Botones
        botones_frame = tk.Frame(root)
        botones_frame.pack(pady=5)

        tk.Button(botones_frame, text="Agregar al final", command=self.controller.agregar_final).grid(row=0, column=0, padx=5)
        tk.Button(botones_frame, text="Agregar al inicio", command=self.controller.agregar_inicio).grid(row=0, column=1, padx=5)
        tk.Button(botones_frame, text="Marcar completada", command=self.controller.marcar_completada).grid(row=0, column=2, padx=5)
        tk.Button(botones_frame, text="Eliminar tarea", command=self.controller.eliminar_tarea).grid(row=0, column=3, padx=5)

        # Lista de tareas
        self.listbox_tareas = tk.Listbox(root, width=70, height=18, font=("Arial", 11))
        self.listbox_tareas.pack(pady=10)

    def obtener_datos_tarea(self):
        return self.entry_tarea.get().strip()

    def mostrar_lista_tareas(self, tareas):
        """Muestra la lista de tareas con colores según el estado."""
        self.listbox_tareas.delete(0, tk.END)
        for tarea in tareas:
            descripcion, estado = tarea
            texto = f"{descripcion}  →  {estado}"
            self.listbox_tareas.insert(tk.END, texto)
            index = self.listbox_tareas.size() - 1
            color = "green" if estado == "Completada" else "red"
            self.listbox_tareas.itemconfig(index, fg=color)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def limpiar_entrada(self):
        self.entry_tarea.delete(0, tk.END)