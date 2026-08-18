"""Independent operations that deliberately seed long-parameter signals."""

from dataclasses import dataclass


def _combine(additions, subtractions=()):
    """Sum the addition terms and subtract the subtraction terms."""
    return sum(additions) - sum(subtractions)


@dataclass
class OrderQuoteInputs:
    subtotal: float
    tax: float
    shipping: float
    handling: float
    insurance: float
    discount: float
    credit: float
    tip: float


def quote_order(inputs):
    return (
        inputs.subtotal
        + inputs.tax
        + inputs.shipping
        + inputs.handling
        + inputs.insurance
        - inputs.discount
        - inputs.credit
        + inputs.tip
    )


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


@dataclass
class SubscriptionInputs:
    base: float
    seats: float
    storage: float
    support: float
    region: float
    term: float
    discount: float
    credit: float


def price_subscription(inputs):
    return _combine(
        additions=(
            inputs.base,
            inputs.seats,
            inputs.storage,
            inputs.support,
            inputs.region,
            inputs.term,
        ),
        subtractions=(inputs.discount, inputs.credit),
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


@dataclass
class CapacityInputs:
    cpu: float
    memory: float
    disk: float
    network: float
    replicas: float
    growth: float
    redundancy: float
    headroom: float


def plan_capacity(inputs):
    return _combine(
        (
            inputs.cpu,
            inputs.memory,
            inputs.disk,
            inputs.network,
            inputs.replicas,
            inputs.growth,
            inputs.redundancy,
            inputs.headroom,
        )
    )


def route_ticket(priority, severity, customer, product, region, language, workload, escalation):
    return _combine(
        (priority, severity, customer, product, region, language, workload, escalation)
    )


@dataclass
class InvoiceInputs:
    billed: float
    paid: float
    refunded: float
    disputed: float
    tax: float
    fees: float
    credits: float
    adjustments: float


def reconcile_invoice(inputs):
    return (
        inputs.billed
        + inputs.tax
        + inputs.fees
        + inputs.adjustments
        - inputs.paid
        - inputs.refunded
        - inputs.disputed
        - inputs.credits
    )


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


@dataclass
class CandidateInputs:
    experience: float
    skills: float
    interview: float
    references: float
    portfolio: float
    location: float
    salary: float
    availability: float


def rank_candidate(inputs):
    return _combine(
        additions=(
            inputs.experience,
            inputs.skills,
            inputs.interview,
            inputs.references,
            inputs.portfolio,
            inputs.location,
            inputs.availability,
        ),
        subtractions=(inputs.salary,),
    )
