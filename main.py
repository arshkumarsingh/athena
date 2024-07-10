import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Function to run a single simulation for final capital
def run_simulation_final(initial_capital, win_rate, average_win, average_loss, num_trades):
    capital = initial_capital
    for _ in range(num_trades):
        if np.random.rand() < win_rate:
            capital += average_win
        else:
            capital -= average_loss
    return capital

# Function to run a single simulation for capital progression
def run_simulation_progression(initial_capital, win_rate, average_win, average_loss, num_trades):
    capital = initial_capital
    capital_progression = [capital]
    for _ in range(num_trades):
        if np.random.rand() < win_rate:
            capital += average_win
        else:
            capital -= average_loss
        capital_progression.append(capital)
    return capital_progression

# Streamlit web app
st.title('Monte Carlo Simulation for Trading Outcomes')

# User inputs
initial_capital = st.number_input('Initial Capital ($)', value=10000)
win_rate = st.slider('Win Rate (%)', min_value=0, max_value=100, value=60) / 100
average_win = st.number_input('Average Win ($)', value=250)
average_loss = st.number_input('Average Loss ($)', value=200)
num_trades = st.number_input('Number of Trades', value=1000)
num_simulations = st.number_input('Number of Simulations', value=10000)
num_paths = st.number_input('Number of Paths to Plot', value=100)

# Running multiple simulations for final capital
final_capitals = [run_simulation_final(initial_capital, win_rate, average_win, average_loss, num_trades) for _ in range(num_simulations)]

# Running multiple simulations for capital progression
all_simulations = [run_simulation_progression(initial_capital, win_rate, average_win, average_loss, num_trades) for _ in range(num_paths)]

# Plotting the histogram of final capital
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

ax[0].hist(final_capitals, bins=50, edgecolor='black', alpha=0.7)
ax[0].set_title('Distribution of Final Capital After 1000 Trades')
ax[0].set_xlabel('Final Capital ($)')
ax[0].set_ylabel('Frequency')

mean_final_capital = np.mean(final_capitals)
median_final_capital = np.median(final_capitals)
percentile_5 = np.percentile(final_capitals, 5)
percentile_95 = np.percentile(final_capitals, 95)

ax[0].axvline(mean_final_capital, color='blue', linestyle='dashed', linewidth=1, label=f'Mean: ${mean_final_capital:.2f}')
ax[0].axvline(median_final_capital, color='green', linestyle='dashed', linewidth=1, label=f'Median: ${median_final_capital:.2f}')
ax[0].axvline(percentile_5, color='red', linestyle='dashed', linewidth=1, label=f'5th Percentile: ${percentile_5:.2f}')
ax[0].axvline(percentile_95, color='purple', linestyle='dashed', linewidth=1, label=f'95th Percentile: ${percentile_95:.2f}')
ax[0].legend()
ax[0].grid(True)

# Plotting the capital progression over time
for simulation in all_simulations:
    ax[1].plot(simulation, linewidth=0.7, alpha=0.7)

ax[1].set_title('Monte Carlo Simulation of Trading Outcomes')
ax[1].set_xlabel('Number of Trades')
ax[1].set_ylabel('Total P&L ($)')
ax[1].axhline(initial_capital, color='green', linestyle='solid', linewidth=1, label='Initial Capital')
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
st.pyplot(fig)

# Detailed summary statistics
st.write(f"Mean final capital: ${mean_final_capital:.2f}")
st.write(f"Median final capital: ${median_final_capital:.2f}")
st.write(f"5th percentile final capital: ${percentile_5:.2f}")
st.write(f"95th percentile final capital: ${percentile_95:.2f}")
st.write(f"Standard deviation of final capital: ${np.std(final_capitals):.2f}")
st.write(f"Minimum final capital: ${np.min(final_capitals):.2f}")
st.write(f"Maximum final capital: ${np.max(final_capitals):.2f}")
