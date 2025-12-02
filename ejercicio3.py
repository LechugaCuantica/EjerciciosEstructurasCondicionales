yearsOld = int(input("Digite su edad: "))

if yearsOld > 0 and yearsOld < 5:
    print("Estás en la categoría infante")
elif yearsOld > 6 and yearsOld < 10:
    print("Estás en la categoría niño")
elif yearsOld > 11 and yearsOld < 15:
    print("Estás en la categoría pre-Adolescente")
elif yearsOld > 16 and yearsOld < 18:
    print("Estás en la categoría adolescente")
elif yearsOld > 19 and yearsOld < 25:
    print("Estás en la categoría Pre adulto")
elif yearsOld > 26 and yearsOld < 40:
    print("Estás en la categoría adulto")
elif yearsOld > 41 and yearsOld < 55:
    print("Estás en la categoría pre-anciano")
elif yearsOld > 56 and yearsOld < 120:
    print("Estás en la categoría anciano")
else:
    print("Edad no valida. digite nuevamente.")
