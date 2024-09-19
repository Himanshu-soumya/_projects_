import random
import pandas as pd

# Function to generate random data
def generate_random_data(num_samples=70):
    data = []
    for _ in range(num_samples):
        temperature = round(random.uniform(10, 40), 2)
        soil_moisture = round(random.uniform(30, 90), 2)
        data.append((temperature, soil_moisture))
    return data

if __name__ == "__main__":
    # Generate random data
    dataset = generate_random_data()

    # Convert data to DataFrame
    df = pd.DataFrame(dataset, columns=["temperature", "soil_moisture"])

    # Save to CSV file
    df.to_csv("data.csv", index=False)
    print("CSV file 'data.csv' saved successfully.")
