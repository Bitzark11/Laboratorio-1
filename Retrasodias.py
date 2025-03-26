#Entrada de datos
numero_Proyectos_Retrasados = int(input("Ingrese el numero de proyectos que ha entregado con mas de un dia de retraso: "))
#Formula para calcular el retraso en la entrega del proyecto
dias_asignados = int(input("Ingrese el numero total de dias que se le asignaron para la entrega del proyecto: "))
dias_retraso = int(input("Ingrese el numero total de dias de retraso en la entrega del proyecto: "))
porcentaje_retraso = float
print(f"El porcentaje total de retraso con respecto a la entrega inicial es: {dias_retraso/dias_asignados * 100}")