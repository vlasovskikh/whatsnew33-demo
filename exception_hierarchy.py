"""Reworking the OS and IO exception hierarchy.

See also <http://www.python.org/dev/peps/pep-3151/>.
"""

from errno import ENOENT, EACCES, EPERM

try:
    with open("document.txt", "r") as f:
        content = f.read()
except OSError as err:
    if err.errno == ENOENT:
        print("document.txt file is missing")
    elif err.errno in (EACCES, EPERM):
        print("You are not allowed to read document.txt")
    else:
        raise


try:
    with open("document.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("document.txt file is missing")
except PermissionError:
    print("You are not allowed to read document.txt")
