"""
Programa principal.

Construye el grafo de municipios, muestra un resumen por consola y genera:
  1. Un mapa interactivo (HTML) con Folium.
  2. Una imagen (PNG) del grafo con matplotlib.

Uso:
    python main.py
"""

from grafo_municipios import construir_grafo, resumen_grafo
from mapa_folium import generar_mapa
from vista_grafo import generar_imagen_grafo


def main():
    # 1. Construir el grafo.
    grafo = construir_grafo()

    # 2. Mostrar resumen por consola.
    resumen_grafo(grafo)

    # 3. Generar el mapa interactivo (HTML).
    archivo_mapa = generar_mapa(grafo)
    print(f"\n[OK] Mapa interactivo generado: {archivo_mapa}")
    print("     Ábrelo en tu navegador para verlo.")

    # 4. Generar la imagen del grafo (PNG).
    archivo_imagen = generar_imagen_grafo(grafo)
    print(f"[OK] Imagen del grafo generada: {archivo_imagen}")


if __name__ == "__main__":
    main()
