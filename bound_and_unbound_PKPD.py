import matplotlib.pyplot as plt
import numpy as np

# Simulate a plasma concentration-time curve (absorption + elimination)
time = np.linspace(0, 24, 300)
ka = 1.2
ke = 0.3
dose = 100
Vd = 1
Cp = dose * ka / (Vd * (ka - ke)) * (np.exp(-ke * time) - np.exp(-ka * time))

# Adjust fraction unbound to make free plasma concentration lower
fu_p = 0.4  # smaller unbound fraction
Cp_u = Cp * fu_p

# Compute Cmax and Tmax
Cmax_idx = np.argmax(Cp)
Tmax = time[Cmax_idx]
Cmax = Cp[Cmax_idx]
Cmax_u = Cp_u[Cmax_idx]

# Simulated EC90-related thresholds
EC90 = 10
fu_assay = 0.5
Cp_thresh = (EC90 * fu_assay) / fu_p
Cp_u_thresh = EC90 * fu_assay

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True)
fig.subplots_adjust(wspace=0.4)

# --- Total concentration plot ---
ax1 = axes[0]
ax1.plot(time, Cp, color='darkorange', linewidth=3)
ax1.plot(Tmax, Cmax, 'o', color='black', markerfacecolor='darkorange')
ax1.annotate(r"$C_p(t_{max}) = C_{max}$", xy=(Tmax, Cmax), xytext=(Tmax+5, Cmax+5),
             arrowprops=dict(arrowstyle='->'), fontsize=12)

# Threshold line
ax1.axhline(Cp_thresh, color='darkorange', linestyle=':', linewidth=2)
ax1.text(12, Cp_thresh+1, r"$C_p = (EC_{90} \cdot f_{u,assay}) / f_{u,p}$", fontsize=12)

ax1.set_xlabel("Time", fontsize=12)
ax1.set_ylabel(r"Plasma Concentration $C_p$", fontsize=12)
ax1.set_title("(a) Working With Total Concentrations", style='italic', fontsize=13)
ax1.set_xlim(0, 24)
ax1.set_ylim(0, max(Cp)*1.2)
ax1.set_xticks([])
ax1.set_yticks([])

# --- Free concentration plot ---
ax2 = axes[1]
ax2.plot(time, Cp_u, color='lightskyblue', linewidth=3)
ax2.plot(Tmax, Cmax_u, 'o', color='black', markerfacecolor='lightskyblue')
ax2.annotate(r"$C_{p,u}(t_{max}) = C_p(t_{max}) \cdot f_{u,p} = C_{max,u}$",
             xy=(Tmax, Cmax_u), xytext=(Tmax+4, Cmax_u+4),
             arrowprops=dict(arrowstyle='->'), fontsize=12)

# Threshold line
ax2.axhline(Cp_u_thresh, color='lightskyblue', linestyle=':', linewidth=2)
ax2.text(12, Cp_u_thresh+0.8, r"$C_{p,u} = EC_{90} \cdot f_{u,assay}$", fontsize=12)

ax2.set_xlabel("Time", fontsize=12)
ax2.set_ylabel(r"Free Plasma Concentration $C_{p,u}$", fontsize=12)
ax2.set_title("(b) Working With Unbound Concentrations", style='italic', fontsize=13)
ax2.set_xlim(0, 24)
ax2.set_ylim(0, max(Cp)*1.2)
ax2.set_xticks([])
ax2.set_yticks([])

plt.show()
