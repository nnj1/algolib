import pprint

class RK4:
    def __init__(self):
        pass
    def approx(self, func, t, y, h, iters):
        data = []
        i = 0
        while i <= iters:
            k1 = func(t,y)
            k2 = func(t + h/2, y + (1/2)*k1*h)
            k3 = func(t + h/2, y + (1/2)*k2*h)
            k4 = func(t + h, y + k3*h)
            y += (h/6)*(k1 + 2*k2 + 2*k3 + k4)
            
            data.append([i,t,y,k1])
            t += h
            i += 1
        return data
kutta = RK4()

# usage
# Euler.approx(y' = f(t,y), x0, y0, stepsize, maxiterations)
data = kutta.approx(lambda t,y : y/2 + t, 0, -0.5, 0.1, 100)

print 'Iter\tt\ty\tm'
pp = pprint.PrettyPrinter(indent=0)
pp.pprint(data)
