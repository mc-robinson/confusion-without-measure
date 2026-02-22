import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create the figure and axis
fig, ax = plt.subplots(figsize=(3, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 6)
ax.axis('off')  # Hide axes

# Draw the tube outline using a rounded box
tube = patches.FancyBboxPatch(
    (0.2, 0.5), 0.6, 5,
    boxstyle="round,pad=0.02",
    edgecolor="black",
    facecolor="none",
    linewidth=1.5
)
ax.add_patch(tube)

# RBC section (bottom, darker gray)
rbc = patches.Rectangle((0.2, 0.5), 0.6, 2.5,
                        linewidth=1, edgecolor='black', facecolor='gray')
ax.add_patch(rbc)

# Plasma section (top, light gray)
plasma = patches.Rectangle((0.2, 3.0), 0.6, 2.5,
                           linewidth=1, edgecolor='black', facecolor='lightgray')
ax.add_patch(plasma)

# Add semi-permeable membrane as a dashed line (thicker)
ax.plot([0.2, 0.8], [3.0, 3.0], linestyle='--', color='black', linewidth=2.5)

# Move membrane label to the right side
ax.text(0.85, 2.9, "semi-permeable\nmembrane", fontsize=10, ha='left', va='bottom')

# Add labels for compartments
ax.text(0.85, 4.2, r"$Plasma$", fontsize=14, verticalalignment='center')
ax.text(0.85, 1.7, r"$Whole \, Blood$", fontsize=14, verticalalignment='center')

# Add arrows and molecule labels for diffusion
arrow_kwargs = dict(arrowstyle="->", color='blue', lw=1.5)
ax.annotate("", xy=(0.3, 3.2), xytext=(0.3, 3.6), arrowprops=arrow_kwargs)
ax.annotate("", xy=(0.7, 2.8), xytext=(0.7, 2.4), arrowprops=arrow_kwargs)

# Add "Drug" labels
ax.text(0.21, 3.7, "Free Drug", fontsize=10, color='blue', va='center', ha='left')
ax.text(0.42, 2.3, "Free Drug", fontsize=10, color='blue', va='center', ha='left')

# Generate Plasma Proteins In plasma (top)
np.random.seed(42)
x_plasma = np.random.uniform(0.25, 0.75, 5)
y_plasma = np.random.uniform(3.2, 5.3, 5)
ax.scatter(x_plasma, y_plasma, color='yellow', s=100)

# Generate Plasma Proteins In blood (top)
np.random.seed(42)
x_plasma = np.random.uniform(0.25, 0.75, 5)
y_plasma = np.random.uniform(0.7, 2.8, 5)
ax.scatter(x_plasma, y_plasma, color='yellow', s=100)

# Generate RBCs In blood (top)
np.random.seed(23)
x_plasma = np.random.uniform(0.25, 0.75, 5)
y_plasma = np.random.uniform(0.7, 2.8, 5)
ax.scatter(x_plasma, y_plasma, color='red', s=100)

# Generate blue dots for unbound compounds
np.random.seed(40)
# In plasma (top)
x_plasma = np.random.uniform(0.25, 0.75, 12)
y_plasma = np.random.uniform(3.2, 5.3, 12)
ax.scatter(x_plasma, y_plasma, color='blue', s=5)

# In RBC (bottom)
x_rbc = np.random.uniform(0.25, 0.75, 12)
y_rbc = np.random.uniform(0.7, 2.8, 12)
ax.scatter(x_rbc, y_rbc, color='blue', s=5)

# Final layout and display
plt.tight_layout()
plt.show()
