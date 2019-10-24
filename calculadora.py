
while True:
    operacion = "Reinicio cada ciclo"
    while operacion != "Sumar" and operacion != "Restar" and operacion != "Multiplicar" and operacion != "Dividir" and operacion != "Potenciar" and operacion != "Salir":
        operacion = input("Qué operación quieres realizar? (Sumar / Restar / Multiplicar / Dividir / Potenciar / Salir) : ")
        if operacion != "Sumar" and operacion != "Restar" and operacion != "Multiplicar" and operacion != "Dividir" and operacion != "Potenciar" and operacion != "Salir":
            print ("Operación desconocida, vuelve a intentarlo.")

    if operacion == "Salir":
        break
    num1 = float(input("Introduce el primer número con el que vamos a operar: "))
    num2 = float(input("Introduce el segundo número con el que vamos a operar: "))

    if operacion == "Sumar":
        print("El resultado de Sumar {} y {} es: {}".format(str(num1), str(num2), str(num1+num2)))
    elif operacion == "Restar":
        print("El resultado de Restar {} y {} es: {}".format(str(num1), str(num2), str(num1-num2)))
    elif operacion == "Multiplicar":
        print("El resultado de Multiplicar {} y {} es: {}".format(str(num1), str(num2), str(num1*num2)))
    elif operacion == "Dividir":
        if num2 == 0:
            print("No se puede dividir entre cero!")
            continue
        else:
            print("El resultado de Dividir {} entre {} es: {}".format(str(num1), str(num2), str(num1/num2)))
    elif operacion == "Potenciar":
        print("El resultado de Elevar {} a {} es: {}".format(str(num1), str(num2), str(num1**num2)))

print("Instrucción 'Salir' recibida; \nPrograma finalizado.")