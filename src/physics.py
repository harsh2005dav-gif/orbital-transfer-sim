import numpy as np
from scipy.integrate import solve_ivp

MU_EARTH = 3.986004418e14
R_EARTH = 6378137.0

def hohmann_transfer_deltav(r1: float, r2: float, mu: float = MU_EARTH) -> tuple[float, float, float]:
    v1 = np.sqrt(mu / r1)
    v2 = np.sqrt(mu / r2)
    a_tx = (r1 + r2) / 2.0
    v_tx_periapsis = np.sqrt(mu * (2.0 / r1 - 1.0 / a_tx))
    v_tx_apoapsis = np.sqrt(mu * (2.0 / r2 - 1.0 / a_tx))
    dv1 = abs(v_tx_periapsis - v1)
    dv2 = abs(v2 - v_tx_apoapsis)
    return dv1, dv2, dv1 + dv2


def two_body_ode(t: float, state: np.ndarray, mu: float = MU_EARTH) -> np.ndarray:
    r_vec = state[0:3]
    v_vec = state[3:6]
    r_mag = np.linalg.norm(r_vec)
    a_vec = -mu * r_vec / (r_mag ** 3)
    return np.concatenate([v_vec, a_vec])


def two_body_ode(t: float, state: np.ndarray, mu: float = MU_EARTH) -> np.ndarray:
    r_vec = state[0:3]
    v_vec = state[3:6]
    r_mag = np.linalg.norm(r_vec)
    a_vec = -mu * r_vec / (r_mag ** 3)
    return np.concatenate([v_vec, a_vec])

def propagate_orbit(initial_state: np.ndarray, t_span: tuple[float, float], t_eval: np.ndarray, mu: float = MU_EARTH):
    solution = solve_ivp(
        fun=two_body_ode,
        t_span=t_span,
        y0=initial_state,
        t_eval=t_eval,
        args=(mu,),
        rtol=1e-9,
        atol=1e-9,
    )
    return solution.y