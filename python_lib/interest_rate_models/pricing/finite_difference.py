# Finite Difference Pricing Method

import numpy as np
from typing import Dict, Any

def finite_difference_pricing(model: Any, inputs: Dict[str, Any]) -> float:
    """
    Basic Crank-Nicolson Finite Difference Method for pricing.
    """
    S0 = inputs.get('S0', 100)
    K = inputs.get('K', 100)
    T = inputs.get('T', 1.0)
    N = inputs.get('N', 100)
    M = inputs.get('M', 100)
    dt = T / N

    # Initialize the grid
    prices = np.zeros((N + 1, M + 1))
    S = np.linspace(0, 2 * K, M + 1)

    # Set up boundary conditions
    prices[-1, :] = np.maximum(S - K, 0)
    prices[:, 0] = 0
    prices[:, -1] = S[-1] - K

    alpha = 0.25 * dt * (model.volatility ** 2 * (S / K) ** 2 - model.drift * (S / K))
    beta = -0.5 * dt * (model.volatility ** 2 * (S / K) ** 2 + model.drift * (S / K))
    gamma = 0.25 * dt * (model.volatility ** 2 * (S / K) ** 2 + model.drift * (S / K))

    # Crank-Nicolson scheme
    for i in range(N - 1, -1, -1):
        for j in range(1, M):
            prices[i, j] = (alpha[j] * prices[i + 1, j - 1] +
                            (1 + beta[j]) * prices[i + 1, j] +
                            gamma[j] * prices[i + 1, j + 1])

    # Interpolation to find the price at S0
    return np.interp(S0, S, prices[0, :])

