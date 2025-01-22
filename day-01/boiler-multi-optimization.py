from scipy.optimize import differential_evolution

# Objective function: Minimize coal usage
def objective(x):
    coal_input = x[0]
    air_supply = 5 * coal_input  # Air supply is 5 times the coal input
    energy_produced = 8000 * coal_input
    steam_required = 10000  # Energy required to generate 10,000 kg/hr of steam
    
    # Constraints: Energy must meet the steam requirement
    energy_constraint = energy_produced - steam_required
    
    # Flue gas constraint: 2.5 * coal input should be within allowable limits (e.g., 5000 kg/hr)
    flue_gas_constraint = 2.5 * coal_input - 5000
    
    # Penalty for violating constraints (penalizing high energy or flue gases)
    penalty = max(0, energy_constraint) + max(0, flue_gas_constraint)
    
    # Return coal usage plus penalty for constraint violations
    return coal_input + penalty

# Boundaries for the decision variables (coal and air supply)
bounds = [(0, None)]  # Coal input must be non-negative
# Air supply is implicitly controlled via coal input, so no separate boundary needed

# Solve using differential evolution
result = differential_evolution(objective, bounds)

# Output results
if result.success:
    coal_input = result.x[0]
    air_supply = 5 * coal_input  # Air is 5 times coal input
    print(f"Optimal coal input (via global optimization): {coal_input:.2f} kg/hr")
    print(f"Optimal air supply (via global optimization): {air_supply:.2f} kg/hr")
else:
    print("Global optimization did not succeed.")
