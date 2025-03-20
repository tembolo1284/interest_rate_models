# Monte Carlo Pricing Method

import numpy as np
from typing import Dict, Any

def monte_carlo_pricing(model: Any, inputs: Dict[str, Any], num_paths: int = 10000, antithetic: bool = True) -> float:
    """
    Monte Carlo simulation with Antithetic Sampling for variance reduction.
    """
    T = inputs.get('T', 1.0)
    dt = inputs.get('dt', 0.01)
    S0 = inputs.get('S0', 100)

    num_steps = int(T / dt)
    prices = np.zeros(num_paths)

    for i in range(num_paths):
        path = [S0]
        path_antithetic = [S0] if antithetic else None

        for _ in range(num_steps):
            Z = np.random.normal()
            if antithetic:
                Z_antithetic = -Z

            S_new = path[-1] + model.drift * dt + model.volatility * np.sqrt(dt) * Z
            path.append(S_new)

            if antithetic:
                S_new_antithetic = path_antithetic[-1] + model.drift * dt + model.volatility * np.sqrt(dt) * Z_antithetic
                path_antithetic.append(S_new_antithetic)

        if antithetic:
            prices[i] = 0.5 * (path[-1] + path_antithetic[-1])
        else:
            prices[i] = path[-1]

    return np.mean(prices)

