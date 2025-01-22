from scipy.optimize import linprog

# Coefficients for the objective function (minimize coal usage)
# Minimize coal input x1 (coefficient for x1 is 1)
c = [1]

# Coefficients for the constraints
# 1. Energy constraint: coal produces 8000 kcal/kg and needs to produce 10,000 kg/hr of steam
# 2. Air supply: 5 kg of air per kg of coal
# 3. Flue gases constraint: Maximum permissible flue gases (this can be defined)

# Coefficients for the linear constraints
A = [
    [-8000, 0],   # Energy balance: 8000 * x1 (coal energy) >= 10000 (steam output)
    [5, -1],      # Air supply: x2 = 5 * x1
    [2.5, 0]      # Flue gas constraint: 2.5 * x1 <= max flue gases
]

# Right-hand side values for the constraints
b = [
    -10000,  # Energy produced by coal must satisfy the steam output requirement
    0,       # This will imply x2 = 5 * x1, no explicit constraint in this form
    5000     # Maximum permissible flue gases
]

# Bounds for each variable
# Coal (x1) >= 0, Air (x2) >= 0
bounds = [(0, None), (0, None)]

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Output results
if result.success:
    coal_input = result.x[0]
    air_supply = 5 * coal_input  # air is 5 times coal input
    print(f"Optimal coal input: {coal_input:.2f} kg/hr")
    print(f"Optimal air supply: {air_supply:.2f} kg/hr")
else:
    print("Optimization did not succeed.")
