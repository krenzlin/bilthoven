def test_template():
    from bilthoven.transformations import template

    assert template([], [], None) == []
    assert template(range(10), [], None) == range(10)
