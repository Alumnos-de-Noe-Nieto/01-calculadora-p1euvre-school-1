"""
Nivel 5: Validación de restas válidas (Análisis Semántico).

Solamente 6 pares específicos de símbolos son permitidos para restar:
IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)

Ejemplos válidos: IV, IX, XL, XC, CD, CM, XIV (X + IV)
Ejemplos inválidos: IL (49), IC (99), XD (490), XM (990), VX (5), LC (50)
"""


def validar_restas(cadena: str) -> bool:
    cadena_limpia = cadena.strip()
    if not cadena_limpia:
        return False
    valores = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sustracciones_validas = {"IV", "IX", "XL", "XC", "CD", "CM"}
    for i in range(len(cadena_limpia) - 1):
        actual = cadena_limpia[i]
        siguiente = cadena_limpia[i + 1]

        if valores[actual] < valores[siguiente]:
            par = actual + siguiente
            if par not in sustracciones_validas:
                return False
            if i > 0 and cadena_limpia[i - 1] == actual:
                return False
    return True

