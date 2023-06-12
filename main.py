import math
import sys

def calculate_arithmetic_sum(first_term, difference, last_term):
    n = last_term - first_term + 1
    sum_arithmetic = (n / 2) * (2 * first_term + (n - 1) * difference)
    return sum_arithmetic

def calculate_geometric_sum(first_term, common_ratio, last_term):
    if common_ratio == 1:
        sum_geometric = (last_term - first_term + 1) * first_term
    else:
        sum_geometric = first_term * ((1 - common_ratio**last_term) / (1 - common_ratio))
    return sum_geometric

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return x1, x2

def main():
    print("1 - Решение квадратного уравнения")
    print("2 - Расчет суммы арифметической прогрессии")
    print("3 - Расчет суммы геометрической прогрессии")
    choice = input("Выберите задание (1/2/3): ")

    match choice:
        case "1":
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            c = float(input("Введите коэффициент c: "))

            solutions = solve_quadratic_equation(a, b, c)

            print("Решения квадратного уравнения:")
            if isinstance(solutions, tuple):
                print("x1 =", solutions[0])
                print("x2 =", solutions[1])
            else:
                print("x =", solutions)

        case "2":
            first_term = float(input("Введите первый член прогрессии: "))
            difference = float(input("Введите разность арифметической прогрессии: "))
            last_term = int(input("Введите номер последнего члена прогрессии: "))

            sum_arithmetic = calculate_arithmetic_sum(first_term, difference, last_term)

            print("Сумма арифметической прогрессии:", sum_arithmetic)

        case "3":
            first_term = float(input("Введите первый член прогрессии: "))
            common_ratio = float(input("Введите знаменатель геометрической прогрессии: "))
            last_term = int(input("Введите номер последнего члена прогрессии: "))

            sum_geometric = calculate_geometric_sum(first_term, common_ratio,)
