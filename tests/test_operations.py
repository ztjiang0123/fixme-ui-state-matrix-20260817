from state_matrix import operations


def test_fixture_is_importable():
    inputs = operations.OrderQuoteInputs(
        subtotal=10,
        tax=1,
        shipping=2,
        handling=3,
        insurance=4,
        discount=1,
        credit=1,
        tip=1,
    )
    assert operations.quote_order(inputs) == 19

