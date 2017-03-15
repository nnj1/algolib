class LinReg:
    def __init__(self, points, stepsize):
        self.points = points
        self.step = stepsize
    def setData(self, points):
        self.points = points
    def addPoint(self, point):
        self.points.append(point)
    def getFit(self):
        # start with shit approximation (we can make this better)
        m, b, prevm, prevb = 1.0, 1.0, 1.1, 1.1
        # do the actual algorithm
        while abs((prevm - m))/self.step >= self.step and abs((prevb - b))/self.step >= self.step:
            prevm = m
            prevb = b
            newm = m - self.step * (1.0/len(self.points)) * self.__partialm(m, b)
            newb = b - self.step * (1.0/len(self.points)) * self.__partialb(m, b)
            m = newm
            b = newb
            #print {'slope': m, 'intercept':b}
        # return answers
        return {'slope': m, 'intercept':b}
    def __partialb(self, m, b):
        cost = 0.0
        for point in self.points:
            cost = cost + ((point[0]* m + b) - point[1])
        return cost
    def __partialm(self, m, b):
        cost = 0.0
        for point in self.points:
            cost = cost + (((point[0]* m + b) - point[1]) * point[0])
        return cost
    def __score(self, m, b):
        score = 0.0
        for point in self.points:
            score = score + ((point[0] * m + b) - point[1])**2
        return score/(2*len(self.points))

linreg = LinReg([[3,4],[9,3],[2,3]], 0.00001)
print linreg.getFit()