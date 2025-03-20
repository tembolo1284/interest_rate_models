# Black-Karasinski Model Calibration

from typing import Dict, Any
import numpy as np
from scipy.optimize import minimize

def black_karasinski_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate Black-Karasinski Model using Optimization (e.g., BFGS).
    """
    target_vols = market_data.get('target_vols', [])
    time_points = market_data.get('time_points', [])

    def objective(params):
        model.mean_reversion, model.volatility = params
        errors = [(model.price({'time': t}) - v) ** 2 for t, v in zip(time_points, target_vols)]
        return sum(errors)

    result = minimize(objective, [model.mean_reversion, model.volatility], method='BFGS')
    model.mean_reversion, model.volatility = result.x

