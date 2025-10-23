import tkinter as tk
from modelo import ListaTareas
from vista import VistaTareas
from controlador import ControladorTareas

if __name__ == "__main__":
    root = tk.Tk()
    modelo = ListaTareas()
    controlador = ControladorTareas(modelo, None)
    vista = VistaTareas(root, controlador)
    controlador.vista = vista
    root.mainloop()