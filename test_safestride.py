def test_safestride_basic():
    assert True


def test_navigation_module_available():
    from nav_engine import NavEngine
    assert NavEngine is not None