import random
v = random.randrange(10, 150)

zone = int(input("Digite la zona en la cual estás conduciendo: (1. Escolar, 2. Vía Urbana, 3. Vía Rural, 4. Ruta Nacional )"))

match zone:
    case 1:
        limit = 30
        zoneStr = "Zona Escolar"
    case 2:
        limit = 60
        zoneStr = "Vía Urbana"
    case 3:
        limit = 80
        zoneStr = "Vía Rural"
    case 4:
        limit = 100
        zoneStr = "Ruta Nacional"

if v > limit:
    print(f"Estás infrigiendo el limite de velocidad ")
    print(
        f"Estás yendo a {v:.1f} km/h y La velocidad limite en {zoneStr} es de {limit}")
