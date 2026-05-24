temperaturas:list[float] = [22.5, 45.0, 18.3, 50.2, 31.1]

# ------------------------------------------------------------------------------

# Opción verbosa, no optimizada
t30 = []
for temp in temperaturas:
  if temp > 30:
    t30.append(temp)

# ------------------------------------------------------------------------------

# Comprensión de lista
t30:list[float] = [temp for temp in temperaturas if temp > 30]

print(f'Temperaturas mayores a 30°: {t30}')