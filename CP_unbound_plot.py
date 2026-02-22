import matplotlib.pyplot as plt
import numpy as np

# Simulate plasma concentration-time curve
time = np.linspace(0, 24, 300)
ka = 1.2
ke = 0.3
dose = 100
Vd = 1
Cp = dose * ka / (Vd * (ka - ke)) * (np.exp(-ke * time) - np.exp(-ka * time))

# Free concentration via fu_p
fu_p = 0.4
Cp_u = Cp * fu_p

# Cmax and Tmax
Cmax_idx = np.argmax(Cp)
Tmax = time[Cmax_idx]
Cmax = Cp[Cmax_idx]
Cmax_u = Cp_u[Cmax_idx]

# EC90-related thresholds
EC90 = 10
fu_assay = 0.5
Cp_thresh = (EC90 * fu_assay) / fu_p
Cp_u_thresh = EC90 * fu_assay

# Single plot showing transition from total to unbound
fig, ax = plt.subplots(figsize=(8,6))

# Plot curves
ax.plot(time, Cp, color='darkorange', linewidth=3, label='Total plasma concentration $C_p$')
ax.plot(time, Cp_u, color='lightskyblue', linewidth=3, label='Unbound plasma concentration $C_{p,u}$')

# Plot Cmax dots
ax.plot(Tmax, Cmax, 'o', color='black', markerfacecolor='darkorange') # , label=r"$C_{max}$")
ax.plot(Tmax, Cmax_u, 'o', color='black', markerfacecolor='lightskyblue') # , label=r"$C_{max,u}$")

# Arrow from total to unbound Cmax
ax.annotate(
    '', 
    xy=(Tmax, Cmax_u), 
    xytext=(Tmax, Cmax),
    arrowprops=dict(arrowstyle='->', color='gray', lw=3)
)

# Annotate Cmax
ax.annotate(
    r"$C_{max}$", 
    xy=(Tmax, Cmax), 
    xytext=(Tmax + 2, Cmax + 5),
    textcoords='data',
    fontsize=12,
    arrowprops=dict(arrowstyle='->', color='darkorange')
)

# Annotate Cmax,u with derivation
ax.annotate(
    r"$C_{max,u} = C_{max} \cdot f_{u,p}$", 
    xy=(Tmax, Cmax_u), 
    xytext=(Tmax + 5, Cmax_u + 7),
    textcoords='data',
    fontsize=12,
    arrowprops=dict(arrowstyle='->', color='lightskyblue')
)

# Threshold lines and labels
# ax.axhline(Cp_thresh, color='darkorange', linestyle=':', linewidth=2)
# ax.text(13, Cp_thresh+1, r"$C_p = \frac{EC_{90} \cdot f_{u,assay}}{f_{u,p}}$", fontsize=12, color='darkorange')

# ax.axhline(Cp_u_thresh, color='lightskyblue', linestyle=':', linewidth=2)
# ax.text(13, Cp_u_thresh+0.8, r"$C_{p,u} = EC_{90} \cdot f_{u,assay}$", fontsize=12, color='lightskyblue')

# Styling
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("Concentration", fontsize=12)
ax.set_title("From Total to Free Plasma Concentration", style='italic', fontsize=14)
ax.set_xlim(0, 24)
ax.set_ylim(0, max(Cp)*1.2)
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc='upper right')

plt.show()
