# Implementa la función summarize y el CLI.
# Requisitos:
# - summarize(nums) -> dict con claves: count, sum, avg
# - Valida que nums sea lista no vacía y elementos numéricos (acepta strings convertibles a float).
# - CLI: python -m app "1,2,3" imprime: sum=6.0 avg=2.0 count=3

def summarize(nums):  # TODO: tipado opcional
    # Evaluamos que nums no sea vacía, en caso sea así, lanzamos ValueError
    if not nums:
        raise ValueError("La lista no puede estar vacía")
    
    # Recorer cada elemento para validar que sea int, float o convertible a float
    for n in nums:
        # Si no es int o float, intentamos convertir a float
        if not isinstance(n, (int, float)):
            try:
                float(n)
            except ValueError:
                # No es convertible a float lanzamos ValueError
                raise ValueError(f"El elemento '{n}' no es numérico ni convertible a float")
              
    # Pasado las validaciones, convertimos todos a float
    nums = [float(n) for n in nums]
    
    # Calculamos la cantidad de elementos
    count = len(nums)
    # Sumamos los elementos de la lista
    total_sum = sum(nums)
    # Calculamos el promedio con los elementos de la lista
    avg = total_sum / count
    # Retornamos el diccionario con los resultados pedidos
    return {"count": count, "sum": total_sum, "avg": avg}


if __name__ == "__main__":
    import sys
    raw = sys.argv[1] if len(sys.argv) > 1 else ""
    items = [p.strip() for p in raw.split(",") if p.strip()]
    # TODO: validar items y llamar summarize, luego imprimir el formato solicitado
    print("TODO: implementar CLI (python -m app \"1,2,3\")")
    
    try:
        # Llamamos a la función summarize con los items obtenidos del CLI
        result = summarize(items)
        # Imprimimos el resultado en el formato que se pidio (sum=6.0 avg=2.0 count=3)
        print(f"sum={result['sum']} avg={result['avg']} count={result['count']}")
    except ValueError as e:
        # Capturamos el ValueError y mostramos el mensaje de error correspondiente
        print(f"Error: {e}")
