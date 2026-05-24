# Ideales para eliminar duplicados de forma masiva y realizar operaciones matemáticas 
# de intersección o unión de datos. No tienen orden fijo (no usan índices)
id_usuarios:set[int] = {101, 102, 103, 101, 104, 102, 104}

print(f'Set (sin duplicados): {id_usuarios}')

# ------------------------------------------------------------------------------

# Operación útil para analistas: Intersección (elementos en común entre dos sets)
activos:set[int] = {1, 2, 3, 4}
morosos:set[int] = {3, 4, 5, 6}
bloquear_cuenta:set[int] = activos.intersection(morosos)

print(f'Clientes activos con deuda: {bloquear_cuenta}')