import matplotlib.pyplot as plt
import math


def f(x):
    y = math.sqrt(1-(math.fabs(x)-1)**2)
    return y


def g(x):
    y = -3*math.sqrt(1-math.sqrt(math.fabs(x))/math.sqrt(2))
    return y

xpoints = []
ypoints = []

plt.ion()

x = -2
while x <= 2:
    xpoints.append(x)
    y = f(x)
    ypoints.append(y)
    plt.plot(xpoints,ypoints)
    p = round(100*(x+2)/4,0)/2
    plt.title(str(p)+"%")
    plt.draw()
    plt.pause(0.05)
    plt.clf()
    x += 0.05

x = 2
while x >= -2:
    xpoints.append(x)
    y = g(x)
    ypoints.append(y)
    plt.plot(xpoints,ypoints)
    p = round(50 + 100*(2-x)/4,0)/2
    plt.title(str(p)+"%")
    plt.draw()
    plt.pause(0.05)
    plt.clf()
    x -= 0.05

xpoints.append(-2)
y = g(-2)
ypoints.append(y)
plt.title("DEAR STUDENTS \n HAPPY PROGRAMMING :)")
plt.xlabel("FROM STEPHEN")
plt.plot(xpoints,ypoints)
plt.draw()
plt.pause(10)

quit()