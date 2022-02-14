planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]

input_planeta = input("Introduzca el nombre de un planeta del sistema solar, recuerde empezar con letra mayuscula: ")

busqueda_planeta = planetas.index(input_planeta)

print("Los planetas mas cercanos al sol que", input_planeta, "son")
print(planetas[0:busqueda_planeta])

print("Los planetas mas alejados al sol que", input_planeta, "son")
print(planetas[busqueda_planeta+1:])