"""Suppressing exception context.


"""


def f(d):
    try:
        return d['foo']
    except KeyError:
        #from None
        raise ValueError("foo dicts are not allowed")

f({'key1': 'value1'})
