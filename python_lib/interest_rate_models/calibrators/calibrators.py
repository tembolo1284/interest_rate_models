# Calibration Techniques for Interest Rate Models

from typing import Dict, Any
import numpy as np
from scipy.optimize import minimize


def ho_lee_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate Ho-Lee Model using simple Least Squares Fitting.
    """
    target_rates = market_data.get('target_rates', [])
    time_points = market_data.get('time_points', [])

    def objective(params):
        model.volatility, model.drift = params
        errors = [(model.price({'time': t}) - r) ** 2 for t, r in zip(time_points, target_rates)]
        return sum(errors)

    result = minimize(objective, [model.volatility, model.drift], method='BFGS')
    model.volatility, model.drift = result.x


def vasicek_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate Vasicek Model using Maximum Likelihood Estimation (MLE).
    """
    rates = market_data.get('rates', [])
    dt = market_data.get('dt', 1.0)

    def log_likelihood(params):
        mean_reversion, long_term_mean, volatility = params
        model.mean_reversion = mean_reversion
        model.long_term_mean = long_term_mean
        model.volatility = volatility
        log_likelihood_sum = 0.0
        for i in range(1, len(rates)):
            drift = mean_reversion * (long_term_mean - rates[i-1]) * dt
            variance = volatility ** 2 * dt
            log_likelihood_sum += -0.5 * ((rates[i] - rates[i-1] - drift) ** 2 / variance + np.log(variance))
        return -log_likelihood_sum

    initial_params = [model.mean_reversion, model.long_term_mean, model.volatility]
    result = minimize(log_likelihood, initial_params, method='BFGS')
    model.mean_reversion, model.long_term_mean, model.volatility = result.x


def cir_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate CIR Model using Generalized Method of Moments (GMM).
    """
    rates = market_data.get('rates', [])
    dt = market_data.get('dt', 1.0)

    def objective(params):
        mean_reversion, long_term_mean, volatility = params
        model.mean_reversion = mean_reversion
        model.long_term_mean = long_term_mean
        model.volatility = volatility

        errors = []
        for i in range(1, len(rates)):
            drift = mean_reversion * (long_term_mean - rates[i-1]) * dt
            variance = volatility ** 2 * rates[i-1] * dt
            moment_error = (rates[i] - rates[i-1] - drift) ** 2 - variance
            errors.append(moment_error ** 2)
        return sum(errors)

    initial_params = [model.mean_reversion, model.long_term_mean, model.volatility]
    result = minimize(objective, initial_params, method='BFGS')
    model.mean_reversion, model.long_term_mean, model.volatility = result.x


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


def hull_white_calibration(market_data: Dict[str, Any], model: Any) -> None:
    """
    Calibrate Hull-White Model using Optimization (e.g., Levenberg-Marquardt).
    """
    target_swaptions = market_data.get('target_swaptions', [])
    time_points = market_data.get('time_points', [])

    def objective(params):
        model.mean_reversion, model.volatility = params
        errors = [(model.price({'time': t}) - s) ** 2 for t, s in zip(time_points, target_swaptions)]
        return sum(errors)

    result = minimize(objective, [model.mean_reversion, model.volatility], method='L-BFGS-B')
    model.mean_reversion, model.volatility = result.x

