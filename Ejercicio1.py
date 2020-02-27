tornillo = 5
tuercasp = 3
arande = 1
tornillos = float(input("Cuantos tornillos desea comprar?: "))
tuercas = float(input("Cuantas tuercas desea comprar? : "))
anrand = float(input("Numero de arandela: "))

if tuercas > tornillos :
    preciofinal= arande + (tornillos*tornillo) + (tuercasp*tuercas)
    print("La orden esta bien, es un total de : ", preciofinal, "RESUMIDO  tornillos = ",tornillos, " tuercas " ,tuercas)
   
else:
     print("Compurebe orden")
    
