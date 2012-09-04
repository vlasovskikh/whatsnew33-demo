"""Implicit namespace packages.

See also <http://www.python.org/dev/peps/pep-0420/>.
"""

import pkg1.m1, pkg1.m2

print(pkg1.m1, pkg1.m2)



import nspkg1.m1, nspkg1.m2

print(nspkg1.m1, nspkg1.m2)
