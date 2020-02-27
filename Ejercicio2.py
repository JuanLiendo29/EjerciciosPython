mill = float(input("Indique las millas por galon: "))
tanq = float(input("Indique la capacidad del tanque: "))
medi = float(input("Indique cuanto marca el medidor: "))
road = tanq*medi*mill
if road > 200:
    print("seguro, proceder")
else:
    print("Solo vas a poder recorrer: ", road, " millas. Vaya a la gasolinera más cerca a para tener mas gasolina")
               
