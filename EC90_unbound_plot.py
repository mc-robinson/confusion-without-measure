import matplotlib.pyplot as plt
import numpy as np

# Simulated sigmoidal curve data
x = np.linspace(0.0001, 1000, 100000)
ec50 = 0.3
ec90 = 1.29
hill_coefficient = 1.5
fu_assay = 0.1

# Response calculation (Hill equation)
response = 100 * (x ** hill_coefficient) / (ec50 ** hill_coefficient + x ** hill_coefficient)
free_x = fu_assay * x

# Plot
fig, axes = plt.subplots(1, 1, figsize=(8,6))
ax = axes
ax.plot(x, response, color='black', linewidth=2)
ax.plot(free_x, response, color='blue', linewidth=2)

# EC90 lines
ax.axhline(90, linestyle=':', color='gray')
ax.axvline(ec90, linestyle=':', color='gray')
ax.axvline(ec90 * fu_assay, linestyle=':', color='blue')

# EC90 dots
ax.plot(ec90, 90, 'o', color='black', label='EC90 point')
ax.plot(ec90 * fu_assay, 90, 'o', color='blue', label='EC90,u point')

# Arrow from EC90 to EC90,u
ax.annotate(
    '', 
    xy=(ec90 * fu_assay, 90), 
    xytext=(ec90-0.1, 90),
    arrowprops=dict(arrowstyle='->', color='gray', lw=4)
)

# Annotations
ax.text(ec90 + 0.6, 15, 'EC$_{90}$', ha='center', va='bottom', fontsize=12)
ax.text(ec90 * fu_assay + 0.57, 1, 'EC$_{90,u} = EC_{90} \cdot f_{u,assay}$', ha='center', va='bottom', fontsize=12, color='blue')
ax.text(0.01, 92, '90%', va='center', ha='left', fontsize=10)
ax.set_xlabel('concentration', fontsize=12, style='italic')
ax.set_ylabel('in vitro response', fontsize=12, style='italic')
ax.set_title("From Total to Free Potency", style='italic', fontsize=14)

# Scaling
ax.set_xscale('log')
ax.set_xlim(0.001, 100)
ax.set_xticks([])
ax.set_yticks([])

plt.show()
