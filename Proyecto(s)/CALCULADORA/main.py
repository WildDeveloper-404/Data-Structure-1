import tkinter as tk
from vista import CalculadoraVista
from controlador import CalculadoraControlador
from modelo import CalculadoraModelo

def main():
    root = tk.Tk()
    root.title("Calculadora de Fracciones y Decimales")

    modelo = CalculadoraModelo()
    vista = CalculadoraVista(root)
    controlador = CalculadoraControlador(modelo, vista)

    vista.set_controlador(controlador)

    root.mainloop()

if __name__ == "__main__":
    main()
                