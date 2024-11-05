'''Estás analizando un conjunto de datos de los comentarios de reseña de un producto almacenados en la variable review_comment. Para el valor determinado de review_comment, muestra:

"El comentario contiene solo letras." seguido de True si review_comment solo contiene caracteres alfabéticos.
"El comentario contiene solo números." seguido de True si review_comment solo contiene dígitos.
"El comentario contiene caracteres mixtos o no alfabéticos." seguido de True si review_comment contiene caracteres no alfabéticos y no tiene dígitos. 1. Para hacerlo, necesitas:
Comprobar si el comentario de revisión solo contiene letras.
Comprobar si el comentario de revisión solo contiene dígitos.
Combinar los resultados de estas comprobaciones con una operación OR.
Negar el resultado combinado para determinar si el comentario contiene una mezcla de caracteres u otros tipos de caracteres.
Completa los espacios con las funciones de predicado correctas, según se explicó previamente.'''
# Código
review_comment = "GreatProduct123"  # Puedes cambiar este valor para poner a prueba diferentes escenarios

# Review_comment contiene solo caracteres alfabéticos
print("El comentario solo contiene letras.", review_comment.isalpha())
# Review_comment contiene solo dígitos
print("El comentario solo contiene números.", review_comment.isdigit())
# Review_comment contiene caracteres no alfabéticos y no tiene dígitos.
print("El comentario contiene caracteres no alfabéticos y no tiene dígitos.", not ( review_comment.isalpha() or review_comment.isdigit()))
  
