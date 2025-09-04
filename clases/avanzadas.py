class Avanzadas:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1:"))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2:"))
                break
            except Exception:
                print("Número inválido")
                continue    
    
    def elevarPotencia(self):
        self.resultado= "El numero "+str(self.num1)+" elevado al "+str(self)+" es = "+str(self.num1**self.num2)
        
        
    def raizCuadrada(self):
        if self.num1 >= 0:
            raiz = self.num1 ** 0.5
            print(f"La raíz cuadrada de {self.num1} es = {raiz}")
        else:
            print("No se puede calcular la raíz cuadrada de un negativo")