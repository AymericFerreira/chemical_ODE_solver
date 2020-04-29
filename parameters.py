import numpy as np
#### PARAMETERS positive feedback
def create_positive_feedback_parameters(V_PLC):
    k_3K = 0
    k_5P = 0.66
    K_PLC = 0.2
    K_3K = 0.4
    k1 = 1.11
    K_a = 0.08
    K_p = 0.13
    k2 = 0.0203
    V_serca = 0.1
    K_serca = 0.01
    epsilon = 0
    v0 = 0.0004
    phi = 0.0047
    V_pm = 0.01
    K_pm = 0.12
    beta = 0.185
    tau_r = 12.5
    K_i = 0.4
    # V_PLC = 3 * 1e-3 # not sure about it
    tau_P = 1 / (k_3K + k_5P)
    eta = k_3K / (k_3K + k_5P)
    Vbar_PLC = V_PLC * tau_P


    return [k_3K, k_5P, Vbar_PLC, K_PLC, K_3K,
            k1, K_a, K_p, k2, V_serca, K_serca,
            epsilon, v0, phi, V_pm, K_pm, beta,
            tau_r, K_i, tau_P, eta]


def create_negative_feedback_parameters(V_PLC):
    k_3K = 0.1
    k_5P = 0
    K_PLC = 0
    K_3K = 0.4
    k1 = 7.4
    K_a = 0.2
    K_p = 0.13
    k2 = 0.00148
    V_serca = 0.25
    K_serca = 0.1
    epsilon = 0
    v0 = 0.0004
    phi = 0.045
    V_pm = 0.01
    K_pm = 0.12
    beta = 0.185
    tau_r = 6.6
    K_i = 0.3
    # V_PLC = 0.4 * 1e-3 # not sure about it
    tau_P = 1 / (k_3K + k_5P)
    eta = k_3K / (k_3K + k_5P)
    Vbar_PLC = V_PLC * tau_P


    return [k_3K, k_5P, Vbar_PLC, K_PLC, K_3K,
            k1, K_a, K_p, k2, V_serca, K_serca,
            epsilon, v0, phi, V_pm, K_pm, beta,
            tau_r, K_i, tau_P, eta]

# ODE solver parameters
# abserr = 1.0e-8
# relerr = 1.0e-6
# stoptime = 10.0
# numpoints = 250

# t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

t0 = 0
tf = 250

t_span = (t0, tf)
# Initialise state variables
p = 0 # fig 8c p < 0.01 fig 8d p < 0.05
c = 0
s = 0
r = 0

# pack the state variables
y0 = [p, c, s, r]

# pack the parameters
param = create_positive_feedback_parameters(0.003)
# param = create_negative_feedback_parameters(0.0004)

