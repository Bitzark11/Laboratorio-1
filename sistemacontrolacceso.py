#Entrada de datos
#Acceso
nivel_acceso = int(input("Ingrese su nivel de acceso (0-5): "))
tarjeta_activa = input("¿tarjeta activa? True/False: ").lower() == "True"
cambio_contraseña = input("¿Cambiaste la contraseña den los ultimos 30 dias? True/False: ").lower() == "True"

#If/Elif/Else

if nivel_acceso == 0:
    print ("Acceso denegado, no cumple el nivel minimo requerido")
elif nivel_acceso >0 and nivel_acceso >=5:
    if tarjeta_activa:
        if cambio_contraseña:
            print("Acceso concedido")
        else:
            print("Acceso denegado, no ha cambiado su contraseña en los ultimos 30 dias")
    else:
        print("Acceso denegado, su tarjeta actualmente esta inactiva")
else:
    print("Acceso denegado, nivel se acceso insuficiente")


