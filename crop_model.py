import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle

from q_learning_agent import QLearningAgent

# Load the data
crop = pd.read_csv('Data/crop_recommendation.csv')

# Define state features (you may need to adjust this based on your data)
state_features = crop.columns[:-1]

# Split the data into training and testing sets
X = crop[state_features].values
Y = crop.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=42)
# Standardize the state features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Update the CropRecommendationEnvironment class
class CropRecommendationEnvironment:
    def __init__(self, X, y):
        self.states = X
        self.actions = np.unique(y)
        self.state_dim = X.shape[1]
        self.num_actions = len(self.actions)
        self.current_state = None
        self.current_action = None
        self.current_step = 0
        self.y_true = y  # Store the true labels

    def reset(self):
        self.current_step = 0
        self.current_state = self.states[self.current_step]
        self.current_action = None
        return self.current_state

    def step(self, action):
        self.current_action = action
        reward = self.calculate_reward()
        self.current_step += 1
        if self.current_step < len(self.states):
            self.current_state = self.states[self.current_step]
        else:
            self.current_state = None
        done = (self.current_step == len(self.states))
        return self.current_state, reward, done, {}

    def calculate_reward(self):
        # For simplicity, use accuracy as a reward
        y_pred_label = self.actions[self.current_action]  # Convert action to crop label
        y_pred = np.repeat([y_pred_label], self.current_step + 1, axis=0)
        accuracy = accuracy_score(self.y_true[: self.current_step + 1], y_pred)
        reward = accuracy
        return reward


# Discretize the state space
a = 2200
num_states = a  # You may need to adjust this based on your problem
state_discretizer = KBinsDiscretizer(n_bins=num_states, encode='ordinal', strategy='uniform')
X_train_discrete = state_discretizer.fit_transform(X_train)
X_test_discrete = state_discretizer.transform(X_test)
# Train the Q-learning agent
print("data training started______")
num_episodes = a
env = CropRecommendationEnvironment(X_test_discrete, y_test)
agent = QLearningAgent(state_dim=num_states, num_actions=len(np.unique(Y)))
for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0
    while state is not None:
        action = agent.choose_action(state)
        next_state, reward, done, _ = env.step(action)
        agent.update_q_table(state, action, reward, next_state)
        state = next_state
        total_reward += reward

    if (episode + 1) % 500 == 0:
        print(f"Episode {episode + 1}/{num_episodes}, Total Average Reward: {total_reward}")

# Save the trained Q-learning model
filepklname = 'crop_recommendation.pkl'
pklmodleel = open(filepklname, 'wb')
pickle.dump(agent, pklmodleel)
pklmodleel.close()


