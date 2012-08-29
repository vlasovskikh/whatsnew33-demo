What's New In Python 3.3
========================

Based on [What's New In Python 3.3][1] by Raymond Hettinger.

New syntax features:

* New `yield from` expression for [generator delegation][PEP-380].
* The `u'unicode'` syntax is accepted again for `str` objects.
* New `raise ... from None` syntax for suppressing exception context.

New library modules:

* `faulthandler` (helps debugging low-level crashes)
* `ipaddress` (high-level objects representing IP addresses and masks)
* `lzma` (compress data using the XZ / LZMA algorithm)
* `venv` (Python [virtual environments][PEP-405], as in the popular
  `virtualenv` package)

New built-in features:

* Reworked [I/O exception hierarchy][PEP-3151]

Other features:

* Native support for implicit namespace packages (PEP 420).
* Qualified name `__qualname__` for classes and functions (PEP 3155).


Implementation improvements:

* Rewritten import machinery based on `importlib`.
* More compact unicode strings.
* More compact attribute dictionaries.

Security improvements:

* Hash randomization is switched on by default.

Please read on for a comprehensive list of user-facing changes.


  [1]: http://docs.python.org/dev/whatsnew/3.3.html
  [PEP-380]: http://www.python.org/dev/peps/pep-0380/
  [PEP-405]: http://www.python.org/dev/peps/pep-0405/
  [PEP-3151]: http://www.python.org/dev/peps/pep-03151/
