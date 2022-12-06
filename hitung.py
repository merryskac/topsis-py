#SPK pemilihan laptop
#terdapat 5 merk, yaitu asus, HP, Lenovo, Acer
#terdapat 5 kriteria dengan bobot 0.15, 0.25, 0.1, 0.1, 0.4

import numpy as np

kriteria  = [[4,4,4,2,3], #asus
        [2,4,2,2,3], #HP
        [3,4,4,2,2], #Lenovo
        [1,4,4,2,4]] #acer 
num = np.rot90(kriteria)[::-1]

bobot = [0.15,0.25,0.1,0.1,0.4]

#pembagi untuk kebutuhan matriks ternormalisasi
#data kriteria/pembagi
pembagi = []
#mencari pembagi
for i in num:
    jumlah = np.sqrt(sum([k**2 for k in i]))
    pembagi.append(np.round(jumlah,2))
    print(np.round(jumlah,2))

mtx_ternormalisasi = np.zeros((4,5))

for idx in range(len(pembagi)):
    for i in range(len(num[idx])):
        print(f'hasil kolom {idx+1} '+ str(round(num[idx][i]/pembagi[idx],3)))
        mtx_ternormalisasi[i][idx]=round(num[idx][i]/pembagi[idx],3)
#pakai di variabel kriteria
print('-----------------------------------')
print("mtx ternormalisasi")
print(mtx_ternormalisasi)
print('---------------(Bobot)--------------------')
print("bobot")
print(bobot)
print('---------------Matriks Normalisasi terbobot--------------------')
mtx_normal_bobot = np.round(mtx_ternormalisasi*bobot,3)
print(mtx_normal_bobot)
print('---------------Nilai Min Max per kriteria--------------------')
mtx_normal_bobot_perkriteria = np.rot90(mtx_normal_bobot)[::-1]
min_value_per_kriteria = [min(i) for i in mtx_normal_bobot_perkriteria]
max_value_per_kriteria = [max(i) for i in mtx_normal_bobot_perkriteria]
print('min: '+str(min_value_per_kriteria))
print('max: '+str(max_value_per_kriteria))
print('---------------Jarak Solusi Ideal Positif--------------------')
a = 1
ideal_positif = []
for i in mtx_normal_bobot:
    print('C'+str(a)+'= '+str(np.round(np.sqrt(sum((i-max_value_per_kriteria)**2)),3)))
    ideal_positif.append(np.round(np.sqrt(sum((i-max_value_per_kriteria)**2)),3))
    a+=1
print('---------------Jarak Solusi Ideal Negatif--------------------')
ideal_negatif = []
for i in mtx_normal_bobot:
    print('C'+str(a)+'= '+str(np.round(np.sqrt(sum((i-min_value_per_kriteria)**2)),3)))
    ideal_negatif.append(np.round(np.sqrt(sum((i-min_value_per_kriteria)**2)),3))
    a+=1
print('---------------preferensi--------------------')
print(ideal_negatif)
for i in range(len(ideal_negatif)):
    print(np.round(ideal_negatif[i]/(ideal_negatif[i]+ideal_positif[i]),3))



