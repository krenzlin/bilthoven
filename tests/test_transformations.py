from numpy import array

def test_template():
    from bilthoven.transformations import template

    assert template([], [], None) == []
    assert template(range(10), [], None) == range(10)


def test_reverse():
    from bilthoven.transformations import reverse

    assert reverse([]) == []
    assert reverse(range(10)) == list(reversed(range(10)))

    np_array = array(range(10))
    assert list(reverse(np_array)) == list(reversed(np_array))


def test_diff():
    from bilthoven.transformations import diff

    a = array([1,2,3,4])
    b = array([1,1,1,1])
    assert all(diff(a, b) == array([0,1,2,3]))
