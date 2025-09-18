from tkinter import messagebox

class CalculadoraControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def boton_presionado(self, texto):
        actual = self.vista.entrada.get()

        # Limitar a 10 cifras significativas (sin contar operadores y separadores)
        if texto not in ("=", "⌫", "C", ",", "+", "-", "*", "/", "."):
            cifras = len(actual.replace(",", "").replace(".", "").replace("-", ""))
            if cifras >= 10:
                return  # no añadir más

        if texto == "=":
            self.calcular()
        elif texto == "⌫":
            self.vista.entrada.delete(0, "end")
            self.vista.entrada.insert(0, actual[:-1])
        elif texto == "C":
            self.vista.entrada.delete(0, "end")
        else:
            self.vista.entrada.insert("end", texto)

    def calcular(self):
        expresion = self.vista.entrada.get()
        # Verificar si se usa coma en vez de punto para decimales
        if "," in expresion:
            # Coma permitida solo si es separación para comparación/orden
            # Si contiene operadores + - * /, asumimos que es decimal mal escrito
            if any(op in expresion for op in "+-*/"):
                messagebox.showwarning("Error decimal", "Para decimales use el punto '.' y no la coma ','")
                return
        resultado = self.modelo.evaluar(expresion)
        self.vista.mostrar_resultado(resultado)

    def comparar_fracciones(self):
        expresion = self.vista.entrada.get()
        resultado = self.modelo.comparar(expresion)
        self.vista.mostrar_resultado(resultado)

    def ordenar_fracciones(self):
        expresion = self.vista.entrada.get()
        resultado = self.modelo.ordenar(expresion)
        self.vista.mostrar_resultado(resultado)
