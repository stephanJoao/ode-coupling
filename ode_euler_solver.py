# Library importing
import matplotlib.pyplot as plt
import numpy as np

# Function evaluation
# Receives name and arguments, return the function evaluated
def feval(funcName, *args):
    return eval(funcName)(*args)

# Defines the numeric resolution of Euler
def euler_method(func, y_init, t_range, step):
    # Number of initial values
    m = len(y_init)

    # Number of iterations necessary
    n = int((t_range[1] - t_range[0]) / step)

    # Initial values
    t = t_range[0]
    y = y_init

    # Containers for solutions
    tsol = np.empty(0)
    tsol = np.append(tsol, t)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    # Iterations of the method
    for i in range(n):
        # Calculate the diferential
        dy = feval(func, t, y)

        # Increments
        t = t + step

        for j in range(m):
            y[j] = y[j] + (step * dy[j])

        # Storing solutions
        tsol = np.append(tsol, t)
        ysol = np.append(ysol, y)

    return [tsol, ysol]

# Defines the evaluated system's ODE(s)
def diferential(t, y):
    alpha_D = 0
    DT = 0
    V_LV = 0
    V_LN = 0.1
    
    alpha_T_c = 0
    estable_T_c = 0
    gamma_T = 0
    theta_BV = 1 #TODO Matheus falou que provavelmente esse valor seria considerado 1, verificar com Bárbara
    Tt_c = 0
    V_BV = 0

    #TODO esses valores ainda estão meio confusos na primeira parte da tese do Matheus
    b_T = 0
    rho_T = 0
    b_rho = 0
    alpha_T_h = 0
    estable_T_h = 0

    rho_B = 0
    alpha_B = 0
    estable_B = 0
    
    rho_F = 0
    gamma_F = 0
    FT = 0

    # When working with only one diferential function there must be created a null extra position
    dy = np.zeros(5)

    # Dendritic cells
    dy[0] = alpha_D * (DT - y[0]) * (V_LV / V_LN)
    # Cytotoxic T cells
    dy[1] = alpha_T_c * (estable_T_c - y[1]) - (gamma_T * theta_BV * (y[1] - Tt_c)) * (V_BV / V_LN)
    # Helper T cells
    dy[2] = b_T*(rho_T * y[2] * y[0] - y[2]*y[0]) - (b_rho * y[2] * y[0] * y[3]) + alpha_T_h * (estable_T_h - y[2])
    # B cells
    dy[3] = (b_rho * ((rho_B * y[2] * y[0]) - (y[2] * y[0] * y[3]))) + alpha_B * (estable_B - y[3])
    # Antibodies
    dy[4] = rho_F - ((gamma_F * theta_BV * (y[4] - FT)) * (V_BV / V_LN))

    return dy

# Defines the parameters


# Step
h = 0.01

# Interval
t_range = np.array([0.0, 4.0])  # TODO

# Initial values
DL = 0     # Dendritic cells
TL_c = 0.2  # Cytotoxic T cells
TL_h = 0.4  # Helper T cells
B = 0      # B cells
FL = 0     # Antibodies
y_init = np.array([DL, TL_c, TL_h, B, FL], dtype='f')

# Calls the Euler method
[ts, ys] = euler_method('diferential', y_init, t_range, h)

# Prepares the results for visualization
node = len(y_init)  # TODO Not working
ys1 = ys[0::node]
ys2 = ys[1::node]
ys3 = ys[2::node]
ys4 = ys[3::node]
ys5 = ys[4::node]

plt.plot(ts, ys1)
plt.plot(ts, ys2)
plt.plot(ts, ys3)
plt.plot(ts, ys4)
plt.plot(ts, ys5)
# plt.plot(t, func)
# plt.legend(["D_T", "D_LN", "T"], loc=2)
# plt.xlabel('horas', fontsize=17)
# plt.ylabel('concentracao de celulas', fontsize=17)
# plt.yscale('log')
plt.show()
