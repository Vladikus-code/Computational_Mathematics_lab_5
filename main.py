from math import sqrt, log


def function(x):
    rezult = pow(1 + x, 2) / sqrt(log(x))
    return rezult


def left_rectangle_integral(f, a, b, _acc):
    n = 2
    h = abs((b - a) / float(n))
    #значения для входа в цикл
    r1 = 1
    r2 = 2

    while(abs(r1 - r2) > _acc):
        r1 = sum([f((a + (k * h))) for k in range(0, n)]) * h

        n *= 2
        h = abs((b - a)/float(n))

        r2 = sum([f((a + (k * h))) for k in range(0, n)]) * h

    return r1


def medium_rectangle_integral(f, a, b, _acc):
    n = 2
    h = abs((b - a) / float(n))

    #значения для входа в цикл
    r1 = 1
    r2 = 2

    while(abs(r1 - r2) > _acc):
        r1 = sum([f(a + (h * k) + h/2) for k in range(0, n)]) * h

        n *= 2
        h = abs((b - a)/float(n))

        r2 = sum([f(a + (h * k) + h/2) for k in range(0, n)]) * h

    return r1


if __name__ == '__main__':
    print("Интегрируемая функция: f(x) = (x+1)^2 / sqrt(ln(x))\n")

    acc = 0.001 #точность
    x1 = 5.2
    x2 = 12.0
    print("Используем формулу левых прямоугольников:")
    print(f"Ответ : {left_rectangle_integral(function, x1, x2, acc)}  с точностью  {acc}\n")
    print("Используем формулу средних прямоугольников:")
    print(f"Ответ : {medium_rectangle_integral(function, x1, x2, acc)}  с точностью  {acc}\n")


    #print("\nОтвет:", a2, "\nКоличество разбиений:", n)

    #print("Используем формулу средних прямоугольников")
