
opcion = ""
while opcion != "salir":
    print("=======Menú========")
    print("Seleciona una de las siguientes opciones:")
    print("(1) para calcular Promedio")
    print("(2) para calcular Curso")
    print("(3) para Salir")
    
    try:
        opcion = int(input("-Ingresa una opción: "))
    except ValueError:
        print("*Debes escribir un número.")
        continue
    
    if opcion == 1:
        
        try:
           cantNotas = int(input("Ingresa la cantidad de notas a promediar: "))
        except ValueError:
            print("*Debes escribir un número.")
            continue
        if  cantNotas < 2:
            print("*El valor no puede ser menor a 2")
        else:
            i = 1
            acum = 0
            while i <= cantNotas:
                try:
                   notas = float(input(f"ingresa la nota N°{i}: "))
                except ValueError:
                    print("*Debes escribir un número.")
                    continue
                if notas > 0 and notas < 8:
                    acum +=notas
                    i +=1
                else:
                    print("*No se puede colocar una nota menor a 0 y mayor a 7")
                    opcion = "salir"
                    break   
            if opcion == "salir":
                opcion = "salir"
            else:           
                promedio = acum/cantNotas   
                print(f"El promedio es: {promedio}")   
                opcion = "salir"
    elif opcion == 2:
        while True:
            try:
                edad = int(input("-Escribe la edad: "))
            except ValueError:
                print("Debes escribir un número.")
                continue

            if edad < 0:
                print("Debes escribir un número positivo.")
                continue
            else:
                break
       
        print("Ingresa el mes de nacimiento...")
        while True:
            try:
                mesNac = int(input("Escribe un número del 1 al 12 según corresponda: "))
            except ValueError:
                print("Debes escribir un número.")
                continue

            if mesNac < 1 or mesNac >12:
                print("*Debes escribir un número entre 1 - 12.")
                continue
            else:
                break
       
        if (edad == 14 and mesNac < 4) or (edad == 15 and mesNac > 3):
            print("El alumno debe ir en Primerio Medio")
        elif (edad == 15 and mesNac < 4) or (edad == 16 and mesNac > 3):
            print("El alumno debe ir en Segundo Medio")
        elif (edad == 16 and mesNac < 4) or (edad == 17 and mesNac > 3):
            print("El alumno debe ir en Tercero Medio")
        elif (edad == 17 and mesNac < 4) or (edad == 18 and mesNac > 3):
            print("El alumno debe ir en Cuarto Medio")
        else:
            print("No apto para este liceo")
            opcion = "salir"

    elif opcion == 3:
      
        opcion = "salir"

    else:

       print("*Debes ingresar un valor válido")





