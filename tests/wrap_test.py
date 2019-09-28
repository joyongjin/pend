from unittest import TestCase

import pend


class WrapTest(TestCase):
    def test_wrap(self):
        assert hasattr(pend, 'parse')
