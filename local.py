
class LocalError(Exception):
    def __init__(self, message):
        self.message = message


def runA():
    raise LocalError('hello')


def runB():
    a = 1
    b = 0
    return a/b


def run():
    try:
        runA()
    except Exception:
        pass

    try:
        runB()
    except Exception:
        pass
