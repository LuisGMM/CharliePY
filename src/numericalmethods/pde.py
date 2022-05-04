
import numpy as np


def __tridiag(a: float, b: float, c: float, k1: int = -1, k2: int = 0, k3: int = 1) -> np.ndarray:
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)



def parabollic(theta, h: float, k: float, x0: float, xf: float, tf: float, u0: np.ndarray) -> np.ndarray:
    
    sigma = k/h**2

    x = np.arange(x0, xf+h, h)
    t = np.arange(0, tf+h, h)

    LEN_X = len(x)
    LEN_T = len(t)

    left_matrix = np.zeros((LEN_X, LEN_X))
    np.fill_diagonal()
    right_matrix = np.array([])
