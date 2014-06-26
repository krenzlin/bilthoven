from itertools import izip
from numpy import array, array_equal


def test_block_iterator():
    from bilthoven.process_functions import block_iterator

    data = range(10)
    assert array_equal(list(block_iterator(data, 5, 5)), [array([0,1,2,3,4]), array([5,6,7,8,9])])

    result = [array([0,1,2,3,4,5]), array([6,7,8,9])]
    for ret, res in izip(block_iterator(data, 6, 6), result):
        assert array_equal(ret, res)

    result = [array([0,1,2,3,4]), array([3,4,5,6,7]), array([6,7,8,9])]
    for ret, res in izip(block_iterator(data, 5, 3), result):
        assert array_equal(ret, res)


