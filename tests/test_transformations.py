from numpy import array, array_equal

def test_template():
    from bilthoven.transformations import template

    assert array_equal(template(array([]), array([]), None), array([]))
    assert array_equal(template(array(range(10)), array([]), None), array(range(10)))


def test_reverse():
    from bilthoven.transformations import reverse

    assert array_equal(reverse(array([])), array([]))
    assert array_equal(reverse(array(range(10))), list(reversed(array(range(10)))))

    np_array = array(range(10))
    assert list(reverse(np_array)) == list(reversed(np_array))


def test_diff():
    from bilthoven.transformations import diff

    a = array([1,2,3,4])
    b = array([1,1,1,1])
    assert array_equal(diff(a, b), array([0,1,2,3]))
