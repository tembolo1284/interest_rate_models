import logging
from interest_rate_models.models.ho_lee_model import HoLeeModel
from interest_rate_models.models.vasicek_model import VasicekModel
from interest_rate_models.models.cir_model import CIRModel
from interest_rate_models.models.black_karasinski_model import BlackKarasinskiModel
from interest_rate_models.models.hull_white_model import HullWhiteModel

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_models():
    logger.info("Initializing models...")
    models = [
        HoLeeModel(),
        VasicekModel(),
        CIRModel(),
        BlackKarasinskiModel(),
        HullWhiteModel()
    ]

    mock_market_data = {
        'target_rates': [0.015, 0.016, 0.017, 0.018, 0.019, 0.02, 0.022, 0.023, 0.024, 0.025, 0.026, 0.027, 0.028, 0.029],
        'time_points': [1/365, 2/365, 1/12, 2/12, 3/12, 6/12, 1, 2, 3, 5, 7, 10, 20, 30],
        'rates': [0.015, 0.016, 0.017, 0.018, 0.019, 0.02, 0.022, 0.023, 0.024, 0.025, 0.026, 0.027, 0.028, 0.029],
        'dt': 1.0,
        'target_vols': [0.01] * 14,
        'target_swaptions': [0.01] * 14
    }

    for model in models:
        model_name = model.__class__.__name__
        logger.info(f"Calibrating {model_name}...")
        model.calibrate(mock_market_data)
        logger.info(f"{model_name} calibrated successfully.")

        logger.info(f"Pricing with {model_name} using Monte Carlo method...")
        price = model.price({'S0': 100, 'T': 1.0, 'dt': 0.01})
        logger.info(f"{model_name} Price: {price}")


if __name__ == "__main__":
    run_models()

