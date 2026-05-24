# Perfectas para datos que nunca deben alterarse durante la ejecución. Al ser 
# inmutables, son más veloces en memoria que las listas
coordenadas:tuple[float, float] = (4.6097, -74.0817)
# coordenadas[0] = 5.123 # !! Esto lanzará un TypeError

print(f'Latitud: {coordenadas[0]}')