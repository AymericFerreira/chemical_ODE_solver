from scipy.integrate import odeint, solve_ivp

def chemical_equations(y, t, k):
    """
    Defines the equations
    :param y: vector of state variables
    :param t: time
    :param k: vector of parameter
    :return: system of all the equations
    """
    # rf = k * y[0] * y[1]**2
    p, c, s, r = y

    f = [

    ]
    return f


ABC = 2

y0 = [A0, B0, C]
k = kf,
t = np.arange(100)

#%%

y = odeint(rhs, y0, t, k)

