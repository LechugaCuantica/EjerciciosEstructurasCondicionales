
questions = int(input("Digite la cantidad total de preguntas: "))
correctAnswers = int(input("Digite la cantidad de respuestas correctas: "))

porcentage = (correctAnswers / questions) * 100

if porcentage >= 90.0:
    print("Tu nivel es: Nivel máximo")
elif porcentage >= 75.0 and porcentage < 90.0:
    print("Tu nivel es: Nivel medio")
elif porcentage >= 50.0 and porcentage < 75.0:
    print("Tu nivel es: Nivel regular")
elif porcentage < 50.0:
    print("Tu nivel es: Fuera de nivel")

print(f"El total de respuestas correctas es de: {correctAnswers}")
print(f"El porcentaje obtenido es {porcentage:.1f}")
