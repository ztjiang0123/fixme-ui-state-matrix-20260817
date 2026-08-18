"""Independent operations that deliberately seed long-parameter signals."""

from dataclasses import dataclass


@dataclass
class SubscriptionPricing:
    """Inputs required to price a subscription.

    Groups the charge components and the reductions that travel together
    through :func:`price_subscription`.
    """

    base: float
    seats: float
    storage: float
    support: float
    region: float
    term: float
    discount: float
    credit: float


def quote_order(subtotal, tax, shipping, handling, insurance, discount, credit, tip):
    return subtotal + tax + shipping + handling + insurance - discount - credit + tip


def schedule_delivery(distance, traffic, weather, handling, warehouse, customs, weekend, priority):
    return distance * traffic * weather + handling + warehouse + customs + weekend - priority


def score_customer(recency, frequency, spend, returns, support, tenure, referrals, risk):
    return recency + frequency + spend + tenure + referrals - returns - support - risk


def reserve_inventory(available, requested, incoming, damaged, held, safety, transfer, override):
    return available + incoming + transfer + override - requested - damaged - held - safety


def calculate_payroll(hours, rate, overtime, bonus, commission, tax, benefits, deductions):
    return hours * rate + overtime + bonus + commission - tax - benefits - deductions


def price_subscription(pricing):
    return (
        pricing.base
        + pricing.seats
        + pricing.storage
        + pricing.support
        + pricing.region
        + pricing.term
        - pricing.discount
        - pricing.credit
    )


def assess_risk(exposure, probability, impact, controls, history, volatility, liquidity, concentration):
    return exposure * probability * impact + history + volatility + concentration - controls - liquidity


def plan_capacity(cpu, memory, disk, network, replicas, growth, redundancy, headroom):
    return cpu + memory + disk + network + replicas + growth + redundancy + headroom


def route_ticket(priority, severity, customer, product, region, language, workload, escalation):
    return priority + severity + customer + product + region + language + workload + escalation


def reconcile_invoice(billed, paid, refunded, disputed, tax, fees, credits, adjustments):
    return billed + tax + fees + adjustments - paid - refunded - disputed - credits


def forecast_demand(history, trend, seasonality, promotion, price, weather, events, inventory):
    return history + trend + seasonality + promotion + weather + events - price - inventory


def rank_candidate(experience, skills, interview, references, portfolio, location, salary, availability):
    return experience + skills + interview + references + portfolio + location - salary + availability

