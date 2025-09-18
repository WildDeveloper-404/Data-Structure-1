import tkinter as tk

class CalculadoraVista:
    def __init__(self, root):
        self.root = root
        self.controlador = None

        self.entrada = tk.Entry(root, width=20, font=("Arial", 18),
                                borderwidth=5, relief="ridge", justify="right")
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("⌫", 5, 0), ("C", 5, 1), (",", 5, 2),
        ]

        for boton in botones:
            if len(boton) == 3:
                texto, fila, col = boton
                colspan = 1
            else:
                texto, fila, col, colspan = boton

            tk.Button(root, text=texto, width=5, height=2, font=("Arial", 14),
                      command=lambda t=texto: self.controlador.boton_presionado(t)).grid(
                          row=fila, column=col, columnspan=colspan,
                          padx=5, pady=5, sticky="nsew"
                      )

        # Botones especiales
        tk.Button(root, text="Comparar (f1,f2,f3)", width=20, height=2, font=("Arial", 12),
                  command=lambda: self.controlador.comparar_fracciones()).grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(root, text="Ordenar (f1,f2,f3)", width=20, height=2, font=("Arial", 12),
                  command=lambda: self.controlador.ordenar_fracciones()).grid(row=6, column=2, columnspan=2, padx=5, pady=5)

    def set_controlador(self, controlador):
        self.controlador = controlador

    def mostrar_resultado(self, resultado):
        self.entrada.delete(0, "end")
        self.entrada.insert(0, resultado)
