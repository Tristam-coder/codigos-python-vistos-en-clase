final_grade = float(input("Nota final: "))

attendance = float(input("Asistencia: "))

modality_code = input("Modalidad (P/V/H): ")

result = ""

if final_grade >= 11 and attendance >= 70:
    result = "Aprobado"
elif final_grade >= 11 and attendance < 70:
    result = "Inhabilitado por asistencia"
else:
    result = "Desaprobado"

modality_name = ""

match modality_code.upper():
    case "P":
        modality_name = "Presencial"
    case "V":
        modality_name = "Virtual"
    case "H":
        modality_name = "Híbrida"
    case _:
        modality_name = "Desconocida"

print("Resultado:", result)

print("Modalidad:", modality_name)

