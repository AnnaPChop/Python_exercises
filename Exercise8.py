'''Estás construyendo un programa para analizar los datos de ventas de una tienda minorista. El director de la tienda quiere que calcules los ingresos totales generados en una semana y averigües los importes de venta más altos y más bajos de un día.

La salida esperada es esta:

Ingresos totales de la semana: $ 1721.99
Importe de ventas más alto en un día: 400.0 $.
Importe de ventas más bajo en un día: 100.25 $.'''

#Lista de importes de ventas en USD
daily_sales = [ 250.75, 300.5, 100.25, 400.0, 320.5, 200.0, 150.0]

#Calcula los ingresos totales utilizando sum() y el operador de asignación aumentada
total_revenue = 0
total_revenue += sum(daily_sales) 

#Encuentra los importes de ventas más altas y más bajos
highest_sales = max(daily_sales)
lowest_sales = min(daily_sales) 

#Mostrar los resultados
print("Ingresos totales de la empresa: $", total_revenue )
print("Importe de ventas más altas en un día: $", highest_sales)
print("Importe de ventas más bajas en un día: $", lowest_sales) 
