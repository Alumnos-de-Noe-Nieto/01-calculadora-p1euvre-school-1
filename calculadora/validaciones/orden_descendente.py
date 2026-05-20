"""
Nivel 4: Validación de orden descendente.

Los símbolos deben ir en orden descendente de valor (izquierda a derecha).
Excepción: las 6 formas sustractivas válidas.
Ejemplos válidos: XVI, MDCLXVI, XIV (sustracción válida)
Ejemplos inválidos: IVX, IIV, VIV
"""

def validar_orden_descendente(cadena: str) -> bool:
    valores =  {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    restas_validas = {"IV", "IX", "XL", "XC", "CD", "CM"}

    cadena_limpia = cadena.strip()

    if not cadena_limpia:
        return False
    i = 0
    ultimo_valor = float('inf')

    while i < len(cadena_limpia):
        if i < len(cadena_limpia) - 1:
            actual = cadena_limpia[i]
            siguiente = cadena_limpia[i + 1]
            valor_actual = valores[actual]
            valor_siguiente = valores[siguiente]
            if valor_actual < valor_siguiente:
                par = actual + siguiente
                if par not in restas_validas:
                    return False
                if i > 0 and cadena_limpia[i - 1] == actual:
                    return False
                valor_par = valor_siguiente - valor_actual
                if valor_par > ultimo_valor:
                    return False
                ultimo_valor = valor_par
                i += 2
                continue
        valor_actual = valores[cadena_limpia[i]]
        if valor_actual > ultimo_valor:
            return False
        ultimo_valor = valor_actual
        i += 1
    return True
