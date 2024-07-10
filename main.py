import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_capital = 10000
win_rate = 0.60
average_win = 250
average_loss = 200
num_trades = 1000
num_simulations = 10000

# Function to run a single simulation
def run_simulation():
    capital = initial_capital
    for _ in range(num_trades):
        if np.random.rand() < win_rate:
            capital += average_win
        else:
            capital -= average_loss
    return capital

# Running multiple simulations
final_capitals = [run_simulation() for _ in range(num_simulations)]

# Plotting the results
plt.hist(final_capitals, bins=50, edgecolor='black')
plt.title('Monte Carlo Simulation of Trading Outcomes')
plt.xlabel('Final Capital')
plt.ylabel('Frequency')
plt.axvline(initial_capital, color='red', linestyle='dashed', linewidth=1)
plt.show()

# Summary statistics
mean_final_capital = np.mean(final_capitals)
median_final_capital = np.median(final_capitals)
percentile_5 = np.percentile(final_capitals, 5)
percentile_95 = np.percentile(final_capitals, 95)

print(f"Mean final capital: ${mean_final_capital:.2f}")
print(f"Median final capital: ${median_final_capital:.2f}")
print(f"5th percentile final capital: ${percentile_5:.2f}")
print(f"95th percentile final capital: ${percentile_95:.2f}")
