"""
Construcción del grafo de municipios con networkx.

- Los nodos son los municipios (guardan sus coordenadas como atributo).
- Las aristas son las conexiones, con la distancia real (km) como peso,
  calculada mediante la fórmula de Haversine.

El grafo se construye a partir de la selección hecha por el usuario.
"""

import math
import networkx as nx

from datos_municipios import CATALOGO_MUNICIPIOS

# Radio medio de la Tierra en kilómetros.
RADIO_TIERRA_KM = 6371.0


def distancia_haversine(coord1, coord2):
    """
    Calcula la distancia en kilómetros entre dos puntos geográficos
    usando la fórmula de Haversine.

    coord1, coord2: tuplas (latitud, longitud) en grados decimales.
    Retorna la distancia en kilómetros (float).
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    lat1_r = math.radians(lat1)
    lon1_r = math.radians(lon1)
    lat2_r = math.radians(lat2)
    lon2_r = math.radians(lon2)

    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r

    a = (math.sin(dlat / 2) ** 2
         + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))

    return RADIO_TIERRA_KM * c


def construir_grafo(municipios, conexiones):
    """
    Construye y retorna el grafo a partir de la selección del usuario.

    municipios: lista de nombres de municipios (deben estar en el catálogo).
    conexiones: lista de tuplas (origen, destino).

    Cada nodo guarda sus coordenadas en el atributo 'pos' (lat, lon).
    Cada arista guarda su distancia en km en el atributo 'weight'.
    """
    grafo = nx.Graph()

    # Agregar nodos con sus coordenadas tomadas del catálogo.
    for nombre in municipios:
        coords = CATALOGO_MUNICIPIOS[nombre]
        grafo.add_node(nombre, pos=coords)

    # Agregar aristas con la distancia real como peso.
    for origen, destino in conexiones:
        coord_origen = CATALOGO_MUNICIPIOS[origen]
        coord_destino = CATALOGO_MUNICIPIOS[destino]
        distancia = distancia_haversine(coord_origen, coord_destino)
        grafo.add_edge(origen, destino, weight=round(distancia, 2))

    return grafo


def resumen_grafo(grafo):
    """
    Imprime en consola un resumen del grafo: municipios, conexiones
    y distancias.
    """
    print("=" * 55)
    print("GRAFO DE MUNICIPIOS")
    print("=" * 55)
    print(f"Municipios (nodos): {grafo.number_of_nodes()}")
    print(f"Conexiones (aristas): {grafo.number_of_edges()}")
    print("-" * 55)

    print("\nGeorreferencias:")
    for nombre, datos in grafo.nodes(data=True):
        lat, lon = datos["pos"]
        print(f"  {nombre:<12} lat={lat:>9.4f}, lon={lon:>9.4f}")

    print("\nConexiones y distancias:")
    for origen, destino, datos in grafo.edges(data=True):
        print(f"  {origen:<12} <--> {destino:<12} {datos['weight']:>7.2f} km")
    print("=" * 55)
