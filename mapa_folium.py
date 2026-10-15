"""
Generación del mapa interactivo con Folium.

Dibuja los municipios como marcadores sobre un mapa real y traza sus
conexiones como líneas, mostrando la distancia de cada tramo.
El resultado es un archivo HTML que se abre en el navegador.
"""

import folium


def generar_mapa(grafo, archivo_salida="mapa_municipios.html"):
    """
    Genera un mapa interactivo (HTML) a partir del grafo.

    grafo: objeto networkx.Graph con nodos que tienen atributo 'pos'
           y aristas con atributo 'weight'.
    archivo_salida: nombre del archivo HTML a generar.
    Retorna la ruta del archivo generado.
    """
    # Calcular el centro del mapa como el promedio de las coordenadas.
    latitudes = [datos["pos"][0] for _, datos in grafo.nodes(data=True)]
    longitudes = [datos["pos"][1] for _, datos in grafo.nodes(data=True)]
    centro = [sum(latitudes) / len(latitudes),
              sum(longitudes) / len(longitudes)]

    # Crear el mapa base centrado en los municipios.
    mapa = folium.Map(location=centro, zoom_start=10,
                      tiles="OpenStreetMap")

    # Dibujar las conexiones (aristas) como líneas.
    for origen, destino, datos in grafo.edges(data=True):
        coord_origen = grafo.nodes[origen]["pos"]
        coord_destino = grafo.nodes[destino]["pos"]
        distancia = datos["weight"]

        folium.PolyLine(
            locations=[coord_origen, coord_destino],
            color="blue",
            weight=3,
            opacity=0.7,
            tooltip=f"{origen} ↔ {destino}: {distancia} km",
        ).add_to(mapa)

    # Dibujar los municipios (nodos) como marcadores.
    for nombre, datos in grafo.nodes(data=True):
        lat, lon = datos["pos"]
        # Número de conexiones de este municipio.
        grado = grafo.degree(nombre)
        popup_html = (
            f"<b>{nombre}</b><br>"
            f"Lat: {lat:.4f}<br>"
            f"Lon: {lon:.4f}<br>"
            f"Conexiones: {grado}"
        )
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_html, max_width=200),
            tooltip=nombre,
            icon=folium.Icon(color="red", icon="map-marker", prefix="fa"),
        ).add_to(mapa)

    mapa.save(archivo_salida)
    return archivo_salida
