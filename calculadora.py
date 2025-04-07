def main():
    
    seguir=True
    while (seguir):
        print("Calculadora de operaciones muy básicas sencillas P2")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
<<<<<<< HEAD
        print("4.Dividir")
        print("4.5 Potencia")
=======
        print("4.Divid")
>>>>>>> 0cda8fa90b44dee5ce6fd1ae41a9427ca04a2e61
        print("5.Salir")
        
        opcion = input("Elija una opción ")
        print ("Opción elegida: ", opcion)
        if opcion == "1":
             num1= float(input ("Introduzca num 1: "))
             num2= float(input ("Introduzca num 2: "))
             resultado=num1 + num2
             print ("Resultado", resultado)
        seguir=opcion!="5"
if __name__=="__main__":
        main()