import numpy as np
from matplotlib  import pyplot as plt
import sympy as sp
#Polinomio de grado 3 f(x)=ax**3+bx**2+cx+d
#Polinomio de grado 4 f(x)=ax**4+bx**3++cx**2+dx+e
global a,b,c,d,g,e,y,x,resultado,fg,ygraf,nombre
class funcion():#creacion de la clase funcion
    def __init__(self,tipo):
        self.tipo=tipo#creacion de atributo 
    def operacion(self):#creacion de
        g=int(input("ingrese el grado de polinomio: "))#aqui se le pide al ususario ingresar el grado de su ecuacion
        if (g==3):
            x=sp.Symbol('x')
            #se le pide que ingrese los valores de su ecuacion
            a=float(input("ingrese el valor de a: "))
            b=float(input("ingrese el valor de b: "))
            c=float(input("ingrese el valor de c: "))
            d=float(input("ingrese el valor de d: "))
            y=a*x**3+b*x**2+c*x+d#se colocan los valores en el polinomio
            resultado=sp.diff(y,x)#se hace la operacion derivacion de polinomio en funcion de x
            print("El resultado es: ",resultado)#se muestra el resultado de la derivacion de polinomio
            fg=sp.lambdify(x,resultado)#esta linea se uso para graficar por mapeo en el caso de usar la derivasion simbolica
            ygraf=np.zeros(20)
            n=len(ygraf)
            x=np.arange(-n/2,n/2) #aqui en el arange muestra valores negativo para observar la grafica de forma correcta
            for i in range(n):
                ygraf[i]=fg(x[i])
            nombre=("f(x)=",resultado)
            plt.plot(x,ygraf,label=nombre,color="red")#se le da color a la grafica y se muestra el polinomio
            plt.xlabel("eje x")
            plt.ylabel("eje y")
            plt.title("Grafica de Polinomio")#titulo de la grafica
            plt.legend()
            plt.show()
        elif(g==4):
            x=sp.Symbol('x')
            a=float(input("ingrese el valor de a: "))
            b=float(input("ingrese el valor de b: "))
            c=float(input("ingrese el valor de c: "))
            d=float(input("ingrese el valor de d: "))
            e=float(input("ingrese el valor de e: "))
            y=a*x**4+b*x**3+c*x**2+d*x+e
            resultado=sp.diff(y,x)
            print("El resultado es: ",resultado)
            fg=sp.lambdify(x,resultado)
            ygraf=np.zeros(20)
            n=len(ygraf)
            x=np.arange(-n/2,n/2)
            for i in range(n):
                ygraf[i]=fg(x[i])
            nombre=("f(x)=",resultado)
            plt.plot(x,ygraf,label=nombre,color="blue")
            plt.xlabel("eje x")
            plt.ylabel("eje y")
            plt.title("Grafica de Polinomio")
            plt.legend()
            plt.show()
        else:
            print("Error fuera de rango de operacion")
A1=funcion(1)   
A1.operacion()