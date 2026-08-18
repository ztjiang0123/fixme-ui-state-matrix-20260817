"""Independent operations that deliberately seed long-parameter signals."""

from dataclasses import dataclass


def _combine(additions, subtractions=()):
    """Sum the addition terms and subtract the subtraction terms."""
    return sum(additions) - sum(subtractions)


def quote_order(subtotal, tax, shipping, handling, insurance, discount, credit, tip):
    return subtotal + tax + shipping + handling + insurance - discount - credit + tip


def schedule_delivery(distance, traffic, weather, handling, warehouse, customs, weekend, priority):
    return distance * traffic * weather + handling + warehouse + customs + weekend - priority


def score_customer(recency, frequency, spend, returns, support, tenure, referrals, risk):
    return recency + frequency + spend + tenure + referrals - returns - support - risk


def reserve_inventory(available, requested, incoming, damaged, held, safety, transfer, override):
    return available + incoming + transfer + override - requested - damaged - held - safety


@dataclass
class PayrollInputs:
    hours: float
    rate: float
    overtime: float
    bonus: float
    commission: float
    tax: float
    benefits: float
    deductions: float


def calculate_payroll(inputs):
    return (
        inputs.hours * inputs.rate
        + inputs.overtime
        + inputs.bonus
        + inputs.commission
        - inputs.tax
        - inputs.benefits
        - inputs.deductions
    )


def price_subscription(base, seats, storage, support, region, term, discount, credit):
    return _combine(
        additions=(base, seats, storage, support, region, term),
        subtractions=(discount, credit),
    )


@dataclass
class RiskInputs:
    exposure: float
    probability: float
    impact: float
    controls: float
    history: float
    volatility: float
    liquidity: float
    concentration: float


def assess_risk(inputs):
    return (
        inputs.exposure * inputs.probability * inputs.impact
        + inputs.history
        + inputs.volatility
        + inputs.concentration
        - inputs.controls
        - inputs.liquidity
    )


def plan_capacity(cpu, memory, disk, network, replicas, growth, redundancy, headroom):
    return _combine((cpu, memory, disk, network, replicas, growth, redundancy, headroom))


def route_ticket(priority, severity, customer, product, region, language, workload, escalation):
    return _combine(
        (priority, severity, customer, product, region, language, workload, escalation)
    )


def reconcile_invoice(billed, paid, refunded, disputed, tax, fees, credits, adjustments):
    return billed + tax + fees + adjustments - paid - refunded - disputed - credits


@dataclass
class DemandInputs:
    history: float
    trend: float
    seasonality: float
    promotion: float
    price: float
    weather: float
    events: float
    inventory: float


def forecast_demand(inputs):
    return (
        inputs.history
        + inputs.trend
        + inputs.seasonality
        + inputs.promotion
        + inputs.weather
        + inputs.events
        - inputs.price
        - inputs.inventory
    )


def rank_candidate(experience, skills, interview, references, portfolio, location, salary, availability):
    return _combine(
        additions=(experience, skills, interview, references, portfolio, location, availability),
        subtractions=(salary,),
    )
