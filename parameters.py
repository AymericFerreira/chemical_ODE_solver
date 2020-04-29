#### PARAMETERS
# dp/dt
k_3K =
k_5P =
tau_P = 1 / (k_3K + k_5P)
Vbar_PLC =
# c =
K_PLC =
eta = k_3K / (k_3K + k_5P)
K_3K =
# p =

# dc/dt
k1 =
# r =
K_a =
K_p =
k2 =
# s =
V_serca =
K_serca =
epsilon =
v0 =
theta =
V_pm =
K_pm =

# ds/dt
beta =

# dr/dt
tau_r =
K_i =

# Initialise state variables
p =
c =
s =
r =
# pack the state variables
w0 = [p, c, s, r]
# pack the parameters
p = [tau_P, Vbar_PLC, eta, k_3K, k1, K_a, ]