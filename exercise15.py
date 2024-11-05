'''Estás analizando una lista de strings almacenada en una variable text_entries. Cada string puede ser una combinación de alfabetos o dígitos. Para cada string en la lista, necesitas:

Mostrar si el string solo contiene caracteres alfabéticos usando isalpha().
Mostrar si el string solo contiene letras en minúscula usando islower().
Mostrar si el string solo contiene dígitos usando isdigit().
Mostrar si el string contiene todo alfabético o todo dígitos usando or.
Mostrar si el string no contiene nada alfabético ni tiene todo dígitos usando not.
Completa las expresiones lógicas y las funciones de predicado, según se explicó previamente.'''
#Código
text_entries = ['Hola', 'hola', '1234', "hola1234"]  # Lista de entradas de texto

for text in text_entries:
    
    print(f"Text '{text}':") 
    
    # Comprueba si el texto solo contiene caracteres alfabéticos
    print("Solo contiene alfabeto", text.isalpha())
    
    # Comprueba si el texto contiene solo letras en minúscula
    print("Solo contiene minúsculas", text.islower())

   # Comprueba si el texto no es todo alfabeto o no son todos dígitos
    print("No es alfabético ni son dígitos", not (text.isalpha() or text.isdigit()))
    # Comprueba si el texto contiene solo dígitos
    print("Solo contiene dígitos", text.isdigit())
    
    # Comprueba si el texto es todo alfabeto o son todos dígitos
    print("Es alfabético o tiene dígitos", text.isalpha() or text.isdigit())
    
