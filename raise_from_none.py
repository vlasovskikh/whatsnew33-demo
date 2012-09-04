"""Suppressing exception context.

See also <http://www.python.org/dev/peps/pep-0409/>.
"""


def f(d):
    try:
        return d['foo']
    except KeyError:
        raise ValueError("foo dicts are not allowed") from None

f({'key1': 'value1'})
