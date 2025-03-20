# CIR Model

from typing import Dict, Any
import numpy as np
from interest_rate_models.calibrators.cir_calibration import cir_calibration
from interest_rate_models.pricing.monte_carlo import monte_carlo_pricing


class CIRModel:
    def __init__(self):
        self.mean_reversion = 0.02
        self.volatility = 0.02
        self.long_term_mean = 0.05

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        cir_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any], method: str = 'monte_carlo') -> float:
        return monte_carlo_pricing(self, inputs)

