from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total):
        pass

class FixedDiscount(DiscountStrategy):
    def apply(self, total):
        return total - 10

class PercentageDiscount(DiscountStrategy):
    def apply(self, total):
        return total * 0.9
