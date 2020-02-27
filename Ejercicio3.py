A = float(input("Precio por libra paquete A: "))
A1 = float(input("Porcentaje magro paquete A: "))
B = float(input("Precio por libra paquete B: "))
B1 = float(input("Porcentaje magro paquete B: "))
C1 =(A/A1)
C2 =(B/B1)
print("Costo por libra de carne magra en Paquete A: " ,C1)
print("Costo por libra de carne magra en Paquete B: " ,C2)

if C1 > C2:
    print("El paquete B es mejor")
else:
    print("El paquete A es mejor")
               
