# CIR Model Calibration

from typing import Dict, Any
import numpy as np
from scipy.optimize import minimize

def cir_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate CIR Model using Generalized Method of Moments (GMM).
    """
    rates = market_data.get('rates', [])
    dt = market_data.get('dt', 1.0)

    def objective(params):
        mean_reversion, long_term_mean, volatility = params
        model.mean_reversion = mean_reversion
        model.long_term_mean = long_term_mean
        model.volatility = volatility

        errors = []
        for i in range(1, len(rates)):
            drift = mean_reversion * (long_term_mean - rates[i-1]) * dt
            variance = volatility ** 2 * rates[i-1] * dt
            moment_error = (rates[i] - rates[i-1] - drift) ** 2 - variance
            errors.append(moment_error ** 2)
        return sum(errors)

    initial_params = [model.mean_reversion, model.long_term_mean, model.volatility]
    result = minimize(objective, initial_params, method='BFGS')
    model.mean_reversion, model.long_term_mean, model.volatility = result.x

