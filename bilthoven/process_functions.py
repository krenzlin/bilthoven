from numpy import array, zeros, append


def block_iterator(data, block_size=1024, hop_size=1024):
    """
    Iterates over the given data in blocks.

    :param block_size: int
    :param hop_size: int
    :return: iterator
    """
    i = 0
    while i < len(data):
        yield array(data[i:i+block_size])
        i += hop_size


def process(data, transformation, block_size=1024, hop_size=None):
    """Applies transformation on audio data blockwise."""
    if not hop_size:
        hop_size = block_size

    processed_data = []

    random_parameter = 0  # TODO random walk
    previous_block = zeros(block_size)
    for current_block in block_iterator(data, block_size=block_size, hop_size=hop_size):
        processed_block = transformation(current_block, previous_block, random_parameter)
        processed_data += list(processed_block)
        previous_block = current_block
    return array(processed_data)


def process_multi(data, *args, **kwargs):
    """Like :func:`process` but can handle multichannel audio data."""
    if len(data.shape) == 1:
        return process(data, *args)
    elif len(data.shape) == 2:
        processed_data = []
        for i in range(data.shape[1]):
            processed_channel = process(data[:, i], *args, **kwargs)
            processed_data.append(processed_channel)
        return array(processed_data).transpose()
        
