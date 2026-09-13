# Coplanar Orbital Transfer Simulator (Hohmann Transfer)

A numerical orbital mechanics simulator in Python modeling coplanar maneuvers between Low Earth Orbit (LEO) and Geostationary Earth Orbit (GEO) using the Hohmann transfer mechanism.

## Features
* **Analytic Delta-V Calculation**: Computes insertion (dv1) and circularization (dv2) impulse requirements using vis-viva principles.
* **Numerical Orbit Propagation**: Solves the Newtonian two-body equations of motion using 'scipy.integrate.solve_ivp'.
* **3D Trajectory Visualization**: Generates a 3D visualization displaying Earth, the initial orbit, the elliptical transfer arc, and the target orbit.

## Equations of Motion
The two-body orbital dynamics are governed by :
$$\ddot{\vec{r}} = -\frac{\mu}{r^3}\vec{r}$$

where $\mu = 3.986 \times 10{14} \text{ m}^3/\text{s}^2$ is Earth's standard gravitational parameter.

## Installation & Usage
'''bash
pip install -r requirements.txt
python main.py