"""Implicit namespace packages.

See also <http://www.python.org/dev/peps/pep-0420/>.
"""

from nspkg1 import m1, m2

print(m1, m2)

class C:
    pass

def f():
    pass

print(C().__qualname__)
#print(f.__qualname__)
