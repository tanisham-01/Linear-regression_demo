import numpy as np
import matplotlib.pyplot as plt


X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Step 1: Calculate Mean
mean_x = np.mean(X)
mean_y = np.mean(y)


# Step 2: Calculate slope (m) and intercept (c)
n = len(X)
numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x) ** 2)
m = numerator / denominator
c = mean_y - m * mean_x

print(f"Slope (m): {m:.2f}")
print(f"Intercept (c): {c:.2f}")

# Step 3: Make predictions
y_pred = m * X + c

# Step 4: Plot the results
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression from Scratch')
plt.legend()
plt.grid(True)
plt.show()

# Step 5: Evaluate with Mean Squared Error (MSE)
mse = np.mean((y - y_pred) ** 2)
print(f"Mean Squared Error: {mse:.2f}")
