import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_capital = 10000
win_rate = 0.60
average_win = 250
average_loss = 200
num_trades = 1000
num_simulations = 10000

# Function to run a single simulation for final capital
def run_simulation_final():
    capital = initial_capital
    for _ in range(num_trades):
        if np.random.rand() < win_rate:
            capital += average_win
        else:
            capital -= average_loss
    return capital

# Function to run a single simulation for capital progression
def run_simulation_progression():
    capital = initial_capital
    capital_progression = [capital]
    for _ in range(num_trades):
        if np.random.rand() < win_rate:
            capital += average_win
        else:
            capital -= average_loss
        capital_progression.append(capital)
    return capital_progression

# Running multiple simulations for final capital
final_capitals = [run_simulation_final() for _ in range(num_simulations)]

# Running multiple simulations for capital progression
num_paths = 100
all_simulations = [run_simulation_progression() for _ in range(num_paths)]

# Plotting the histogram of final capital
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.hist(final_capitals, bins=50, edgecolor='black', alpha=0.7)
plt.title('Distribution of Final Capital After 1000 Trades')
plt.xlabel('Final Capital ($)')
plt.ylabel('Frequency')

mean_final_capital = np.mean(final_capitals)
median_final_capital = np.median(final_capitals)
percentile_5 = np.percentile(final_capitals, 5)
percentile_95 = np.percentile(final_capitals, 95)

plt.axvline(mean_final_capital, color='blue', linestyle='dashed', linewidth=1, label=f'Mean: ${mean_final_capital:.2f}')
plt.axvline(median_final_capital, color='green', linestyle='dashed', linewidth=1, label=f'Median: ${median_final_capital:.2f}')
plt.axvline(percentile_5, color='red', linestyle='dashed', linewidth=1, label=f'5th Percentile: ${percentile_5:.2f}')
plt.axvline(percentile_95, color='purple', linestyle='dashed', linewidth=1, label=f'95th Percentile: ${percentile_95:.2f}')

plt.legend()
plt.grid(True)

# Plotting the capital progression over time
plt.subplot(1, 2, 2)
for simulation in all_simulations:
    plt.plot(simulation, linewidth=0.7, alpha=0.7)

plt.title('Monte Carlo Simulation of Trading Outcomes')
plt.xlabel('Number of Trades')
plt.ylabel('Total P&L ($)')
plt.axhline(initial_capital, color='green', linestyle='solid', linewidth=1, label='Initial Capital')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Detailed summary statistics
print(f"Mean final capital: ${mean_final_capital:.2f}")
print(f"Median final capital: ${median_final_capital:.2f}")
print(f"5th percentile final capital: ${percentile_5:.2f}")
print(f"95th percentile final capital: ${percentile_95:.2f}")
print(f"Standard deviation of final capital: ${np.std(final_capitals):.2f}")
print(f"Minimum final capital: ${np.min(final_capitals):.2f}")
print(f"Maximum final capital: ${np.max(final_capitals):.2f}")
