"""
Nivel 8: Orquestación del Pipeline Completo
Este módulo contiene la función principal para evaluar expresiones aritméticas de números romanos.
"""

from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    if not expresion or expresion.strip() == "":
        raise ExpresionInvalida(f'La expresion "{expresion}" esta vacia')
    try:
        tokens = parsear_expresion(expresion)
    except ExpresionInvalida:
        raise
    if not tokens:
        raise ExpresionInvalida(f'La expresion "{expresion}" no produjo tokens')
    #filtra espacios
    tokens_sin_espacios = [t for t in tokens if t.tipo != "ESPACIO"]
    resultado = None
    operador_actual = None

    for token in tokens_sin_espacios:
        if token.tipo == "ROMANO":
            valor_entero = romano_a_entero(token.valor)

            if resultado is None:
                resultado = valor_entero
            elif operador_actual == "SUMA":
                resultado += valor_entero
            elif operador_actual == "RESTA":
                resultado -= valor_entero
        elif token.tipo in ["SUMA", "RESTA"]:
            operador_actual = token.tipo
    if resultado is None:
        raise ExpresionInvalida(f'No se puede evaluar la expresion "{expresion}"')
    if resultado <= 0:
        raise ExpresionInvalida(f'El resultado de la expresion "{expresion}" es {resultado}, debe ser positivo')
    return resultado
