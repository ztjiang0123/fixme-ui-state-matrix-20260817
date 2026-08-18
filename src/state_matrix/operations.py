"""Independent operations that deliberately seed long-parameter signals."""

from dataclasses import dataclass


def _combine(additions, subtractions=()):
    """Sum the addition terms and subtract the subtraction terms."""
    return sum(additions) - sum(subtractions)


def _combine_fields(inputs, additions, subtractions=()):
    """Combine named ``inputs`` fields, adding some and subtracting others."""
    return _combine(
        tuple(getattr(inputs, name) for name in additions),
        tuple(getattr(inputs, name) for name in subtractions),
    )


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


@dataclass
class DeliveryInputs:
    distance: float
    traffic: float
    weather: float
    handling: float
    warehouse: float
    customs: float
    weekend: float
    priority: float


def schedule_delivery(inputs):
    return (
        inputs.distance * inputs.traffic * inputs.weather
        + inputs.handling
        + inputs.warehouse
        + inputs.customs
        + inputs.weekend
        - inputs.priority
    )


@dataclass
class CustomerInputs:
    recency: float
    frequency: float
    spend: float
    returns: float
    support: float
    tenure: float
    referrals: float
    risk: float


def score_customer(inputs):
    return (
        inputs.recency
        + inputs.frequency
        + inputs.spend
        + inputs.tenure
        + inputs.referrals
        - inputs.returns
        - inputs.support
        - inputs.risk
    )


@dataclass
class InventoryInputs:
    available: float
    requested: float
    incoming: float
    damaged: float
    held: float
    safety: float
    transfer: float
    override: float


def reserve_inventory(inputs):
    return _combine_fields(
        inputs,
        additions=("available", "incoming", "transfer", "override"),
        subtractions=("requested", "damaged", "held", "safety"),
    )


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


@dataclass
class TicketInputs:
    priority: float
    severity: float
    customer: float
    product: float
    region: float
    language: float
    workload: float
    escalation: float


def route_ticket(inputs):
    return _combine(
        (
            inputs.priority,
            inputs.severity,
            inputs.customer,
            inputs.product,
            inputs.region,
            inputs.language,
            inputs.workload,
            inputs.escalation,
        )
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
    return _combine_fields(
        inputs,
        additions=("billed", "tax", "fees", "adjustments"),
        subtractions=("paid", "refunded", "disputed", "credits"),
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
