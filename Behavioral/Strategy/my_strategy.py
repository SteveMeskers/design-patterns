from abc import ABC
import cmath


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b**2-4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        outcome = b**2-4*a*c
        return float('nan') if outcome < 0 else outcome


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        dis = complex(self.strategy.calculate_discriminant(a, b, c))
        return (
            (-b + cmath.sqrt(dis)) / 2*a,
            (-b - cmath.sqrt(dis)) / 2*a
        )
