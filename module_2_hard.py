

x = int(input('Введите число от 3 до 20: '))
if x < 3 or x > 20:
    print('отрубить палец дебилу')
result = ''
for i in range(1, x):
    for j in range(1, x):
        if x % (i+j) == 0 and i < j:
            result += str(i)+str(j)
print(result)
