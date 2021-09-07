from example_robot_framework import dummy
from example_robot_framework import ContextException


class DummyTranslation(object):

    def __init__(self):
        self.dummy = dummy.DummyLibrary()

    def confirm_the_product_of(self, a, b, res):
        if self.dummy.confirm_product(int(a), int(b), int(res)) is True:
            return True
        else:
            raise ContextException("Could not confirm that the product of {} and {} is {}.".format(a, b, res))

    def confirm_the_product_of_is_not(self, a, b, res):
        if self.dummy.confirm_product(int(a), int(b), int(res)) is False:
            return True
        else:
            raise ContextException("The product of {} and {} is in fact {}.".format(a, b, res))
