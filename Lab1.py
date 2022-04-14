import numpy as np
import matplotlib.pyplot as plt


def interpolateLegendreToPowerTwo(function, x1, x2, x3, value):
    return (value - x2) * (value - x3) * function(x1) / ((x1 - x2) * (x1 - x3)) + (value - x1) * (
            value - x3) * function(x2) / ((x2 - x1) * (x2 - x3)) + (value - x1) * (value - x2) * function(x3) / (
                   (x3 - x1) * (x3 - x2))


def twoExponent(x):
    return 2 ** x


def linFunc(x):
    return x


def lnFunc(x):
    return np.log(x)


def plottingFunction(segmentStart, segmentEnd, partitionRate, function):
    plt.title('График для разбиения на ' + str(partitionRate) + ' частей')
    xSegment = np.linspace(segmentStart, segmentEnd, 1000)
    ySegment = [function(x) for x in xSegment]
    plt.plot(xSegment, ySegment, 'k')
    ax = plt.gca()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')


def addRectangleToPlotting(leftSide, rightSide, step, osnashenie, function):
    xLeft = np.linspace(leftSide, leftSide, 1000)
    ySides = np.linspace(0, function(leftSide + step * osnashenie), 1000)
    xRight = np.linspace(rightSide, rightSide, 1000)
    xTop = np.linspace(leftSide, rightSide, 1000)
    yTop = 0 * xTop + function(leftSide + step * osnashenie)
    plt.plot(xRight, ySides, 'b', lw=0.5)
    plt.plot(xLeft, ySides, 'b', lw=0.5)
    plt.plot(xTop, yTop, 'b', lw=0.5)


def addParaboleToPlotting(leftSide, step, function):
    xArange = np.linspace(leftSide, leftSide + step, 100)
    y = [interpolateLegendreToPowerTwo(function, leftSide, leftSide + step / 2, leftSide + step, x) for x in xArange]
    plt.plot(xArange, y, 'r', lw=0.5)


def rectangleIntegration(segmentStart, segmentEnd, partitionRate, osnashenie, function):
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


def simpsonIntegration(segmentStart, segmentEnd, partitionRate, function):
    summ = 0
    step = (segmentEnd - segmentStart) / partitionRate
    currentX = segmentStart
    plottingFunction(segmentStart, segmentEnd, partitionRate, function)
    for i in range(1, partitionRate + 1):
        addParaboleToPlotting(currentX, step, function)
        summ += function(currentX) + 4 * function(currentX + step / 2) + function(currentX + step)
        currentX += step
    summ *= step / 6
    return summ


def printComparing(result):
    print('Численное значение:', result)
    print('Разница значений, полученных численно и алгебраически:', abs(result - 3 / np.log(2)))


def printSimpsonResult():
    result = simpsonIntegration(0, 2, 1, twoExponent)
    printComparing(result)


def printRectangleResult():
    result = rectangleIntegration(0, 2, 1, twoExponent)
    printComparing(result)


def main():
    printSimpsonResult()
    # printRectangleResult()
    # plt.show()  # все графики рисуются на одной координатной плоскости и наслаиваются друг на друга, так что если нужен график,нужно вызывать только один метод для интегрирования


if __name__ == '__main__':
    main()
