import numpy as np

num = [[4,2,3,1],
       [4,4,4,4],
       [4,2,4,4],
       [2,2,2,2],
       [3,3,2,4]]
kriteria = np.rot90(num)[::-1]

bobot = [0.15,0.25,0.1,0.1,0.4]
pembagi = []
for i in num:
    jumlah = np.sqrt(sum([k**2 for k in i]))
    pembagi.append(np.round(jumlah,2))
    print(np.round(jumlah,2))

mtx_ternormalisasi = np.zeros((4,5))

for idx in range(5):
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
print(np.round(mtx_ternormalisasi*bobot,3))



