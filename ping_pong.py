"""Generator delegation.

See also <http://www.python.org/dev/peps/pep-0380/>.
"""

def pong_core(msg):
    while True:
        msg = yield 'pong {0}'.format(msg)


def pong():
    try:
        msg = yield
        yield from pong_core(msg)
    except GeneratorExit:
        print('pong stopped')


def ping(pong, requests):
    next(pong)
    for request in requests:
        print('ping', request)
        reply = pong.send(request)
        print('got', reply)
    pong.close()


generator = pong()
ping(generator, range(10000))
