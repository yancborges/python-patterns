from operator import mod, eq
from typing import Callable, Any
from functools import wraps, partial


def compose(*funcs):
    def inner(arg):
        state = arg
        for func in reversed(funcs):
            state = func(state)
        return state
    return inner


def is_int(func: Callable) -> Callable:
    @wraps(func)
    def inner(val: Any) -> Any:
        return func(val) if isinstance(val, int) else val
    return inner


@is_int
def queijo(n: int) -> str:
    return 'queijo' if eq(n % 3, 0) else n


@is_int
def goiabada(n: int) -> str:
    return 'goiabada' if eq(n % 5, 0) else n


@is_int
def queijo_goiabada(n: int) -> str:
    return 'romeu e julieta' if eq(n % 3, 0) and eq(n % 5, 0) else n


romeu_julieta = compose(goiabada, queijo, queijo_goiabada)
romeus_julietas = compose(list, partial(map, romeu_julieta))


"""
def romeu_julieta(val: int):
    if queijo_goiabada(val) == 'romeu e julieta':
        return 'romeu e julieta'

    if queijo(val) == 'queijo':
        return 'queijo'

    if goiabada(val) == 'goiabada':
        return 'goiabada'
"""