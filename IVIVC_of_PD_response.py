import matplotlib.pyplot as plt
import numpy as np

# Simulated sigmoidal curve data
x = np.linspace(0.001, 10, 1000)
ec50 = 0.3
ec90 = 1.29
hill_coefficient = 1.5

# Response calculation (Hill equation)
response = 100 * (x ** hill_coefficient) / (ec50 ** hill_coefficient + x ** hill_coefficient)

# Regenerate plot with proper placement of the annotation arrow and text using figure coordinates
fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True, gridspec_kw={'wspace': 0.4})

# --- Left panel: in vitro ---
ax = axes[0]
ax.plot(x, response, color='black', linewidth=2)
ax.axhline(50, linestyle=':', color='gray')
ax.axhline(90, linestyle=':', color='gray')
ax.axvline(ec50, linestyle=':', color='gray')
ax.axvline(ec90, linestyle=':', color='gray')
ax.text(ec50, 5, 'EC$_{50}$', ha='center', va='bottom', fontsize=12)
ax.text(ec90, 5, 'EC$_{90}$', ha='center', va='bottom', fontsize=12)
ax.text(0.1, 50, '50%', va='center', ha='left', fontsize=10)
ax.text(0.1, 90, '90%', va='center', ha='left', fontsize=10)
ax.set_xlabel('in vitro free concentration', fontsize=12, style='italic')
ax.set_ylabel('in vitro response', fontsize=12, style='italic')

ax.set_xscale('log')
ax.set_xticks([])
ax.set_yticks([])

# --- Right panel: in vivo ---
ax2 = axes[1]
ax2.plot(x, response, color='steelblue', linewidth=2)
ax2.text(7, 70, 'PD', fontsize=16, color='steelblue')
ax2.set_xlabel('in vivo free concentration', fontsize=12, style='italic')
ax2.set_ylabel('in vivo response', fontsize=12, style='italic')
ax2.set_xticks([])
ax2.set_yticks([])

ax2.set_xscale('log')
ax2.set_xticks([])
ax2.set_yticks([])

# --- Assumption arrow between plots using figure coordinates ---
fig.text(0.50, 0.55, 'Assumption', ha='center', va='center', fontsize=12, fontweight='bold')
fig.axes[0].annotate('', xy=(0.45, 0.55), xytext=(0.34, 0.55),
                    xycoords='figure fraction', textcoords='figure fraction',
                    arrowprops=dict(arrowstyle='->', lw=3, color='black'))

# Style both plots
for ax in axes:
    ax.set_xlim(1e-2, 10)
    ax.set_ylim(0, 110)
    ax.spines[['top', 'right']].set_visible(False)

plt.show()
