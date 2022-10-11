
length = int(input('Введите длину стороны квадрата: '))
perimeter = length * 4
square = length**2
print(perimeter)
print(square)
length1 = int(input('Введите длину стороны квадрата: '))
vwidth1 = int(input('Введите ширину стороны квадрата: '))
P = 2 * (length1 + vwidth1)
S = length1 * vwidth1
print('Периметр:', P)
print('Площадь:', S)

a = '#'
b = P + S
print(a * b)

salary = int(input('Введите заработную плату: '))
mortgageInterest = int(input('Какой процент от зп уходит на ипотеку: '))
life = int(input('Какой процент от зп уходит на жизнь: '))
mortgage = salary / 100 * mortgageInterest * 12
forlife = salary / 100 * life * 12
accumulation = salary * 12 - mortgage + forlife
print('На ипотеку было потрачено: ', (int(mortgage)))
print('Было накоплено: ', (int(accumulation)))



