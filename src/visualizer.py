"""
3D trajectory visualization module .
"""

import numpy as np
import matplotlib.pyplot as plt
from src.physics import R_EARTH

def plot_transfer(traj_initial: np.ndarray, traj_tx: np.ndarray, traj_final: np.ndarray, r_earth: float = R_EARTH):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0d1117')
    fig.patch.set_facecolor('#0d1117')

    # Scale to kilometers for plotting clarity
    scale = 1e3

    # Plot Earth as a reference wireframe
    u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:15j]
    x_e = (r_earth / scale) * np.cos(u) * np.sin(v)
    y_e = (r_earth / scale) * np.sin(u) * np.sin(v)
    z_e = (r_earth / scale) * np.cos(v)
    ax.plot_wireframe(x_e, y_e, z_e, color='#1f6feb', alpha=0.35, linewidth=0.8)

    # Plot orbits
    ax.plot(traj_initial[0]/scale, traj_initial[1]/scale, traj_initial[2]/scale, label='LEO (Initial)',color='#58a6ff', linewidth=1.5)
    ax.plot(traj_tx[0]/scale, traj_tx[1]/scale, traj_tx[2]/scale, label='Hohmann Transfer Arc', color='#f0883e', linestyle='--', linewidth=2)
    ax.plot(traj_final[0] / scale, traj_final[1] / scale, traj_final[2] / scale, label='Traget Orbit (GEO)', color='#3fb950', linewidth=1.5)

    #Formatting
    ax.set_xlabel('X (km)', color='#c9d1d9')
    ax.set_ylabel('Y (km)', color='#c9d1d9')
    ax.set_zlabel('Z (km)', color='#c9d1d9')
    ax.tick_params(colors='#8b949e')
    ax.grid(color='#30363d', linestyle=':', linewidth=0.5)

    # Equal aspect ratio scaling
    max_range = np.max(np.abs(traj_final[0:2])) / scale * 1.1
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(-max_range, max_range)

    ax.legend(facecolor='#161b22', edgecolor='#30363d', labelcolor='#c9d1d9')
    plt.title('Coplanar Orbital Transfer Maneuver', color='#f0f6fc', pad=20, fontsize=14)
    plt.tight_layout()
    plt.show()