from math import sqrt, log

def function(x):
    result = pow(1 + x, 2) / sqrt(log(x))
    return result


def left_rectangle_integral(f, a, b, _acc):
    n = 2
    h = abs(b - a) / float(n)
    #значения для входа в цикл
    r1 = 1
    r2 = 2

    while(abs(r1 - r2) > _acc):
        r1 = sum([f((a + (k * h))) for k in range(0, n)]) * h

        n *= 2
        h = abs(b - a)/float(n)

        r2 = sum([f((a + (k * h))) for k in range(0, n)]) * h

    return r1


def medium_rectangle_integral(f, a, b, _acc):
    n = 2
    h = abs(b - a) / float(n)

    #значения для входа в цикл
    r1 = 1
    r2 = 2

    while(abs(r1 - r2) > _acc):
        r1 = sum([f(a + (h * k) + h/2) for k in range(0, n)]) * h

        n *= 2
        h = abs(b - a)/float(n)

        r2 = sum([f(a + (h * k) + h/2) for k in range(0, n)]) * h

    return r1


def iteration(a, b):
    m = 3 #номер порядка
    C = 8
    c0 = m/C
    w = [1, 3, 3, 1]  # значения весовых коэффициентов порядка m
    h = abs(b - a) / float(3)
    return sum([function(a + (k * h)) * w[k] for k in range(0, 4)]) * h * c0

def newton_cotes_integral(f, a, b, _acc):
    m = 3 #номер порядка
    C = 8
    c0 = m/C
    w = [1, 3, 3, 1] #значения весовых коэффициентов порядка m
    n = pow(m, 1)
    h = abs(b - a) / float(3)# шаг для метода
    h_gen = abs(b - a) / float(n)


    #значения для входа в цикл
    r1 = 0
    r2 = sum([f(a + (k * h_gen)) * w[k] for k in range(0, 4)]) * h_gen * c0

    while(abs(r1 - r2) > _acc):
        n *= 3
        r1 = r2
        temp = 0
        h_gen = abs(b - a) / float(n)
        x = a

        for i in range(0, n):
            temp += iteration(x, x+h_gen)
            x += h_gen

        r2 = temp

    return r2


if __name__ == '__main__':
    print("Интегрируемая функция: f(x) = (x+1)^2 / sqrt(ln(x))\n")

    acc = 0.01 #точность
    x1 = 5.2 #левая граница интервала интегрирования
    x2 = 12.0 #правая граница интервала интегрирования
    print("Используем метод левых прямоугольников:")
    print(f"Ответ : {left_rectangle_integral(function, x1, x2, acc)}  с точностью  {acc}\n")
    print("Используем метод средних прямоугольников:")
    print(f"Ответ : {medium_rectangle_integral(function, x1, x2, acc)}  с точностью  {acc}\n")
    print("Используем метод Ньютона-Котеса:")
    print(f"Ответ : {newton_cotes_integral(function, x1, x2, acc)}  с точностью  {acc}\n")


