import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
file_path = "lab4.xlsx"
df = pd.read_excel(file_path)

# Determine the number of products and parameters
n_products = df.shape[1] - 2  # Subtracting two columns (name and criterion)
n_params = df.shape[0]

# Initialize the array of criteria and compute normalized values
f = np.zeros((n_params, n_products))
f0 = np.zeros((n_params, n_products))

# Fill the criteria array f
for product in range(n_products):
    for criterion in range(n_params):
        f[criterion][product] = df.iloc[criterion, product + 1]  # Index shifted by 1

# Calculate the sum of criteria and normalize them
sum_f = np.sum(f, axis=1)
for i in range(n_params):
    f0[i] = f[i] / sum_f[i]

# Calculate integro for each product
G = np.ones(n_params)
G0 = G / np.sum(G)
G_global = G0[0]

integro = np.zeros(n_products)
for i in range(n_params):
    integro += G0[i] * (1 - f0[i]) ** (-1)

# Find the optimal product
optimal_product = np.argmax(integro)
print('The best product - ', optimal_product + 1)

# Display plots
x = np.arange(n_products)
plt.figure(figsize=(10, 6))
plt.bar(x, integro, color='#4bb2c5')
plt.xlabel('Products')
plt.ylabel('Integro')
plt.title('Integro for each product')
plt.show()

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

for i in range(n_params):
    xs = np.arange(n_products)
    ys = np.full((n_products,), i)
    zs = f[i]
    ax.bar(xs, zs, zs=i, zdir='y', color=np.random.rand(3, ))

ax.set_xlabel('Products')
ax.set_ylabel('Criteria')
ax.set_zlabel('Values')
plt.title('3D Bar chart for criteria values')
plt.show()
