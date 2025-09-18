from fractions import Fraction
import re

class CalculadoraModelo:
    def evaluar(self, expresion):
        try:
            # Reemplazar todas las fracciones "a/b" por float
            def fraccion_a_float(match):
                return str(float(Fraction(match.group())))

            expr_modificada = re.sub(r'\d+/\d+', fraccion_a_float, expresion)

            # Evaluar expresión en decimal
            resultado = eval(expr_modificada)

            # Limitar a 10 cifras significativas
            return f"{resultado:.10g}"

        except ZeroDivisionError:
            return "Error: división por 0"
        except Exception:
            return "Error: expresión inválida"

    def comparar(self, expresion):
        try:
            elementos = [float(Fraction(f.strip())) for f in expresion.split(",")]
            if len(elementos) < 2 or len(elementos) > 3:
                return "Debe ingresar 2 o 3 fracciones/decimales"
            return " < ".join(f"{x:.10g}" for x in sorted(elementos))
        except Exception:
            return "Error en comparación"

    def ordenar(self, expresion):
        try:
            elementos = [float(Fraction(f.strip())) for f in expresion.split(",")]
            if len(elementos) < 2 or len(elementos) > 3:
                return "Debe ingresar 2 o 3 fracciones/decimales"
            return ", ".join(f"{x:.10g}" for x in sorted(elementos))
        except Exception:
            return "Error en ordenamiento"

