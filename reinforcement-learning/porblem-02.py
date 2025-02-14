import numpy as np

class TaxiEnvironment:
    def __init__(self, size=5):
        self.size = size
        self.reset()

    def reset(self):
        """Initialize the taxi, passenger, and destination at random positions."""
        self.taxi_position = (np.random.randint(self.size), np.random.randint(self.size))
        self.passenger_position = (np.random.randint(self.size), np.random.randint(self.size))
        self.destination = (np.random.randint(self.size), np.random.randint(self.size))
        self.has_passenger = False
        return self.taxi_position, self.passenger_position, self.destination

    def step(self, action):
        """Move the taxi or perform pick-up/drop-off actions."""
        x, y = self.taxi_position

        # Move actions
        if action == 0 and y > 0:  # Move left
            y -= 1
        elif action == 1 and y < self.size - 1:  # Move right
            y += 1
        elif action == 2 and x > 0:  # Move up
            x -= 1
        elif action == 3 and x < self.size - 1:  # Move down
            x += 1
        elif action == 4:  # Pick up
            if self.taxi_position == self.passenger_position and not self.has_passenger:
                self.has_passenger = True
                reward = 0  # No penalty for correct pickup
            else:
                reward = -5  # Incorrect pickup attempt
            return (self.taxi_position, self.passenger_position, self.destination), reward, False
        elif action == 5:  # Drop off
            if self.taxi_position == self.destination and self.has_passenger:
                reward = 10  # Successfully dropped off
                done = True
            else:
                reward = -5  # Incorrect drop-off
                done = False
            return (self.taxi_position, self.passenger_position, self.destination), reward, done

        # Update taxi position
        self.taxi_position = (x, y)
        reward = -1  # Penalty for each move
        done = False
        return (self.taxi_position, self.passenger_position, self.destination), reward, done

# Simulating the environment with random actions
env = TaxiEnvironment()
state = env.reset()
done = False

print("Starting Taxi Simulation...")

while not done:
    action = np.random.choice([0, 1, 2, 3, 4, 5])  # Randomly choose an action
    next_state, reward, done = env.step(action)
    print(f"Action: {action}, New State: {next_state}, Reward: {reward}")
