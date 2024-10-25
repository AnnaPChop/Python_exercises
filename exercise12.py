'''El Banco ABC ha presentado una nueva cuenta Elite diseñada para clientes de alto poder adquisitivo que ganan más de $200 000 al año. 
Escribe código para iterar sobre los clientes, comprueba que sus ingresos anuales superen los $200 000 y agrega la sublista sobre un cliente elegible a la variable 
elite_clients, que es una lista de clientes ricos. Muestra la variable elite_clients al final.'''
#Código
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

elite_clients = [] 

for client in clients:
  if client[3]>200000:
    elite_clients.append(client)

print(elite_clients)
