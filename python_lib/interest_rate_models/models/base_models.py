# Python Pricing and Calibration Library

# Folder structure:
# - interest_rate_models/
#    - models/
#    - calibrators/
#    - pricing/
#    - tests/

# Initializing with necessary imports and base classes for models

from abc import ABC, abstractmethod
from typing import Dict, Any
import numpy as np
from scipy.optimize import minimize
from interest_rate_models.calibrators.calibrators import (
    ho_lee_calibration, vasicek_calibration, cir_calibration,
    black_karasinski_calibration, hull_white_calibration
)


class InterestRateModel(ABC):
    """
    Abstract base class for all interest rate models.
    """

    @abstractmethod
    def calibrate(self, market_data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def price(self, inputs: Dict[str, Any]) -> float:
        pass


class HoLeeModel(InterestRateModel):
    def __init__(self):
        self.volatility = 0.01
        self.drift = 0.0

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        ho_lee_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any]) -> float:
        return np.random.normal(100, self.volatility)


class VasicekModel(InterestRateModel):
    def __init__(self):
        self.mean_reversion = 0.03
        self.volatility = 0.01
        self.long_term_mean = 0.05

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        vasicek_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any]) -> float:
        return np.random.normal(100, self.volatility)


class CIRModel(InterestRateModel):
    def __init__(self):
        self.mean_reversion = 0.02
        self.volatility = 0.02
        self.long_term_mean = 0.05

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        cir_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any]) -> float:
        return np.random.normal(100, self.volatility)


class BlackKarasinskiModel(InterestRateModel):
    def __init__(self):
        self.mean_reversion = 0.03
        self.volatility = 0.01

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        black_karasinski_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any]) -> float:
        return np.random.normal(100, self.volatility)


class HullWhiteModel(InterestRateModel):
    def __init__(self):
        self.mean_reversion = 0.05
        self.volatility = 0.015

    def calibrate(self, market_data: Dict[str, Any]) -> None:
        hull_white_calibration(market_data, self)

    def price(self, inputs: Dict[str, Any]) -> float:
        return np.random.normal(100, self.volatility)


# Example usage
market_data = {
    'target_rates': [0.02, 0.025, 0.03],
    'time_points': [1, 2, 3],
    'rates': [0.015, 0.02, 0.025],
    'dt': 1.0,
    'target_vols': [0.01, 0.015, 0.02],
    'target_swaptions': [0.01, 0.015, 0.02]
}

models = [HoLeeModel(), VasicekModel(), CIRModel(), BlackKarasinskiModel(), HullWhiteModel()]

for model in models:
    model.calibrate(market_data)
    price = model.price({'example': 'input'})
    print(f"{model.__class__.__name__}: Price = {price}")

