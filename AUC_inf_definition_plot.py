import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz
from numpy.polynomial.polynomial import polyfit

# === Data ===
time_hr = np.array([0, 0.033, 0.083, 0.25, 0.5, 1, 2, 4])
concentration_ng_ml = np.array([1744.207, 1208.552, 733.448, 440.151, 243.913, 66.238, 12.696, 2.217])
error = np.array([160, 100, 80, 60, 30, 5, 2, 0.5])

# === AUC Calculation ===

# AUC from 0 to last measured point
auc_0_t = trapz(concentration_ng_ml, time_hr)

# Terminal phase log-linear regression using last 3 points
log_conc = np.log(concentration_ng_ml[-2:])
time_terminal = time_hr[-2:]
slope, intercept = np.polyfit(time_terminal, log_conc, 1)
lambda_z = -slope  # terminal elimination rate constant

# Extrapolated AUC: Clast / lambda_z
C_last = concentration_ng_ml[-1]
auc_extrap = C_last / lambda_z

# Total AUC (AUCinf)
auc_inf = auc_0_t + auc_extrap

# === Plotting ===

# Generate exponential decay line
fit_time = np.linspace(time_hr[-2], 10, 100)
fit_conc = np.exp(intercept + slope * fit_time)

plt.figure(figsize=(10, 6))
plt.errorbar(time_hr, concentration_ng_ml, yerr=error, fmt='-o', color='black', label='Observed Data')

# Fill AUC_0_t (observed)
plt.fill_between(time_hr, concentration_ng_ml, color='lightsteelblue', alpha=0.7, label='AUC_last (oberved)')

# Plot terminal exponential fit
plt.plot(fit_time[-75:], fit_conc[-75:], 'r--', label='Exponential Fit (Terminal Phase)')

# Fill AUC extrapolated
plt.fill_between(fit_time[-75:], fit_conc[-75:], color='red', alpha=0.4, label='AUC_extrapolated')

# Annotations
plt.annotate(r'$AUC_{last}$', xy=(1.5, 3), fontsize=14, color='black')
plt.annotate(r'$AUC_{t_{last}-t_{inf}}$', xy=(5, 0.25), fontsize=14, color='black')

plt.annotate(r'$AUC_{inf} = AUC_{last} + AUC_{t_{last}-t_{inf}}$', xy=(4.2, 11), fontsize=14, color='black')
plt.annotate(r'$where \,\,\, AUC_{inf} = AUC_{0-t_{inf}}, \,\, AUC_{last} = AUC_{0-t_{last}}$', xy=(4.2, 4), fontsize=14, color='black')


# Plot formatting
plt.yscale('log')
plt.xlabel("Time (h)", fontsize=12, fontweight='bold')
plt.ylabel("Plasma Concentration (ng/mL)", fontsize=12, fontweight='bold')
plt.title("Plasma Concentration vs. Time with Extrapolated AUC", fontsize=14)
plt.xlim(0, 10)
plt.ylim(0.1, 10000)
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
