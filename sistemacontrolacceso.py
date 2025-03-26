# Nivel de acceso requerido por defecto
nivel_acceso_requerido = 5

# Entrada de datos
nivel_acceso_usuario = int(input("Ingrese su nivel de acceso (0-5): "))

# Validación para el estado de la tarjeta
while True:
    respuesta_tarjeta = input("¿La tarjeta está activa? (si/no): ")
    if respuesta_tarjeta == "si":
        tarjeta_activa = True
        break
    elif respuesta_tarjeta == "no":
        tarjeta_activa = False
        break
    else:
        print("Por favor, ingrese una respuesta válida (si/no).")

# Validación para el cambio de contraseña
while True:
    respuesta_contraseña = input("¿La contraseña fue cambiada en los últimos 30 días? (si/no): ")
    if respuesta_contraseña == "si":
        contraseña_cambiada_recientemente = True
        break
    elif respuesta_contraseña == "no":
        contraseña_cambiada_recientemente = False
        break
    else:
        print("Por favor, ingrese una respuesta válida (si/no).")

# Verificar condiciones de acceso
if nivel_acceso_usuario >= nivel_acceso_requerido:
    if tarjeta_activa:
        if contraseña_cambiada_recientemente:
            print("Acceso permitido.")
        else:
            print("Acceso denegado: La contraseña no se ha cambiado recientemente.")
    else:
        print("Acceso denegado: La tarjeta no está activa.")
else:
    print("Acceso denegado: Nivel de acceso insuficiente.")
