from nose.tools import assert_raises

import pytjson

from .loader import get_examples


def _make_test(example):
    """
    A test function maker.
    """
    def _test():
        if example.success is True:
            try:
                pytjson.loads(example.data)
            except:
                assert False, example
        else:
            assert_raises(
                pytjson.ParseError,
                pytjson.loads,
                example.data)
    _test.__doc__ = ': '.join([example.description, example.data])
    _test.__name__ = 'test_{0}'.format(example.name)
    return _test


# Create individual test functions for each example.
for example in get_examples():
    test = _make_test(example)
    globals()[test.__name__] = test
