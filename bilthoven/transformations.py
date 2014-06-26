def template(current_block, previous_block, random_parameter):
    """This is just a no-op transformation for you to see what interface you should provide."""
    return current_block


def reverse(current_block, *args):
    """Reverses the data of the current block."""
    return current_block[::-1]


def diff(current_block, previous_block, *args):
    """Substracts the previous block from the current block."""
    return current_block - previous_block
