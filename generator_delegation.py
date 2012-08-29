"""Generator delegation.

See also <http://www.python.org/dev/peps/pep-0380/>.
"""

def g(x):
    yield from range(x, 0, -1)
    yield from range(x + 1)

#list(g(5))
