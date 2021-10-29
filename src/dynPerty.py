import numpy as np
from scipy.stats import beta

class DynamicPersonality:
    def __init__(self):
        self.a = 1.0
        self.b = 1.0
        # Personality Beta Curve
        self.pbc = None
        self.max_range = 100

    def inherit(self, perality):
        self.a = perality.a + np.random.uniform(-1, 1)
        self.b = perality.b +np.random.uniform(-1, 1)
        self.pbc = beta(self.a, self.b)

    def generate(self, x, a=0.0, b=0.0):
        if a == 0.0 and b == 0.0:
            # a,b = 6.0, 4.11
            a,b = self.a, self.b
        self.pbc = beta(a=a, b=b)
        return self.pbc

    def getIndex(self, x, a=0.0, b=0.0, size=1000):
        if a == 0.0 and b == 0.0:
            a,b = self.a, self.b
        # rv = beta(a=a, b=b)
        return beta.rvs(a, b, size=size)

    def genCurve(self, x, a=0.0, b=0.0):
        return beta.pdf(x, a=a, b=b, scale=1)
