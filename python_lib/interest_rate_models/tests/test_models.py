import pytest
import logging
import numpy as np
from interest_rate_models.models.ho_lee_model import HoLeeModel
from interest_rate_models.models.vasicek_model import VasicekModel
from interest_rate_models.models.cir_model import CIRModel
from interest_rate_models.models.black_karasinski_model import BlackKarasinskiModel
from interest_rate_models.models.hull_white_model import HullWhiteModel

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture
def mock_market_data():
    logger.info("Setting up mock market data for testing...")
    return {
        'target_rates': [0.015, 0.016, 0.017, 0.018, 0.019, 0.02, 0.022, 0.023, 0.024, 0.025, 0.026, 0.027, 0.028, 0.029],
        'time_points': [1/365, 2/365, 1/12, 2/12, 3/12, 6/12, 1, 2, 3, 5, 7, 10, 20, 30],
        'rates': [0.015, 0.016, 0.017, 0.018, 0.019, 0.02, 0.022, 0.023, 0.024, 0.025, 0.026, 0.027, 0.028, 0.029],
        'dt': 1.0,
        'target_vols': [0.01] * 14,
        'target_swaptions': [0.01] * 14
    }


def test_ho_lee_model(mock_market_data):
    logger.info("Testing Ho-Lee Model...")
    model = HoLeeModel()
    model.calibrate(mock_market_data)
    price = model.price({'S0': 100, 'T': 1.0, 'dt': 0.01}, method='monte_carlo')
    assert isinstance(price, float)
    logger.info(f"Ho-Lee Model Test Passed. Price: {price}")


def test_vasicek_model(mock_market_data):
    logger.info("Testing Vasicek Model...")
    model = VasicekModel()
    model.calibrate(mock_market_data)
    price = model.price({'S0': 100, 'T': 1.0, 'dt': 0.01})
    assert isinstance(price, float)
    logger.info(f"Vasicek Model Test Passed. Price: {price}")


def test_cir_model(mock_market_data):
    logger.info("Testing CIR Model...")
    model = CIRModel()
    model.calibrate(mock_market_data)
    price = model.price({'S0': 100, 'T': 1.0, 'dt': 0.01})
    assert isinstance(price, float)
    logger.info(f"CIR Model Test Passed. Price: {price}")


def test_black_karasinski_model(mock_market_data):
    logger.info("Testing Black-Karasinski Model...")
    model = BlackKarasinskiModel()
    model.calibrate(mock_market_data)
    price = model.price({'S0': 100, 'T': 1.0, 'dt': 0.01})
    assert isinstance(price, float)
    logger.info(f"Black-Karasinski Model Test Passed. Price: {price}")


def test_hull_white_model(mock_market_data):
    logger.info("Testing Hull-White Model...")
    model = HullWhiteModel()
    model.calibrate(mock_market_data)
    price = model.price({'S0': 100, 'T': 1.0, 'dt': 0.01})
    assert isinstance(price, float)
    logger.info(f"Hull-White Model Test Passed. Price: {price}")

