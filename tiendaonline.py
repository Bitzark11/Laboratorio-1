# Entrada de datos
monto_compra = float(input("Ingrese el monto total de la compra: "))

# Validación para la respuesta de si el cliente es VIP
while True:
    respuesta_vip = input("¿El cliente es miembro VIP? (si/no): ")
    if respuesta_vip == "si":
        es_vip = True
        break
    elif respuesta_vip == "no":
        es_vip = False
        break
    else:
        print("Por favor, ingrese una respuesta válida (si/no).")

# Validación para la respuesta de si tiene código de descuento
while True:
    respuesta_codigo = input("¿El cliente tiene un código de descuento especial? (si/no): ")
    if respuesta_codigo == "si":
        tiene_codigo_descuento = True
        break
    elif respuesta_codigo == "no":
        tiene_codigo_descuento = False
        break
    else:
        print("Por favor, ingrese una respuesta válida (si/no).")

# Cálculo de descuentos
if monto_compra > 100:
    total_pagar = monto_compra * 0.80  # Descuento del 20%
    if es_vip:
        total_pagar *= 0.90  # Descuento adicional del 10%
    if tiene_codigo_descuento:
        total_pagar *= 0.95  # Descuento adicional del 5%
else:
    # Si el monto no supera 100, solo se aplican descuentos para VIP o con código especial
    total_pagar = monto_compra
    if es_vip:
        total_pagar *= 0.90  # Descuento adicional del 10%
    if tiene_codigo_descuento:
        total_pagar *= 0.95  # Descuento adicional del 5%

# Salida del total a pagar
print(f"El total a pagar después de aplicar los descuentos es: ${total_pagar:.2f}")
