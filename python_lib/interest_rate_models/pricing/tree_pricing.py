# Tree-Based Pricing Method

import numpy as np
from typing import Dict, Any

def tree_pricing(model: Any, inputs: Dict[str, Any], num_steps: int = 100) -> float:
    """
    Binomial Tree pricing method for American/European options.
    """
    S0 = inputs.get('S0', 100)
    K = inputs.get('K', 100)
    T = inputs.get('T', 1.0)
    dt = T / num_steps

    u = np.exp(model.volatility * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(model.drift * dt) - d) / (u - d)

    prices = np.zeros(num_steps + 1)

    # Terminal payoffs
    for i in range(num_steps + 1):
        prices[i] = max(S0 * (u ** (num_steps - i)) * (d ** i) - K, 0)

    # Backward induction
    for j in range(num_steps - 1, -1, -1):
        for i in range(j + 1):
            prices[i] = np.exp(-model.drift * dt) * (p * prices[i] + (1 - p) * prices[i + 1])

    return prices[0]

