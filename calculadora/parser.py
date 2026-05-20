"""
Nivel 7: Parsing de Expresiones
Este módulo contiene las funciones para parsear expresiones aritméticas con números romanos.
"""

from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    tipo: str
    valor: str
    posicion: int


def evaluar_expresion(expresion: str) -> list[Token]:
    if not expresion or expresion.strip() == "":
        return []
    try:
        tokens = tokenizar_expresion(expresion)

        if not validar_estructura_tokens(tokens):
            raise ExpresionInvalida(f'La expresion "{expresion}" tiene una estructura invalida')
        return tokens
    except ExpresionInvalida:
        raise
    except Exception as e:
        raise ExpresionInvalida(f'La expresion "{expresion}" tiene una estructura invalida') from e


def tokenizar_expresion(expresion: str) -> list[Token]:
    tokens = []
    i = 0
    longitud = len(expresion)

    while i < longitud:
        caracter = expresion[i]

        if caracter == ' ':
            tokens.append(Token("ESPACIO", " ", i))
            i += 1

        elif caracter == "+":
            tokens.append(Token("SUMA", "+", i))
            i += 1

        elif caracter == '-':
            tokens.append(Token("RESTA", "-", i))
            i += 1

        elif caracter in "IVXLCDM":
            inicio = i
            while i < longitud and expresion[i] in "IVXLCDM":
                i += 1

            valor_romano = expresion[inicio:i]
            tokens.append(Token("ROMANO", valor_romano, inicio))

        else:
            raise ExpresionInvalida(f"Caracter invalido '{caracter}' en posicionj {i}")
    return tokens


def validar_estructura_tokens(tokens: list[Token]) -> bool:
    tokens_sin_espacios = [t for t in tokens if t.tipo != "ESPACIO"]

    if len(tokens_sin_espacios) < 3:
        return False
    if len(tokens_sin_espacios) % 2 == 0:
        return False
    for i, token in enumerate(tokens_sin_espacios):
        if i % 2 == 0:
            if token.tipo != "ROMANO":
                return False
        else:
            if token.tipo not in ["SUMA", "RESTA"]:
                return False
    return True

