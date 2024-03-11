import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fitter import Fitter,  get_common_distributions

class dimension:

    def __init__(self, mean, tol, size=10000):
        self.mean = mean
        self.tol = tol
        self.size = size

    def generate(self, random_seed=None):
        if random_seed is not None:
            np.random.seed(random_seed)
            x = np.random.normal(loc=self.mean, scale=self.tol/3, size=self.size)
        else:
            x = np.random.normal(loc=self.mean, scale=self.tol/3, size=self.size)
        return x

def plot_dist(x):
    plt.figure(figsize=(10, 5))
    sns.histplot(x, kde=True)
    plt.title('Histogram for Dimension')
    plt.show()
    plt.savefig('histogram.png')

def fit_dist(x):
    f = Fitter(x, distributions=get_common_distributions())
    f.fit()
    f.summary()
    best_fit = f.get_best()
    print(f'Best fitted distribution : {best_fit}')

def get_data_frame(**dims):
    df = pd.DataFrame(dims)
    return df

def describe_dims(**dims):
    df = get_data_frame(**dims)
    d = df.describe().T
    return d
