n=[-1, -2, -3, 4, 5, 6, 7, 8, -9]
average=0
for number in n:
    if (number>=0):
        average+=number
print("Список чисел", n)
print("Среднє арифметичне невід'ємних чисел списку = ", average)