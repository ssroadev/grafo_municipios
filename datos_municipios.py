"""
Datos de los municipios y sus conexiones.

Cada municipio tiene un nombre y sus georreferencias (latitud, longitud).
Las conexiones definen qué municipios están unidos en el grafo.

Se eligieron 5 municipios de Cundinamarca (Colombia) cercanos a Bogotá.
Puedes modificar libremente estos datos para usar otros municipios.
"""

# Municipios: nombre -> (latitud, longitud)
# Coordenadas aproximadas del casco urbano de cada municipio.
MUNICIPIOS = {
    "Bogotá":    (4.7110, -74.0721),
    "Soacha":    (4.5790, -74.2160),
    "Chía":      (4.8619, -74.0327),
    "Zipaquirá": (5.0221, -73.9947),
    "Facatativá":(4.8167, -74.3550),
}

# Conexiones entre municipios (aristas del grafo).
# Cada tupla representa una vía/relación entre dos municipios.
CONEXIONES = [
    ("Bogotá", "Soacha"),
    ("Bogotá", "Chía"),
    ("Bogotá", "Facatativá"),
    ("Chía", "Zipaquirá"),
    ("Zipaquirá", "Facatativá"),
    ("Soacha", "Facatativá"),
]
