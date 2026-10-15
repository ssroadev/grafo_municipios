"""
Programa principal (interactivo).

1. Pregunta al usuario qué municipios incluir (del catálogo) y cómo
   conectarlos.
2. Construye el grafo con esa selección.
3. Muestra un resumen por consola.
4. Genera un mapa interactivo (HTML) con Folium.
5. Genera una imagen (PNG) del grafo con matplotlib.

Uso:
    python main.py
"""

from menu_interactivo import flujo_interactivo
from grafo_municipios import construir_grafo, resumen_grafo
from mapa_folium import generar_mapa
from vista_grafo import generar_imagen_grafo


def main():
    # 1. Selección interactiva de municipios y conexiones.
    municipios, conexiones = flujo_interactivo()

    # 2. Construir el grafo con la selección del usuario.
    grafo = construir_grafo(municipios, conexiones)

    # 3. Mostrar resumen por consola.
    print()
    resumen_grafo(grafo)

    # 4. Generar el mapa interactivo (HTML).
    archivo_mapa = generar_mapa(grafo)
    print(f"\n[OK] Mapa interactivo generado: {archivo_mapa}")
    print("     Ábrelo en tu navegador para verlo.")

    # 5. Generar la imagen del grafo (PNG).
    archivo_imagen = generar_imagen_grafo(grafo)
    print(f"[OK] Imagen del grafo generada: {archivo_imagen}")

    print("\n¡Listo! 🎉")


if __name__ == "__main__":
    main()
