def check_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        print("Треугольника с такими сторонами не существует")
        return
    if a != b and b != c and a != c:
        print("Треугольник разносторонний")
    elif a == b and b == c:
        print("Треугольник равносторонний")
    else:
        print("Треугольник равнобедренный")


a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))


check_triangle(a, b, c)
