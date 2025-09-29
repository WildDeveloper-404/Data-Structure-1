class PolinomioEstatico:
    def __init__(self, terminos):
        #Lista
        self._terminos = terminos  

    #getter
    def obtener_terminos(self):
        return self._terminos

    #setter
    def asignar_terminos(self, nuevos_terminos):
        self._terminos = nuevos_terminos

    # Calcula para el valor dado de x
    def evaluar(self, x):
        return sum(coef * (x ** exp) for coef, exp in self._terminos)

    # Retorna en cadena el Polinomio
    def mostrar(self):
        return " + ".join(f"{coef}x^{exp}" for coef, exp in self._terminos)


#Uso de forma estática
poli_estatico = PolinomioEstatico([(1,0), (2,3), (7,1), (9,2)])
print("Términos:", poli_estatico.obtener_terminos())
print("Polinomio Estático:", poli_estatico.mostrar())
print("Evaluado en x=2:", poli_estatico.evaluar(2))

#Uso de forma dinámica
poli_estatico.asignar_terminos([(4,6), (2,3), (7,2)])
print("------ Términos modificados. ------")
print("Nuevo Polinomio Estático:", poli_estatico.mostrar())
print("Nueva evaluación en x=4:", poli_estatico.evaluar(4))
print("Nuevos términos:", poli_estatico.obtener_terminos())


print("------------------------------------------------")


class PolinomioDinamico:
    def __init__(self):
        
        self._terminos = []
    #getter
    def obtener_terminos(self):
        return self._terminos

    #setter
    def asignar_terminos(self, nuevos_terminos):
        self._terminos = nuevos_terminos

    
    def agregar_termino(self, coef, exp):
        self._terminos.append((coef, exp))

    
    def evaluar(self, x):
        return sum(coef * (x ** exp) for coef, exp in self._terminos)

    
    def mostrar(self):
        return " + ".join(f"{coef}x^{exp}" for coef, exp in self._terminos)
    

# Ejemplo de uso dinamico
poli_dinamico = PolinomioDinamico()
poli_dinamico.agregar_termino(2,0)
poli_dinamico.agregar_termino(2,5) 
poli_dinamico.agregar_termino(7,1)
poli_dinamico.agregar_termino(9,3)

print("Términos:", poli_dinamico.obtener_terminos())
print("Polinomio Dinámico:", poli_dinamico.mostrar())
print("Evaluado en x=1:", poli_dinamico.evaluar(1)) 

# Se cambian los términos dinámicamente
poli_dinamico.asignar_terminos([(4,6), (2,3), (7,2)])
print("------ Términos modificados. ------")
print("Nuevo Polinomio Dinámico:", poli_dinamico.mostrar())
print("Nueva evaluación en x=1:", poli_dinamico.evaluar(1))
print("Nuevos términos:", poli_dinamico.obtener_terminos())