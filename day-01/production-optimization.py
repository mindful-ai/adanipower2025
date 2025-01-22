from scipy.optimize import linprog

# Coefficients of the objective function (profit per unit for each product)
c = [-10, -15, -20]  # Negative because linprog performs minimization

# Coefficients of the inequality constraints
# Machine 1: 2x1 + 3x2 + 1x3 <= 10
# Machine 2: 3x1 + 2x2 + 4x3 <= 12
# Material: 5x1 + 4x2 + 6x3 <= 50
# Energy: 3x1 + 2x2 + 4x3 <= 30
A_ub = [
    [2, 3, 1],  # Machine 1 constraint
    [3, 2, 4],  # Machine 2 constraint
    [5, 4, 6],  # Material constraint
    [3, 2, 4]   # Energy constraint
]

# Right-hand side of the inequalities
b_ub = [10, 12, 50, 30]

# Bounds for the decision variables (must be >= 0)
x_bounds = [(0, None), (0, None), (0, None)]  # No upper bound, only non-negative values

# Solving the optimization problem
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method='highs')

# Output the result
if result.success:
    print(f"Optimal production schedule found with total profit: ${-result.fun:.2f}")
    print("Decision variables (number of units produced for each product):")
    print(f"Product 1: {result.x[0]:.2f} units")
    print(f"Product 2: {result.x[1]:.2f} units")
    print(f"Product 3: {result.x[2]:.2f} units")
else:
    print("Optimization failed.")
