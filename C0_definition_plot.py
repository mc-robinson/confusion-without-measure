import matplotlib.pyplot as plt
import numpy as np

# Example data approximating the image
time_hr = np.array([0, 0.033, 0.083, 0.25, 0.5, 1, 2, 4])
concentration_ng_ml = np.array([1716, 1208.552, 733.448, 440.151, 243.913, 66.238, 12.696, 2.217])
error = np.array([84, 100, 80, 60, 30, 5, 2, 0.5])  # Example error bars

# Create the plot
plt.figure(figsize=(10, 6))
plt.errorbar(time_hr[0:2], concentration_ng_ml[0:2], yerr=error[0:2], fmt='--o', color='red', label='Extrapolation')
plt.errorbar(time_hr[1:], concentration_ng_ml[1:], yerr=error[1:], fmt='-o', color='black', label='IV at 1 mg/kg')

# Annotate C₀
plt.annotate(r'$C_0$', xy=(time_hr[0]+0.02, concentration_ng_ml[0]), xytext=(0.1, 3000),
             arrowprops=dict(facecolor='red',width=0.8, headwidth=8, shrink=0.05), fontsize=14)

# Log scale for y-axis
plt.yscale('log')

# Labeling
plt.xlabel("Time (h)", fontsize=12, fontweight='bold')
plt.ylabel("Plasma Concentration (ng/mL)", fontsize=12, fontweight='bold')
plt.title("Plasma Concentration vs. Time -- Calculating Cp(t=0)", fontsize=14)

# Axis limits and formatting
plt.xlim(0, 2.1)
plt.ylim(10, 10000)

# Add legend
plt.legend()

# Grid and layout
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.tight_layout()
plt.show()
