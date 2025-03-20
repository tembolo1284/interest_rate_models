# Vasicek Model Calibration

from typing import Dict, Any
import numpy as np
from scipy.optimize import minimize

def vasicek_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate Vasicek Model using Maximum Likelihood Estimation (MLE).
    """
    rates = market_data.get('rates', [])
    dt = market_data.get('dt', 1.0)

    def log_likelihood(params):
        mean_reversion, long_term_mean, volatility = params
        model.mean_reversion = mean_reversion
        model.long_term_mean = long_term_mean
        model.volatility = volatility
        log_likelihood_sum = 0.0
        for i in range(1, len(rates)):
            drift = mean_reversion * (long_term_mean - rates[i-1]) * dt
            variance = volatility ** 2 * dt
            log_likelihood_sum += -0.5 * ((rates[i] - rates[i-1] - drift) ** 2 / variance + np.log(variance))
        return -log_likelihood_sum

    initial_params = [model.mean_reversion, model.long_term_mean, model.volatility]
    result = minimize(log_likelihood, initial_params, method='BFGS')
    model.mean_reversion, model.long_term_mean, model.volatility = result.x

