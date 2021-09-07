from .exceptions import ContextException


class DummyLibrary:
    def __init__(self):
        pass

    def confirm_product(self, a, b, res):
        if a * b == res:
            return True
        else:
            return False
