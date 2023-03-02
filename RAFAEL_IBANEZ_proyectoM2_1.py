import sys 

def main():

    # Programa para identificar la longitud de una palabra ingresada. 
    # La palabra correcta debe tener entre cuatro y ocho letras.

    control = 0
    word1 = 0

    while control == 0 :

        #Se debe solicitar una Palabra indicando la longitud requerida

        while True:
            try:
                word1 = input("Escribe una palabra que contenga de 4 a 8 caracteres: ")
            except ValueError:
                continue

            if len(word1) >= 4 : 
                if  len(word1) <= 8 :
                    print("La palabra ", word1, "es correcta")
                    control = 1
                    break
                else :
                    print("La palabra excede la longitud requerida, sobra(n) ", len(word1) - 8, "letra(s) ")
            else :
                print("La palabra no tiene la longitud requerida, falta(n)", 4 - len(word1), "letra(s)" )
# Opcional

        continuar = " "

        while continuar == " " :
            continuar = input("¿Deseas evaluar otra palabra (S/N)?")
            continuar_up = continuar.upper()

            #print("continuar_up ", continuar_up)

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