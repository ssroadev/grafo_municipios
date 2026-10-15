"""
Generación de una vista del grafo con matplotlib.

Dibuja el grafo como un diagrama clásico de nodos y aristas, ubicando
cada municipio según sus coordenadas geográficas (longitud = x, latitud = y)
y etiquetando las aristas con la distancia en km.
El resultado es una imagen PNG.
"""

import matplotlib
matplotlib.use("Agg")  # backend sin ventana, para guardar en archivo
import matplotlib.pyplot as plt
import networkx as nx


def generar_imagen_grafo(grafo, archivo_salida="grafo_municipios.png"):
    """
    Genera una imagen PNG del grafo.

    grafo: objeto networkx.Graph con nodos que tienen atributo 'pos' (lat, lon)
           y aristas con atributo 'weight'.
    archivo_salida: nombre del archivo PNG a generar.
    Retorna la ruta del archivo generado.
    """
    # Posiciones para el dibujo: x = longitud, y = latitud.
    posiciones = {
        nodo: (datos["pos"][1], datos["pos"][0])
        for nodo, datos in grafo.nodes(data=True)
    }

    plt.figure(figsize=(9, 7))

    # Dibujar aristas.
    nx.draw_networkx_edges(grafo, posiciones, width=2,
                           edge_color="gray", alpha=0.7)

    # Dibujar nodos.
    nx.draw_networkx_nodes(grafo, posiciones, node_size=1400,
                           node_color="#ff6b6b", edgecolors="black")

    # Etiquetas de los municipios.
    nx.draw_networkx_labels(grafo, posiciones, font_size=9,
                            font_weight="bold")

    # Etiquetas de las aristas (distancia en km).
    etiquetas_aristas = {
        (u, v): f"{d['weight']} km"
        for u, v, d in grafo.edges(data=True)
    }
    nx.draw_networkx_edge_labels(grafo, posiciones,
                                 edge_labels=etiquetas_aristas,
                                 font_size=8)

    plt.title("Grafo de municipios (Cundinamarca)\n"
              "Posición según coordenadas geográficas", fontsize=12)
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(archivo_salida, dpi=200)
    plt.close()

    return archivo_salida
