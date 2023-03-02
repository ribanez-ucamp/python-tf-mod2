import sys 

def main():

    # Programa para identificar EL cuadrante en el que se encuentran 
    # Las coordenadas, proporcionadas.

    control = 0

    while control == 0 :
        x = int (input ('Ingresa el valor de x: '))
        y = int (input ('Ingresa el valor de y: '))
        if x==0 and y==0:
            print ('Origen')
        if x==0:
            print ('Eje Y, ', y)
        if y==0:
            print ('Eje X, ', x)
        if x>0 and y>0:
            print ('Cuadrante I')
        if x<0 and y>0:
            print ('Cuadrante II')
        if x<0 and y<0:
            print ('Cuadrante III')
        if x>0 and y<0:
            print ('Cuadrante VI')
        print ()

# Opcional

        continuar = " "

        while continuar == " " :
            continuar = input("¿Deseas ubicar otras coordenadas (S/N)?")
            continuar_up = continuar.upper()

            if continuar_up == "S" :
                control = 0
                continuar = "S"
            elif continuar_up == "N" :
                control = 1
                continuar = "N"
                break            
            else :
                print("Debe responder S para si y N para no")
                continuar = " "

# Fin opcional

    print("Fin del programa. ")


if __name__ == "__main__":
    main()