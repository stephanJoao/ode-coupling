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
    global population_limit, growing_rate
    population_limit = 500
    growing_rate = 3
    growing_rate2 = 5
    
    # When working with only one diferential function there must be created a null extra position
    dy = np.zeros(2)
    # dy[0] = y[0]
    dy[0] = growing_rate * y[0] * np.log(population_limit / y[0])
    dy[1] = growing_rate2 * y[1] * np.log(population_limit / y[1])

    return dy

# Defines the parameters

# Step
h = 0.01

# Interval
t_range = np.array([0.0, 4.0])

# Initial values
y = 1
y_init = np.array([y, y], dtype='f')

# Calls the Euler method
[ts, ys] = euler_method('diferential', y_init, t_range, h)

# Prepares the results for visualization
node = len(y_init)
ys1 = ys[0::node]
ys2 = ys[1::node]

plt.plot(ts, ys1)
plt.plot(ts, ys2)
# plt.plot(t, func)
# plt.legend(["D_T", "D_LN", "T"], loc=2)
# plt.xlabel('horas', fontsize=17)
# plt.ylabel('concentracao de celulas', fontsize=17)
# plt.yscale('log')
plt.show()