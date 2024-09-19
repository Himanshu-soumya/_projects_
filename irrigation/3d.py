import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
days = 70
moisture_range = (20, 90)
initial_state = 'normal'
irrigation_actions = ['normal_speed_irrigation', 'fast_speed_irrigation', 'slow_speed_irrigation', 'no_irrigation']

# Initialize Agent
class IrrigationAgent:
    def __init__(self, moisture_trigger_low=60, moisture_trigger_high=80):
        self.moisture_trigger_low = moisture_trigger_low
        self.moisture_trigger_high = moisture_trigger_high
        self.actions = ['normal_speed_irrigation', 'fast_speed_irrigation', 'slow_speed_irrigation', 'no_irrigation']
        self.q_table = np.zeros((2, len(self.actions)))  # States: [normal, high_moisture], Actions: [normal_speed_irrigation, fast_speed_irrigation, slow_speed_irrigation, no_irrigation]
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_prob = 0.1

    def choose_action(self, state):
        if np.random.rand() < self.exploration_prob:
            return np.random.choice(len(self.actions))
        else:
            return np.argmax(self.q_table[state, :])

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state, :])
        self.q_table[state, action] += self.learning_rate * (
            reward + self.discount_factor * self.q_table[next_state, best_next_action] - self.q_table[state, action]
        )
        
def simulate_irrigation(agent, soil_moisture):
    state = 0  # Assume starting in the 'normal' state
    if soil_moisture <= 50:
        action = 1  # Fast speed irrigation
    elif 70 < soil_moisture <= 80:
        action = 2  # Slow speed irrigation
    elif 50 < soil_moisture < 70:
        action = 0  # Normal speed irrigation
    elif soil_moisture > agent.moisture_trigger_high:
        action = 3  # No irrigation
    else:
        action = agent.choose_action(state)  # Use learned policy
    return action
# Create an instance of the agent
agent = IrrigationAgent()

# Arrays to store results
soil_moisture_history = []
irrigation_history = []
plant_growth_history = []

# Simulate 3D model for 70 days
for day in range(1, days + 1):
    # Simulate random soil moisture for each day
    soil_moisture = np.random.uniform(*moisture_range)
    
    # Choose irrigation action using the agent
    irrigation_action = simulate_irrigation(agent, soil_moisture)
    
    # Update agent based on the chosen action and reward
    reward = 1 if irrigation_action != 3 else 0
    next_state = 1 if soil_moisture > agent.moisture_trigger_high else 0
    agent.update_q_table(0, irrigation_action, reward, next_state)
    
    # Store results
    soil_moisture_history.append(soil_moisture)
    irrigation_history.append(irrigation_action)
    plant_growth_history.append(day / days)  # Plant growth as a percentage of days

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for Soil Moisture and Irrigation Actions
ax.scatter(range(1, days + 1), soil_moisture_history, plant_growth_history, c=irrigation_history, cmap='viridis', s=50)

# Colorbar legend
cbar = plt.colorbar(ax.scatter([], [], [], c=[], cmap='viridis', s=50), ax=ax)
cbar.set_label('Irrigation Actions')

# Set labels
ax.set_xlabel('Days')
ax.set_ylabel('Soil Moisture')
ax.set_zlabel('Plant Growth')

plt.title('3D Model of Tomato Farming')
plt.show()
