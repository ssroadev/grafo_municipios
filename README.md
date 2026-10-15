# Grafo de Municipios con Python (interactivo)

Programa en Python que permite **elegir municipios de un catálogo** y los modela
como un grafo: calcula las distancias reales entre ellos a partir de sus
georreferencias y los muestra en un **mapa interactivo** y en una **imagen del
grafo**.

## ¿Qué hace?

- Muestra un **menú interactivo** con los municipios disponibles y te deja
  elegir cuáles incluir (mínimo 5).
- Te pregunta **cómo conectarlos**: automático (todos con todos), manual o
  usando conexiones predefinidas.
- Representa los municipios como **nodos** y sus conexiones como **aristas**.
- Guarda las **georreferencias** (latitud y longitud) de cada municipio.
- Calcula la **distancia real en kilómetros** entre municipios conectados
  usando la fórmula de **Haversine**.
- Genera un **mapa interactivo** (`mapa_municipios.html`) con Folium, sobre un
  mapa real de OpenStreetMap.
- Genera una **imagen del grafo** (`grafo_municipios.png`) con matplotlib.

## Municipios disponibles en el catálogo

Bogotá, Soacha, Chía, Zipaquirá, Facatativá, Fusagasugá, Girardot, Cajicá,
Mosquera, Madrid, La Calera y Sopó (Cundinamarca, Colombia).

Puedes agregar o cambiar municipios editando `datos_municipios.py`.

## Estructura del proyecto

```
Grafos Python/
├── datos_municipios.py   # Catálogo de municipios y conexiones por defecto
├── menu_interactivo.py   # Menú de selección (municipios y conexiones)
├── grafo_municipios.py   # Construcción del grafo + fórmula de Haversine
├── mapa_folium.py        # Genera el mapa interactivo (HTML)
├── vista_grafo.py        # Genera la imagen del grafo (PNG)
├── main.py               # Programa principal (flujo interactivo)
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

El programa te guiará paso a paso:

1. **Elegir municipios.** Verás la lista numerada; escribe los números
   separados por comas (ej: `1,2,3,4,5`) o escribe `todos`.
2. **Elegir cómo conectarlos:**
   - `1` Automático: conecta todos los municipios entre sí.
   - `2` Manual: tú defines cada conexión (ej: `1-2`, luego `fin`).
   - `3` Predefinidas: usa las conexiones por defecto que apliquen.
3. El programa muestra un **resumen** con coordenadas y distancias, y genera:
   - `mapa_municipios.html` — ábrelo en tu navegador (mapa interactivo).
   - `grafo_municipios.png` — imagen del grafo.

### Ejemplo de ejecución

```
MUNICIPIOS DISPONIBLES
   1. Bogotá       (lat=4.7110, lon=-74.0721)
   2. Soacha       (lat=4.5790, lon=-74.2160)
   ...
Tu selección: 1,2,3,4,5

¿CÓMO CONECTAR LOS MUNICIPIOS?
  1. Automático   2. Manual   3. Predefinidas
Elige una opción (1-3): 3
```

## Fórmula de Haversine

La distancia entre dos puntos sobre la superficie de la Tierra se calcula con:

```
a = sen²(Δlat/2) + cos(lat1)·cos(lat2)·sen²(Δlon/2)
c = 2·asin(√a)
d = R·c          (R = 6371 km, radio medio de la Tierra)
```

## Licencia

Proyecto académico de uso libre.
