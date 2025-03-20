# Hull-White Model Calibration

from typing import Dict, Any
import numpy as np
from scipy.optimize import minimize

def hull_white_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate Hull-White Model using Optimization (e.g., L-BFGS-B).
    """
    target_swaptions = market_data.get('target_swaptions', [])
    time_points = market_data.get('time_points', [])

    def objective(params):
        model.mean_reversion, model.volatility = params
        errors = [(model.price({'time': t}) - s) ** 2 for t, s in zip(time_points, target_swaptions)]
        return sum(errors)

    result = minimize(objective, [model.mean_reversion, model.volatility], method='L-BFGS-B')
    model.mean_reversion, model.volatility = result.x

