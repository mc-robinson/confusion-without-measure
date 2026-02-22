import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# --- Parameters ---
ka = 0.4  # absorption rate constant
ke = 0.2  # elimination rate constant
dose = 5
Vd = 1
ec50 = 0.3  # less potent PD
hill_coef = 1.5

# --- PK and PKPD Time Series ---
time = np.linspace(0, 24, 300)
pk_conc_abs = dose * ka / (Vd * (ka - ke)) * (np.exp(-ke * time) - np.exp(-ka * time))
pkpd_response = 1 * (pk_conc_abs ** hill_coef) / (ec50 ** hill_coef + pk_conc_abs ** hill_coef)

# --- PD Concentration-Response ---
conc = np.logspace(-3, 10, 1000)
pd_response = 100 * (conc ** hill_coef) / (ec50 ** hill_coef + conc ** hill_coef)

# --- Create Figure ---
fig = plt.figure(figsize=(10, 8))

# Text panel (top-left)
text_ax = fig.add_axes([0.05, 0.55, 0.35, 0.35])
text_ax.axis('off')
text_ax.text(0, 1.05, "Simplified Picture", fontsize=12, weight='bold', style='italic')
text_ax.text(0.05, 0.8, "PK: What the body does to the drug\nconcentration over time", fontsize=10, style='italic')
text_ax.text(0.05, 0.5, "PD: What the compound does to the body at\na given concentration", fontsize=10, style='italic')
text_ax.text(0.05, 0.2, "PK/PD: What the compound does to the\nbody over time", fontsize=10, style='italic')
text_ax.set_xlim(0, 1)
text_ax.set_ylim(0, 1)
text_ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], linestyle='dotted', color='gray')

# PK plot (top-right)
pk_ax = fig.add_axes([0.65, 0.65, 0.25, 0.25])
pk_ax.plot(time, pk_conc_abs, color='orange', linewidth=2)
pk_ax.set_xticks([])
pk_ax.set_yticks([])
pk_ax.set_xlabel("Time", fontsize=12)
pk_ax.set_ylabel("Concentration", fontsize=12)
pk_ax.text(18, max(pk_conc_abs)*0.8, "PK", fontsize=14, color='orange')

# PD plot (bottom-left)
pd_ax = fig.add_axes([0.05, 0.1, 0.25, 0.25])
pd_ax.plot(conc, pd_response, color='steelblue', linewidth=2)
pd_ax.set_xlim(1e-3, 100)
pd_ax.set_ylim(0, 101)
pd_ax.set_xscale('log')
pd_ax.set_xticks([])
pd_ax.set_yticks([])
pd_ax.set_xlabel("Concentration", fontsize=12)
pd_ax.set_ylabel("Response", fontsize=12)
pd_ax.text(20, 30, "PD", fontsize=14, color='steelblue')

# PKPD plot (bottom-right)
pkpd_ax = fig.add_axes([0.65, 0.1, 0.25, 0.25])
pkpd_ax.plot(time, pkpd_response, color='darkgreen', linewidth=2)
pkpd_ax.set_xticks([])
pkpd_ax.set_yticks([])
pkpd_ax.set_xlabel("Time", fontsize=12)
pkpd_ax.set_ylabel("Response", fontsize=12)
pkpd_ax.text(18, max(pkpd_response)*0.8, "PK/PD", fontsize=14, color='darkgreen')

# Arrows connecting panels
fig.patches.extend([
    FancyArrowPatch((0.32, 0.22), (0.63, 0.22), transform=fig.transFigure,
                    arrowstyle='->', mutation_scale=20, color='gray', lw=2),
    FancyArrowPatch((0.77, 0.62), (0.77, 0.36), transform=fig.transFigure,
                    arrowstyle='->', mutation_scale=20, color='gray', lw=2)
])

plt.show()
