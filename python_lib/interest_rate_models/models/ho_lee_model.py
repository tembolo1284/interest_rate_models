# Ho-Lee Model

from typing import Dict, Any
import numpy as np
from interest_rate_models.calibrators.ho_lee_calibration import ho_lee_calibration
from interest_rate_models.pricing.monte_carlo import monte_carlo_pricing
from interest_rate_models.pricing.finite_difference import finite_difference_pricing
from interest_rate_models.pricing.tree_pricing import tree_pricing


class HoLeeModel:
    def __init__(self):
        self.volatility = 0.01
        self.drift = 0.0

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        ho_lee_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any], method: str = 'monte_carlo') -> float:
        if method == 'monte_carlo':
            return monte_carlo_pricing(self, inputs)
        elif method == 'finite_difference':
            return finite_difference_pricing(self, inputs)
        elif method == 'tree':
            return tree_pricing(self, inputs)

