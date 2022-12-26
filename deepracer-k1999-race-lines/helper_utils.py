import numpy as np
import re
import sys

def array2D_repr_columns(arr: np.ndarray, col: int, precision: int = 5) -> str:
    opt = np.get_printoptions()
    np.set_printoptions(precision=precision, suppress=True, threshold=sys.maxsize)
    arr_repr = np.array_repr(arr)
    np.set_printoptions(**opt)

    pattern = r'( *\[[^]]+\]),?\n?'
    for _ in range(col-1):
        pattern += r' *(\[[^]]+\]),?\n?'

    repl = r''
    for i in range(1, col + 1):
        repl += r'\g<{}>,'.format(i)
        repl += r'\t' if i != col else r'\n'

    return re.sub(pattern, repl, arr_repr)

def array1D_repr_columns(arr: np.ndarray, col: int, precision: int = 5) -> str:
    opt = np.get_printoptions()
    np.set_printoptions(precision=precision, suppress=True, threshold=sys.maxsize)
    arr_repr = np.array_repr(arr)
    np.set_printoptions(**opt)

    pattern = r''
    for _ in range(col):
        pattern += r' *(\d\.[\d ]+),?\n? *'

    repl = r''
    for i in range(1, col + 1):
        repl += r'\g<{}>, '.format(i)
    repl += r'\n       '

    repr_cols = re.sub(r'\n      ', r'', arr_repr)
    return re.sub(pattern, repl, repr_cols)