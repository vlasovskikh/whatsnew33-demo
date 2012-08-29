"""Explicit unicode literals.

See also <http://www.python.org/dev/peps/pep-0414/>.
"""

import unittest

class UnicodeLiteralTest(unittest.TestCase):
    def test_bytes(self):
        self.assertIsInstance(b'foo', bytes)

    def test_implicit_unicode(self):
        self.assertIsInstance('foo', str)

    def test_explicit_unicode(self):
        self.assertIsInstance(u'foo', str)
