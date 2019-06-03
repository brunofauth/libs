class Box(object):

    def __init__(self, boxed):
        self._boxed = iter(boxed)
    
    def map(self, function):
        self._boxed = map(function, self._boxed)
        return self

    def __iter__(self):
        return self._boxed

