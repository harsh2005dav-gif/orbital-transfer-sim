"""
Main entry point for running the orbital transfer simulation.
"""

import numpy as np
from src.physics import (MU_EARTH, R_EARTH, hohmann_transfer_deltav, propagate_orbit)
from src.visualizer import plot_transfer

def main():
    # Define orbits: 400 km LEO to 35,786 km GEO
    r_initial = R_EARTH + 400_000.0
    r_target = R_EARTH + 35_786_000.0

    dv1, dv2, total_dv = hohmann_transfer_deltav(r_initial, r_target)

    print("=" * 50)
    print("    ORBITAL MANEUVER ANALYSIS: LEO -> GEO")
    print("=" * 50)
    print(f"Initial Orbital Radius : {r_initial / 1e3:,.1f} km")
    print(f"Target Orbital Radius  : {r_target / 1e3:,.1f} km")
    print("-" * 50)
    print(f"Delta-V 1 (Insertion) : {dv1:,.2f} m/s")
    print(f"Delta-V 2 (Circularize) : {dv2:,.2f} m/s")
    print(f"Total Delta-V Budget : {total_dv:,.2f} m/s ({total_dv/1e3:.3f} km/s)")
    print("=" * 50)

    # 1. Propagate Initial Orbit (one full period)
    v_init = np.sqrt(MU_EARTH / r_initial)
    t_period_init = 2 * np.pi * np.sqrt(r_initial**3 / MU_EARTH)
    t_init = np.linspace(0, t_period_init, 200)
    state_0 = np.array([r_initial, 0.0, 0.0, 0.0, v_init, 0.0])  
    traj_init = propagate_orbit(state_0, (0, t_period_init), t_init)

    # 2. Propagate Transfer Arc (half transfer ellipse)
    a_tx = (r_initial + r_target) / 2.0
    t_transfer = np.pi * np.sqrt(a_tx**3 / MU_EARTH)
    v_tx = np.sqrt(MU_EARTH * (2.0 / r_initial - 1.0 / a_tx))
    state_tx = np.array([r_initial, 0.0, 0.0, 0.0, v_tx, 0.0])
    t_tx = np.linspace(0, t_transfer, 200)
    traj_tx = propagate_orbit(state_tx, (0, t_transfer), t_tx)

    # 3. Propagate Target Orbit 
    v_target = np.sqrt(MU_EARTH / r_target)
    t_period_target = 2 * np.pi * np.sqrt(r_target**3 / MU_EARTH)
    state_target = np.array([-r_target, 0.0, 0.0, 0.0, -v_target, 0.0])
    t_target = np.linspace(0, t_period_target, 300)
    traj_target = propagate_orbit(state_target, (0, t_period_target), t_target)

    # Render 3D Visualizer
    print("\n[+] Generating 3D trajectory plot...")
    plot_transfer(traj_init, traj_tx, traj_target)

if __name__ == "__main__":
    main()