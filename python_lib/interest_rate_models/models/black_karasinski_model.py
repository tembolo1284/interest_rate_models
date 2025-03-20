# Black-Karasinski Model

from typing import Dict, Any
import numpy as np
from interest_rate_models.calibrators.black_karasinski_calibration import black_karasinski_calibration
from interest_rate_models.pricing.monte_carlo import monte_carlo_pricing


class BlackKarasinskiModel:
    def __init__(self):
        self.mean_reversion = 0.03
        self.volatility = 0.01

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        black_karasinski_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any], method: str = 'monte_carlo') -> float:
        return monte_carlo_pricing(self, inputs)

