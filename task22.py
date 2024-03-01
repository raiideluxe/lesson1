melt = {
    "CuO": 1200,
    "SO3": 200,
    "Fe2O3": 1565,
    "Al2O3": 2072
}
melting_temperatures = []

for substance, temperature in melt.items():
    if 'O' in substance:
        melting_temperatures.append(str(temperature))

print(" ".join(melting_temperatures))