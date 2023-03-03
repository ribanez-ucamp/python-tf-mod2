import sys 

# Se incluye la biblioteca para graficar matplotlib

import matplotlib.pyplot as plt

def main():

    # Programa para identificar EL cuadrante en el que se encuentran 
    # Las coordenadas, proporcionadas.

    
    # Se realiza la ejecución el programa hasta que el usuario decida terminar

    # Se define una función para validar que las entradas sean numéricas

    print("Bienvenidos al programa para graficar un punto!")
    print("\n")

    def isNumeric(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    control = False

    while control == False :

        # Se valida que se proporcione un número entero para x

        while True:
            ent_x = input('Ingresa el valor de x: ') 

            if ent_x.isalpha() :
                print("Dato incorrecto. Debes introducir un número para x")
            else :
                s = ent_x
                #print(isNumeric(s))    # True
                if isNumeric(s) :
                    x = int(ent_x)
                    break
                else :
                    print("Dato incorrecto. Debes introducir un número para x")

        # Se valida que se proporcione un número entero para y

        while True:
            ent_y = input('Ingresa el valor de y: ') 

            if ent_y.isalpha() :
                print("Dato incorrecto. Debes introducir un número para y")
            else :
                s = ent_y
                #print(isNumeric(s))    # True
                if isNumeric(s) :
                    y = int(ent_y)
                    break
                else :
                    print("Dato incorrecto. Debes introducir un número para x")

        # Se imprime el cuadrante al que corresponden las coordenadas    

        if x==0 and y==0:
            print ('Origen')
        if x==0:
            print ('Abcsisa 0 - Eje Y, ', y)
        if y==0:
            print ('Ordenada 0 - Eje X, ', x)
        if x>0 and y>0:
            print ('Cuadrante I')
        if x<0 and y>0:
            print ('Cuadrante II')
        if x<0 and y<0:
            print ('Cuadrante III')
        if x>0 and y<0:
            print ('Cuadrante IV')
        print ()

        input("Oprima cualquier tecla para ver la gráfica. ")

        plt.plot(x,y,marker ="o")
        plt.show()

    # Opcional

        continuar = " "

        while continuar == " " :
            continuar = input("¿Deseas evaluar otras coordenadas (S/N)?")
            continuar_up = continuar.upper()

            if continuar_up == "S" :
                continuar = "S"
            elif continuar_up == "N" :
                control = True
                continuar = "N"
                break            
            else :
                print("Debe responder S para si y N para no")
                continuar = " "

    # Fin opcional

    print("Fin del programa. ")


if __name__ == "__main__":
    main()