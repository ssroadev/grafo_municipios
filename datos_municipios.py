"""
Catálogo de municipios disponibles con sus georreferencias.

Cada municipio tiene su nombre y coordenadas (latitud, longitud).
Este es el catálogo del que el usuario elige al ejecutar el programa.

Puedes agregar más municipios siguiendo el mismo formato:
    "Nombre": (latitud, longitud),
"""

# Catálogo de municipios: nombre -> (latitud, longitud)
# Municipios de Cundinamarca (Colombia) y alrededores de Bogotá.
CATALOGO_MUNICIPIOS = {
    "Bogotá":       (4.7110, -74.0721),
    "Soacha":       (4.5790, -74.2160),
    "Chía":         (4.8619, -74.0327),
    "Zipaquirá":    (5.0221, -73.9947),
    "Facatativá":   (4.8167, -74.3550),
    "Fusagasugá":   (4.3376, -74.3637),
    "Girardot":     (4.3049, -74.8017),
    "Cajicá":       (4.9185, -74.0280),
    "Mosquera":     (4.7059, -74.2300),
    "Madrid":       (4.7324, -74.2659),
    "La Calera":    (4.7210, -73.9690),
    "Sopó":         (4.9087, -73.9400),
}

# Conexiones por defecto (se usan solo si el usuario elige el modo
# "conexiones predefinidas" y los municipios seleccionados coinciden).
CONEXIONES_POR_DEFECTO = [
    ("Bogotá", "Soacha"),
    ("Bogotá", "Chía"),
    ("Bogotá", "Facatativá"),
    ("Chía", "Zipaquirá"),
    ("Zipaquirá", "Facatativá"),
    ("Soacha", "Facatativá"),
]
