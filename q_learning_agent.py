import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle

# Update the QLearningAgent class
class QLearningAgent:
    def __init__(self, state_dim, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.state_dim = state_dim
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.num_actions)
        else:
            state_index = int(state[0]) if state is not None else 0  # Convert state to integer index
            return np.argmax(self.q_table[state_index, :])

    def update_q_table(self, state, action, reward, next_state):
        if next_state is not None:
            state_index = int(state[0]) if state is not None else 0  # Convert state to integer index
            best_next_action = np.argmax(self.q_table[int(next_state[0]), :])
            self.q_table[state_index, action] += self.learning_rate * (
                reward + self.discount_factor * self.q_table[int(next_state[0]), best_next_action] - self.q_table[state_index, action]
            )

