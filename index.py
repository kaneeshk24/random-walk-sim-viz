# the expected value is the theoretical mean(avg) of a random variable
# the average of the squared difference from the mean is variance (always +ve)
import numpy as np
import matplotlib.pyplot as plt


# defining parameters
n_jumps = 1000  # taking number of jumps
p_left = 0.4  # less than 1
p_right = 1 - p_left  # probab of moving right
starting_position = 0  # initial position


# simulate walk
positions = np.zeros(n_jumps + 1)  # array to store positions(Xn)
positions[0] = starting_position

for i in range(1, n_jumps + 1):
    # generate random number to determine direction
    direction = np.random.choice(['left', 'right'], p=[p_left, p_right])

    # Update position based on direction
    if direction == 'left':
        positions[i] = positions[i-1] - 1
    else:
        positions[i] = positions[i-1] + 1


# calculate stats
expected_position = np.mean(positions)
variance = np.var(positions)

print(f"Expected position after {n_jumps} jumps: {expected_position}")
print(f"Variance of positions after {n_jumps} jumps: {variance}")

plt.plot(range(n_jumps + 1), positions)
plt.xlabel("Number of jumps")
plt.ylabel("Particle position")
plt.title(f"Random walk simulation: n = {n_jumps}, p_left = {p_left}")
plt.show()
