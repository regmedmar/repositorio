def main():
    
    seguir=True
    while (seguir):
        print("Calculadora de operaciones muy básicas sencillas P2, otro cambio ")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
        print("4.Dividir")
        print("4.5 Potencia")
        print("5.Salir")
        opcion = input("Elija una opción ")
        print ("Opción elegida: ", opcion)
        if opcion == "1":
             num1= float(input ("Primer num 1: "))
             num2= float(input ("Segundo num 2: "))
             resultado=num1 + num2
             print ("Resultado", resultado)
        if opcion == "2":
             num1= float(input ("Primer num 1: "))
             num2= float(input ("Segundo num 2: "))
             resultado=num1 - num2
             print ("Resultado", resultado)
        if opcion == "3":
             num1= float(input ("Primer num 1: "))
             num2= float(input ("Segundo num 2: "))
             resultado=num1 * num2
             print ("Resultado", resultado)
<<<<<<< HEAD
        if opcion == "4":
             num1= float(input ("Primer num 1: "))
             num2= float(inpt ("Segundo num 2: "))
             resultado=num1 / num2
=======
        if opcion == "4.5":
             num1= int(input ("Primer num 1: "))
             num2= int(input ("Segundo num 2: "))
             resultado=num1 ** num2
>>>>>>> f4f6a70bf73c11215db3df5d4f9e57056621eaaa
             print ("Resultado", resultado)
        seguir=opcion!="5"
if __name__=="__main__":
     main()