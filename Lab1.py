import numpy as np
import matplotlib.pyplot as plt


def twoExponent(x):
    return 2 ** x


def lnFunc(x):
    return np.log(x)


def plottingFunction(segmentStart, segmentEnd, partitionRate, function):
    plt.title('График для разбиения на ' + str(partitionRate) + ' частей')
    xSegment = np.linspace(segmentStart, segmentEnd, 1000)
    ySegment = [function(x) for x in xSegment]
    plt.plot(xSegment, ySegment, 'b')
    ax = plt.gca()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')


def addRectangleToPlotting(leftSide, rightSide, step, osnashenie, function):
    xLeft = np.linspace(leftSide, leftSide, 1000)
    ySides = np.linspace(0, function(leftSide + step * osnashenie), 1000)
    xRight = np.linspace(rightSide, rightSide, 1000)
    xTop = np.linspace(leftSide, rightSide, 1000)
    yTop = 0 * xTop + function(leftSide + step * osnashenie)
    plt.plot(xRight, ySides, 'k', lw=0.5)
    plt.plot(xLeft, ySides, 'k', lw=0.5)
    plt.plot(xTop, yTop, 'k', lw=0.5)


def integrate(segmentStart, segmentEnd, partitionRate, osnashenie, function):
    # для oscnashenie = 0 берется левая точка отрезка, для osnachenie = 1 - правая
    summ = 0
    step = (segmentEnd - segmentStart) / partitionRate
    print('Количество итераций:', partitionRate)
    print('Шаг интегрирования:', step)
    currentX = segmentStart
    plottingFunction(segmentStart, segmentEnd, partitionRate, function)
    for i in range(1, partitionRate + 1):
        addRectangleToPlotting(currentX, currentX + step, step, osnashenie, function)
        summ += function(currentX + step / 2)
        currentX += step
    summ *= step
    return summ


resOfTwoExponent = integrate(0, 2, 100, 1 / 2, twoExponent)
print('Численное значение:', resOfTwoExponent)
print('Разница значений, полученных численно и алгебраически:', abs(resOfTwoExponent - 3 / np.log(2)))
plt.show()