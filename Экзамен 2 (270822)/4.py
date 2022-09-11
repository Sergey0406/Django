# № 4
import random

set_1 = set([random.randint(0, 10) for j in range(10)])
set_2 = set([random.randint(0, 10) for g in range(10)])
print('set_1:', set_1, '\nset_2:', set_2)
if set_1 == set_2:
    print("1) Множества равны.")
else:
    print("1) Множества не равны.")
print('2) set_1 состоит из set_2 -', set_1.issubset(set_2))
print('2) set_2 состоит из set_1 -', set_2.issubset(set_1))
if set_1 & set_2:
    print('3) Множества пересекаются -', set_1 & set_2)
else:
    print('3) Множества не пересекаются.')
