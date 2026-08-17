
class StudentDiscount:
    def apply_discount(self, tuition):
        pass

class PL(StudentDiscount):
    def apply_discount(self, tuition):
        return tuition - (tuition * 1)

class DL(StudentDiscount):
    def apply_discount(self, tuition):
        return tuition - (tuition * 0.50)

class NoDiscount(StudentDiscount):
    def apply_discount(self, tuition):
        return tuition

class Checkout:
    def __init__(self, strategy: StudentDiscount):
        self.strategy = strategy

    def calculate_total(self, tuition):
        return self.strategy.apply_discount(tuition)
