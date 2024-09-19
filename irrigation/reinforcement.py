import numpy as np

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

# Example Usage:
agent = IrrigationAgent()

# Train the agent with some random data
for _ in range(100000):
    soil_moisture = np.random.uniform(20, 90)  # Simulate random soil moisture
    action = simulate_irrigation(agent, soil_moisture)
    reward = 1 if action != 3 else 0  # Reward for irrigation, no reward for no irrigation
    next_state = 1 if soil_moisture > agent.moisture_trigger_high else 0
    agent.update_q_table(0, action, reward, next_state)

# Test the agent with specific conditions
for moisture in range(20, 100):
    test_action = simulate_irrigation(agent, moisture)
    print(f"Soil Moisture: {moisture}, Action: {agent.actions[test_action]}")
