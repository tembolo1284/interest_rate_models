# Ho-Lee Model Calibration

from typing import Dict, Any
import numpy as np
from scipy.optimize import minimize

def ho_lee_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate Ho-Lee Model using simple Least Squares Fitting.
    """
    target_rates = market_data.get('target_rates', [])
    time_points = market_data.get('time_points', [])

    def objective(params):
        model.volatility, model.drift = params
        errors = [(model.price({'time': t}) - r) ** 2 for t, r in zip(time_points, target_rates)]
        return sum(errors)

    result = minimize(objective, [model.volatility, model.drift], method='BFGS')
    model.volatility, model.drift = result.x

