'''El departamento de marketing del Banco ABC está interesado en conocer la edad promedio de su clientela. 
La edad promedio es simplemente la suma de las edades de todos los clientes dividida entre la cantidad de clientes. 
Utiliza el bucle for para iterar sobre la lista clients y actualiza las variables total_age y num_clients en cada iteración del bucle.

La variable total_age debe almacenar la suma de edades, mientras que la variable num_clients se usa para almacenar el número total de clientes.

Las variables total_age y num_clients ya están declaradas para que hagas tus cálculos con ellas. Tras recorrer la lista y actualizar estas dos variables, 
calcula la edad promedio de todos los clientes, almacénala en la variable average_age y muéstrala.

La salida esperada es esta:

35.25'''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"]
]

total_age = 0
num_clients = 0

for client in clients:
  total_age += client[2]
  num_clients += 1

average_age = total_age / num_clients

print(average_age) 
  
