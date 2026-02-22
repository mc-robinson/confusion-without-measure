from scipy.stats import linregress
import matplotlib.pyplot as plt
import numpy as np

# Example data points based on the image
time_min = np.array([0, 5, 15, 30])
compound1 = np.array([100, 95, 89, 83])
compound1_err = np.array([0, 5, 6, 5])  # Approximate errors
compound2 = np.array([100, 70, 32, 15])
compound2_err = np.array([0, 6, 4, 3])  # Approximate errors

# Convert % remaining to natural log for linear regression
log_compound1 = np.log(compound1[compound1 > 0])
log_compound2 = np.log(compound2[compound2 > 0])
time1 = time_min[:len(log_compound1)]
time2 = time_min[:len(log_compound2)]

# Perform linear regression on log-transformed data
slope1, intercept1, _, _, _ = linregress(time1, log_compound1)
slope2, intercept2, _, _, _ = linregress(time2, log_compound2)

# Calculate half-life: t1/2 = ln(2) / |slope|
half_life1 = np.log(2) / abs(slope1)
half_life2 = np.log(2) / abs(slope2)

# Re-plot with calculated half-lives in legend
plt.figure(figsize=(8, 5))
plt.errorbar(time_min, compound1, yerr=compound1_err,
             fmt='-o', color='blue', capsize=4, markersize=6,
             label=f'compound-1 ($t_{{1/2}}$ = {half_life1:.1f} min)')
plt.errorbar(time_min, compound2, yerr=compound2_err,
             fmt='-^', color='orange', capsize=4, markersize=6,
             label=f'compound-2 ($t_{{1/2}}$ = {half_life2:.1f} min)')

# Labels and formatting
plt.xlabel("Incubation time (min)", fontsize=12)
plt.ylabel("Percent Compound Remaining (%)", fontsize=12)
plt.title("")  # No title
plt.xlim(-1, 32)
plt.ylim(0, 110)
plt.grid(False)
plt.legend()
plt.tight_layout()
plt.show()
