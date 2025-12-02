import datetime
import random
import string

options = [1, 2, 3, 4, 5]
res = 1
while True:
    if res == 1:
        CC = str(input("Digite tu # de cedula: "))
        name = str(input("Digite su nombre: "))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            """
        1. Seleccione la opción 1 si vas para servicio de caja
        2. Seleccione la opción 2 si vas para el servicio al cliente
        3. Seleccione la opción 3 si vas para el pago de impuestos
        4. Seleccione la opción 4 si vas para el crédito hipotecario
        5. Seleccione la opción 5 si vas a realizar operaciones con la tarjeta de crédito
        """
        )
        print("Digite la opción: ")
        option = int(input())

        n = str(random.randrange(1, 999999)) + \
            random.choice(string.ascii_letters)
        match option:
            case 1:
                print("Vas para él servicio de caja")
            case 2:
                print("Vas para el servicio al cliente")
            case 3:
                print("Vas para el pago de impuestos")
            case 4:
                print("Vas para el crédito hipotecario")
            case 5:
                print("Vas a realizar operaciones con la tarjeta de crédito")
            case _:
                print("Digite una opción valida")
                break

        if option in options:
            print(f"""
            {CC}
            {name}
            {date}
            {n}
            """)
        else:
            break
        res = int(
            input("Seleccione 1 para continuar la transaccion 2 para salir: "))
    elif res == 2:
        break
    else:
        print("Digite una opcion valida.")
