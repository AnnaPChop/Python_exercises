''' 
Los departamentos de seguridad del banco no quedaron satisfechos con la forma en la que presentamos la lista de clientes la última vez. Esta vez nos pidieron que proporcionáramos los nombres de los clientes imprimiendo cada nombre en una línea separada.

Haz un bucle en la lista de clientes y muestra sus nombres.

La salida esperada es esta:

Jack Wilson
Nina Brown
Alex Smith
Brian Perez
Sarah Lee
David Kim
Samantha Chen
Juan Rodriguez '''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
]

for client in clients: 
  print(client[1])
  
