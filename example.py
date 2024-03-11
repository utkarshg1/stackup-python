from stackup_python import stackup
import numpy as np

size=100000
dim1 = stackup.dimension(mean=30, tol=15, size=size)
dim2 = stackup.dimension(mean=40, tol=20, size=size)

seed = 42
a = dim1.generate(seed)
b = dim2.generate(seed)

c = np.sqrt(a**2 + b**2)

mu = np.mean(c)
sigma = np.std(c)

print(c)
print(f'Average value of c : {mu:.2f}')
print(f'Standard Deviation : {sigma:.2f}')
print(f'Maximum : {mu+3*sigma:.2f}')
print(f'Minimum : {mu-3*sigma:.2f}')

stackup.plot_dist(c)

stackup.fit_dist(c)

df = stackup.get_data_frame(a=a, b=b, c=c)
print(df)

print(stackup.describe_dims(a=a, b=b, c=c))