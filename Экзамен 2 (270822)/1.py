# № 1
import os
print(os.getcwd())
os.mkdir('C:/Users/user/Desktop/exam_2')
os.chdir('C:/Users/user/Desktop/exam_2')
file_1 = open('test_1.txt', 'w+')
file_1.close()
file_2 = open('test_2.txt', 'w+')
file_2.close()
file_3 = open('test_3.txt', 'w+')
file_3.close()
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir('D:/Overone/Экзамен 2 (270822)')
os.rmdir('C:/Users/user/Desktop/exam_2')