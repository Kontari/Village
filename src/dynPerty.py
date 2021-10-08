import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt


class DynamicPersonality:
    def __init__(self):
        self.a = 1.0
        self.b = 1.0
        self.per = None
        self.max_range = 100

    def randomPersonality(self):
        self.getPersonalityIndex()


    def inheritedPersonality(self):
        self.shape = 2.0
        self.scale = 2.0
        self.per = np.random.beta(self.shape, self.scale, self.max_range)

    def getPersonalityIndex(self, x, a=0.0, b=0.0):
        if a == 0.0 and b == 0.0:
            # a,b = 6.0, 4.11
            a,b = self.a, self.b
        # x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99, a, b), 100)
        rv = beta(a=a, b=b)
        # fig, ax = plt.subplots(ncols = 1, nrows = 1, figsize = (12,5), sharex = True)
        return rv.pdf(x)