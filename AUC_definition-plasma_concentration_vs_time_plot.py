import matplotlib.pyplot as plt
import numpy as np

# Example data approximating the image
time_hr = np.array([0, 0.033, 0.083, 0.25, 0.5, 1, 2, 4,8])
concentration_ng_ml = np.array([1744.207, 1208.552, 733.448, 440.151, 243.913, 66.238, 12.696, 2.217, 0.1])
error = np.array([160, 100, 80, 60, 30, 5, 2, 0.5, 0.01])  # Example error bars

# Create the plot
plt.figure(figsize=(10, 6))
plt.errorbar(time_hr, concentration_ng_ml, yerr=error, fmt='-o', color='black', label='IV at 1 mg/kg')

# Log scale for y-axis
plt.yscale('log')

# Labeling
plt.xlabel("Time (h)", fontsize=12, fontweight='bold')
plt.ylabel("Concentration (ng/mL)", fontsize=12, fontweight='bold')
plt.title("Concentration vs. Time", fontsize=14)

# Fill the area under the curve (AUC) up to the last measured point before extrapolation
plt.fill_between(time_hr, concentration_ng_ml, color='lightsteelblue', alpha=0.7)

# annotate with AUC text
plt.annotate(r'$AUC$', xy=(1.75, 3), xytext=(1.75, 3),
             fontsize=18, color='black')

# Axis limits and formatting
plt.xlim(0, 10)
plt.ylim(0.1, 10000)

# Add legend
plt.legend()

# Grid and layout
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.tight_layout()
plt.show()
