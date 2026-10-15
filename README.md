# Grafo de Municipios con Python

Programa en Python que modela **5 municipios de Cundinamarca (Colombia)** como un
grafo, calcula las distancias reales entre ellos a partir de sus georreferencias
y los muestra en un **mapa interactivo** y en una **imagen del grafo**.

## ¿Qué hace?

- Representa los municipios como **nodos** y sus conexiones como **aristas**.
- Guarda las **georreferencias** (latitud y longitud) de cada municipio.
- Calcula la **distancia real en kilómetros** entre municipios conectados
  usando la fórmula de **Haversine**.
- Genera un **mapa interactivo** (`mapa_municipios.html`) con Folium, sobre un
  mapa real de OpenStreetMap.
- Genera una **imagen del grafo** (`grafo_municipios.png`) con matplotlib.

## Municipios incluidos

| Municipio   | Latitud  | Longitud  |
|-------------|----------|-----------|
| Bogotá      | 4.7110   | -74.0721  |
| Soacha      | 4.5790   | -74.2160  |
| Chía        | 4.8619   | -74.0327  |
| Zipaquirá   | 5.0221   | -73.9947  |
| Facatativá  | 4.8167   | -74.3550  |

Puedes cambiar los municipios y sus conexiones editando `datos_municipios.py`.

## Estructura del proyecto

```
Grafos Python/
├── datos_municipios.py   # Coordenadas y conexiones de los municipios
├── grafo_municipios.py   # Construcción del grafo + fórmula de Haversine
├── mapa_folium.py        # Genera el mapa interactivo (HTML)
├── vista_grafo.py        # Genera la imagen del grafo (PNG)
├── main.py               # Programa principal que orquesta todo
├── requirements.txt      # Dependencias del proyecto
├── .gitignore
└── README.md
```

## Requisitos

- Python 3.9 o superior
- Dependencias (ver `requirements.txt`):
  - networkx
  - folium
  - matplotlib

## Instalación

```bash
# (Opcional) crear y activar un entorno virtual
python3 -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

Al ejecutarlo:

1. Imprime en consola un resumen con los municipios, sus coordenadas y las
   distancias entre conexiones.
2. Genera `mapa_municipios.html` — ábrelo en tu navegador para ver el mapa
   interactivo.
3. Genera `grafo_municipios.png` — imagen del grafo.

## Fórmula de Haversine

La distancia entre dos puntos sobre la superficie de la Tierra se calcula con:

```
a = sen²(Δlat/2) + cos(lat1)·cos(lat2)·sen²(Δlon/2)
c = 2·asin(√a)
d = R·c          (R = 6371 km, radio medio de la Tierra)
```

## Licencia

Proyecto académico de uso libre.
