# № 2
C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
print('Сумма С_1 =', sum(C_1))
print('Сумма С_2 =', sum(C_2))
if sum(C_1) > sum(C_2):
    print('1) Сумма элементов больше в кортеже С_1')
else:
    print('1) Сумма элементов больше в кортеже С_2')
print('min C_1 =', min(C_1), '\nmax C_1 =', max(C_1))
print('min C_2 =', min(C_2), '\nmax C_2 =', max(C_2))
print('2) Порядковый номер мин-го элемента в С_1:',
      C_1.index(min(C_1)),
      '\n     Порядковый номер макс-го элемента в С_1:',
      C_1.index(max(C_1)))
print('3) Порядковый номер мин-го элементав С_2:',
      C_2.index(min(C_2)),
      '\n     Порядковый номер макс-го элементав С_2:',
      C_2.index(max(C_2)))