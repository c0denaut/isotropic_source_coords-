from k1 import Isotropic

while True:
    try:
        n = int(input("Введите количество точек: "))
        method = Isotropic(n)
        break
    except ValueError as e:
        print(f"Ошибка: {e}")
        print("Пожалуйста, попробуйте снова.\n")

method.plot()
