"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos


def romano_a_entero(cadena: str) -> int:

    cadena_limpia = cadena.strip().upper()

    if not cadena_limpia:
        raise ExpresionInvalida("La cadena esta vacia")
    #validaciones de niveles 1 al 5
    if not validar_simbolos(cadena_limpia):
        raise ExpresionInvalida(f'"{cadena_limpia}" contiene simbolos invalidos')
    if not validar_repeticiones_icxm(cadena_limpia):
        raise ExpresionInvalida(f'"{cadena_limpia}" tiene repeticiones invalidas de I/X/C/M')
    if not validar_repeticiones_vld(cadena_limpia):
        raise ExpresionInvalida(f'"{cadena_limpia}" tiene repeticiones invalidas de V/L/D')
    if not validar_orden_descendente(cadena_limpia):
        raise ExpresionInvalida(f'"{cadena_limpia}" tiene orden decendiente invalido')
    if not validar_restas(cadena_limpia):
        raise ExpresionInvalida(f'"{cadena_limpia}" tiene orden decendiente invalido')
    if not validar_restas(cadena_limpia):
        raise ExpresionInvalida(f'"{cadena_limpia}" tiene restas invalidas')
    #"convertir"
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    i = 0
    while i < len(cadena_limpia):
        valor_actual = valores[cadena_limpia[i]]
        if i + 1 < len(cadena_limpia):
            valor_siguiente = valores[cadena_limpia[i+1]]
            if valor_actual < valor_siguiente:
                total += valor_siguiente - valor_actual
                i += 2
                continue
        total += valor_actual
        i += 1
    return total
