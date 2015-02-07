import pprint

class Euler:
    def __init__(self):
        pass
    def approx(self, func, t, y, step, iters):
        data = []
        i = 0
        while i <= iters:
            slope = func(t,y)
            y += (step * slope)
            data.append([i,t,y,slope])
            t += step
            i += 1
        return data
euler = Euler()

# usage
# Euler.approx(y' = f(t,y), x0, y0, stepsize, maxiterations)
data = euler.approx(lambda t,y : 2*(y**3) + t**2, 0, -0.5, 0.1, 20)

print 'Iter\tt\ty\tm'
pp = pprint.PrettyPrinter(indent=0)
pp.pprint(data)
