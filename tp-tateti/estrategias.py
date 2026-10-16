"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)


def minimax_max(tateti: Tateti, estado: List[List[str]]) -> float:
    """
    Valor minimax de un estado desde el turno de MAX.

    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero

    Returns:
        float: Utilidad (1.0, 0.5 o 0.0) desde la perspectiva de MAX
    """
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)

    valor = float('-inf')

    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = max(valor, minimax_min(tateti, sucesor))

    return valor


def minimax_min(tateti: Tateti, estado : List[List[str]]) -> float:
    """
    Valor minimax de un estado desde el turno de MIN.

    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero

    Returns:
        float: Utilidad (1.0, 0.5 o 0.0) desde la perspectiva de MAX
    """
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)

    valor = float('inf')

    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = min(valor, minimax_max(tateti, sucesor))

    return valor


def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]: # type: ignore
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """
    if tateti.jugador(estado) == JUGADOR_MAX:
        sucs = {
            accion : minimax_min(tateti, tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return max(sucs, key = sucs.get) # type: ignore

    if tateti.jugador(estado) == JUGADOR_MIN:
        sucs = {
            accion : minimax_max(tateti, tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return min(sucs, key = sucs.get) # type: ignore