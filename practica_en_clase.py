# Solicitar al usuario que ingrese un número
numero = int(input("Por favor, ingresa un número: "))

# Verificar si el número es cero
if numero == 0:
    print("El número ingresado es cero.")
# Verificar si el número es par
elif numero % 2 == 0:
    print(f"El número {numero} es par.")
# Si no es cero ni par, debe ser impar
else:
    print(f"El número {numero} es impar.")

print("")
print("Mejia Suarez Emmanuel Alexander:mi practica verifica que el numero que ingresa el usuario si es par, impar o 0 ")
print("")
