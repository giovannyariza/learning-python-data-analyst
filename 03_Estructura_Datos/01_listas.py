# Ideales para guardar colecciones cronológicas o elementos que cambian constantemente
# Permiten cualquier tipo de dato y elementos repetidos
lenguajes:list[str] = ['Python', 'SQL', 'R', 'Python']
# Modificar por índice (base 0)
lenguajes[1] = 'T-SQL'
# Agregar elemento al final de la lista
lenguajes.append('Scala')
# Eliminar un elemento de la lista
del lenguajes[3]
# Eliminar el último elemento de la lista
lenguajes.pop()

# Imprimir elementos de la lista por su índice
print(f'Lenguaje en la 3ra posición: {lenguajes[2]}')
# Imprimir la lista completa
print(f'Lista completa {lenguajes}')