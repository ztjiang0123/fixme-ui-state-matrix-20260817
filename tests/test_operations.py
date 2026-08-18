from state_matrix import operations


def test_fixture_is_importable():
    assert operations.quote_order(10, 1, 2, 3, 4, 1, 1, 1) == 19


def test_price_subscription_uses_pricing_object():
    pricing = operations.SubscriptionPricing(
        base=100,
        seats=10,
        storage=5,
        support=3,
        region=2,
        term=1,
        discount=4,
        credit=2,
    )
    assert operations.price_subscription(pricing) == 115

