from state_matrix import operations


def test_fixture_is_importable():
    assert operations.quote_order(10, 1, 2, 3, 4, 1, 1, 1) == 19

