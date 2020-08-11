import builtins
from collections import defaultdict


collector = defaultdict(list)


OldException = builtins.Exception


class NewException(OldException):

    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        super().__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if not getattr(cls.__init__, 'collect', None):
            old_init = cls.__init__
            def __init__(i, *args, **kwargs):
                import inspect
                s = inspect.stack()
                collector[cls].append((i, (args, kwargs), s))

                old_init(i, *args, **kwargs)

            __init__.collect = True
            cls.__init__ = __init__

        return super().__new__(cls, *args, **kwargs)


builtins.Exception = NewException

# TODO replace all builtin execption


#---------------------------------#
from local import run

try:
    run()
except OldException:
    pass

print(collector)
