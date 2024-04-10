"""Решение дифференциальных уравнений (Метод Эйлера)"""
import numpy
from matplotlib import pyplot

"""
    x`` + x = 0; x(0) = 1, x`(0) = 1
"""

def function(x, v):
    """
        Выше написанное уравнение разложили на систему уравнений
        x` = v
        v` = -x
    """
    dx_dt = v
    dv_dt = -x
    return dx_dt, dv_dt


def methodEuler(function, initialConditions, stepSize, stepCount):
    """
        Входные данные:
        function - функция, описывающая уравнние
        initialConditions - начальные данные
        stepSize - величина шага
        stepCount - кол-во шагов

        Выходные данные:
        xValues - значение х на каждом шаге
        vValues - значение производной х на каждом шаге
    """
    xValues = numpy.zeros(stepCount + 1)
    vValues = numpy.zeros(stepCount + 1)

    xValues[0] = initialConditions[0]
    vValues[0] = initialConditions[1]

    for i in range(stepCount):
        x = xValues[i]
        v = vValues[i]

        dx_dt, dv_dt = function(x, v)

        xValues[i+1] = x + dx_dt * stepSize
        vValues[i+1] = v + dv_dt * stepSize

    return xValues, vValues


def analiticSolution(t):
    # аналитическое решение, при котором с1= 1 и с2 = 1
    return numpy.cos(t) + numpy.sin(t)


def main():
    initialConditions = [1, 1]
    stepSize = 0.1
    stepCount = 100

    xValues, vValues = methodEuler(function, initialConditions, stepSize, stepCount)
    tValues = numpy.linspace(0, stepSize * stepCount, stepCount + 1)
    analiticValues = analiticSolution(tValues)
    errorValues = numpy.abs(xValues - analiticValues)

    pyplot.plot(tValues, xValues, label="x(t)")
    pyplot.plot(tValues, vValues, label="v(t)")
    # pyplot.plot(tValues, errorValues, label="Погрешность")
    pyplot.legend()
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    main()