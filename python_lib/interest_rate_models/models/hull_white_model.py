import numpy as np
from interest_rate_models.calibrators.hull_white_calibration import hull_white_calibration
from interest_rate_models.pricing.monte_carlo import monte_carlo_pricing
from interest_rate_models.pricing.finite_difference import finite_difference_pricing
from interest_rate_models.pricing.tree_pricing import tree_pricing


class HullWhiteModel:
    def __init__(self):
        self.params = {}

    def calibrate(self, market_data):
        """
        Calibrate the Hull-White model using market data.
        """
        self.params = hull_white_calibration(market_data)

    def price(self, inputs, method='monte_carlo'):
        """
        Price an instrument using the specified pricing method.

        Args:
            inputs (dict): A dictionary containing inputs such as S0, K, T, dt.
            method (str): Pricing method - 'monte_carlo', 'finite_difference', or 'tree'.

        Returns:
            float: The calculated price of the instrument.
        """
        if method == 'monte_carlo':
            return monte_carlo_pricing(self, inputs)
        elif method == 'finite_difference':
            return finite_difference_pricing(self, inputs)
        elif method == 'tree':
            return tree_pricing(self, inputs)
        else:
            raise ValueError(f"Invalid pricing method: {method}")

