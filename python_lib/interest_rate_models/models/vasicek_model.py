# Vasicek Model

from typing import Dict, Any
import numpy as np
from interest_rate_models.calibrators.vasicek_calibration import vasicek_calibration
from interest_rate_models.pricing.monte_carlo import monte_carlo_pricing


class VasicekModel:
    def __init__(self):
        self.mean_reversion = 0.03
        self.volatility = 0.01
        self.long_term_mean = 0.05

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        vasicek_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any], method: str = 'monte_carlo') -> float:
        return monte_carlo_pricing(self, inputs)

