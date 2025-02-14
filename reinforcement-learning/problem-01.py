import numpy as np

class GridWorld:
    def __init__(self, size=3):
        self.size = size
        self.goal = (size - 1, size - 1)  # Goal at bottom-right
        self.state = (0, 0)  # Start at top-left

    def reset(self):
        """Reset the agent to the start position."""
        self.state = (0, 0)
        return self.state

    def step(self, action):
        """Move the agent based on the action."""
        x, y = self.state

        if action == 0 and y > 0:  # Move left
            y -= 1
        elif action == 1 and y < self.size - 1:  # Move right
            y += 1
        elif action == 2 and x > 0:  # Move up
            x -= 1
        elif action == 3 and x < self.size - 1:  # Move down
            x += 1

        self.state = (x, y)

        reward = 1 if self.state == self.goal else -0.1
        done = self.state == self.goal
        return self.state, reward, done

# Simulating the environment with random actions
env = GridWorld()
state = env.reset()
done = False

print("Starting Grid World Simulation...")

while not done:
    action = np.random.choice([0, 1, 2, 3])  # Randomly pick an action
    next_state, reward, done = env.step(action)
    print(f"Action: {action}, New State: {next_state}, Reward: {reward}")

print("Goal reached!")
