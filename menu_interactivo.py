"""
Módulo interactivo: menú de selección de municipios y conexiones.

Muestra al usuario el catálogo de municipios disponibles (tipo lista
desplegable en consola) y le pide:
  1. Qué municipios incluir (mínimo 5).
  2. Cómo conectarlos: automático (todos con todos), manual, o conexiones
     predefinidas.

Devuelve la selección de municipios y la lista de conexiones elegidas.
"""

import itertools

from datos_municipios import CATALOGO_MUNICIPIOS, CONEXIONES_POR_DEFECTO

MINIMO_MUNICIPIOS = 5


def _leer_opcion_numerica(mensaje, minimo, maximo):
    """Lee un número entero válido dentro de un rango [minimo, maximo]."""
    while True:
        entrada = input(mensaje).strip()
        if not entrada.isdigit():
            print("  ⚠ Escribe un número válido.")
            continue
        valor = int(entrada)
        if valor < minimo or valor > maximo:
            print(f"  ⚠ Elige un número entre {minimo} y {maximo}.")
            continue
        return valor


def mostrar_catalogo():
    """Imprime el catálogo de municipios numerado."""
    print("\n" + "=" * 50)
    print("MUNICIPIOS DISPONIBLES")
    print("=" * 50)
    nombres = list(CATALOGO_MUNICIPIOS.keys())
    for i, nombre in enumerate(nombres, start=1):
        lat, lon = CATALOGO_MUNICIPIOS[nombre]
        print(f"  {i:>2}. {nombre:<12} (lat={lat:.4f}, lon={lon:.4f})")
    print("=" * 50)
    return nombres


def seleccionar_municipios():
    """
    Pide al usuario elegir municipios del catálogo (mínimo 5).

    Retorna una lista con los nombres de los municipios seleccionados.
    """
    nombres = mostrar_catalogo()
    total = len(nombres)

    print(f"\nSelecciona al menos {MINIMO_MUNICIPIOS} municipios.")
    print("Escribe los números separados por comas (ej: 1,2,3,4,5)")
    print(f"o escribe 'todos' para incluir los {total}.")

    while True:
        entrada = input("\nTu selección: ").strip().lower()

        if entrada == "todos":
            return nombres[:]

        # Procesar números separados por comas.
        partes = [p.strip() for p in entrada.split(",") if p.strip()]
        if not all(p.isdigit() for p in partes):
            print("  ⚠ Usa solo números separados por comas (ej: 1,2,3,4,5).")
            continue

        indices = [int(p) for p in partes]
        if any(i < 1 or i > total for i in indices):
            print(f"  ⚠ Hay números fuera de rango (1 a {total}).")
            continue

        # Quitar duplicados conservando el orden.
        seleccion = []
        for i in indices:
            nombre = nombres[i - 1]
            if nombre not in seleccion:
                seleccion.append(nombre)

        if len(seleccion) < MINIMO_MUNICIPIOS:
            print(f"  ⚠ Debes elegir al menos {MINIMO_MUNICIPIOS} "
                  f"municipios (elegiste {len(seleccion)}).")
            continue

        return seleccion


def _conexiones_todos_con_todos(municipios):
    """Genera conexiones entre todos los pares de municipios."""
    return list(itertools.combinations(municipios, 2))


def _conexiones_predefinidas(municipios):
    """
    Filtra las conexiones por defecto para quedarse solo con las que
    unen municipios que el usuario seleccionó.
    """
    conjunto = set(municipios)
    return [(a, b) for a, b in CONEXIONES_POR_DEFECTO
            if a in conjunto and b in conjunto]


def _conexiones_manuales(municipios):
    """Permite al usuario definir manualmente las conexiones."""
    print("\nDefine las conexiones manualmente.")
    print("Municipios seleccionados:")
    for i, nombre in enumerate(municipios, start=1):
        print(f"  {i:>2}. {nombre}")
    print("\nEscribe cada conexión como dos números separados por un guion")
    print("(ej: 1-2). Escribe 'fin' cuando termines.")

    conexiones = []
    total = len(municipios)
    while True:
        entrada = input("  Conexión (o 'fin'): ").strip().lower()
        if entrada == "fin":
            if not conexiones:
                print("  ⚠ Debes crear al menos una conexión.")
                continue
            break

        partes = entrada.split("-")
        if len(partes) != 2 or not all(p.strip().isdigit() for p in partes):
            print("  ⚠ Formato inválido. Usa, por ejemplo: 1-2")
            continue

        a, b = int(partes[0]), int(partes[1])
        if a < 1 or a > total or b < 1 or b > total:
            print(f"  ⚠ Números fuera de rango (1 a {total}).")
            continue
        if a == b:
            print("  ⚠ Un municipio no se conecta consigo mismo.")
            continue

        conexion = (municipios[a - 1], municipios[b - 1])
        # Evitar duplicados (sin importar el orden).
        if any({conexion[0], conexion[1]} == {c[0], c[1]}
               for c in conexiones):
            print("  ⚠ Esa conexión ya existe.")
            continue

        conexiones.append(conexion)
        print(f"    ✓ {conexion[0]} <-> {conexion[1]}")

    return conexiones


def seleccionar_conexiones(municipios):
    """
    Pregunta al usuario cómo quiere conectar los municipios.

    Retorna la lista de conexiones (tuplas de nombres).
    """
    print("\n" + "=" * 50)
    print("¿CÓMO CONECTAR LOS MUNICIPIOS?")
    print("=" * 50)
    print("  1. Automático: conectar todos con todos")
    print("  2. Manual: definir cada conexión")
    print("  3. Predefinidas: usar las conexiones por defecto")
    print("     (solo las que apliquen a tu selección)")

    opcion = _leer_opcion_numerica("\nElige una opción (1-3): ", 1, 3)

    if opcion == 1:
        return _conexiones_todos_con_todos(municipios)
    if opcion == 2:
        return _conexiones_manuales(municipios)

    # opción 3
    conexiones = _conexiones_predefinidas(municipios)
    if not conexiones:
        print("\n  ⚠ Ninguna conexión por defecto aplica a tu selección.")
        print("    Se conectarán todos con todos automáticamente.")
        return _conexiones_todos_con_todos(municipios)
    return conexiones


def flujo_interactivo():
    """
    Ejecuta el flujo completo de selección y retorna:
        (municipios_seleccionados, conexiones)
    """
    print("\n╔" + "═" * 48 + "╗")
    print("║" + " GENERADOR DE GRAFOS DE MUNICIPIOS ".center(48) + "║")
    print("╚" + "═" * 48 + "╝")

    municipios = seleccionar_municipios()
    conexiones = seleccionar_conexiones(municipios)

    print(f"\n✓ {len(municipios)} municipios y {len(conexiones)} conexiones "
          "seleccionados.")
    return municipios, conexiones
