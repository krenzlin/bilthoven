from itertools import izip
from numpy import array, array_equal


def test_block_iterator():
    from bilthoven.process_functions import block_iterator

    data = range(10)
    assert array_equal(list(block_iterator(data, 5, 5)), [array([0,1,2,3,4]), array([5,6,7,8,9])])

    result_should = [array([0,1,2,3,4,5]), array([6,7,8,9])]
    for ret, res in izip(block_iterator(data, 6, 6), result_should):
        assert array_equal(ret, res)

    result_should = [array([0,1,2,3,4]), array([3,4,5,6,7]), array([6,7,8,9])]
    for ret, res in izip(block_iterator(data, 5, 3), result_should):
        assert array_equal(ret, res)



def test_process():
    from bilthoven.process_functions import process_single_channel
    from bilthoven.transformations import reverse

    data = array(range(10))

    result_should = array([1,0,3,2,5,4,7,6,9,8])
    result_is = process_single_channel(data, reverse, block_size=2)
    assert array_equal(result_is, result_should)

