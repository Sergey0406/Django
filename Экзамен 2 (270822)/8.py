# № 8
#Depeche_Mode_violator_songsdict:
songsdict = {'World in My Eyes': 4.76,
                     'Sweetest Perfection': 5.43,
                     'Personal Jesus': 4.56,
                     'Halo': 4.30,
                     'Waiting for the Night': 6.07,
                     'Enjoy the Silence': 4.6,
                     'Policy of Truth': 4.88,
                     'Blue Dress': 4.18,
                     'Clean': 5.68}
# 1
sum = 0
for i in songsdict:
    sum += songsdict[i]
print('1) Общее звучание всех песен:', sum, 'минут')
# 2
list1 = list(songsdict)
del list1[7]
print('2) Список песен продолжительностью более 5 минут:', list1[1:8:3])
# 3
list2 = list(songsdict)
list3 = []
songs_duration = []
for j in list2:
    if j.count(' ') == 0:
        list3.append(j)
for k in songsdict:
    songs_duration.append(songsdict[k])
songsdict_2 = dict(zip(list3, songs_duration[3:10:5]))
print('3) Словарь песен, названия которых состоят из 1-го слова:', songsdict_2)