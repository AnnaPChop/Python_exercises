'''Añade a la lista movies_filtered las películas de movies_info que se produjeron en los EE. UU. y que duran más de 150 minutos.'''
#Código
movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

movies_filtered = []

for movie in movies_info: # un bucle sobre cada película
    if movie[1] == 'USA' and movie[4] > 150: # si la película se produjo en los EE.UU. y dura más de 150 minutos,
        movies_filtered.append(movie) # la añadimos

for movie in movies_filtered:
    for elem in movie:
        print(f'{elem:<46}', end='')
    print()
