z = [2, 3, 4, 5, 6, 7, 8, 9, 0]
y = [0, 12, 4, 6, 242, 7, 9]
print(0, 4, 6, 7, 9)
for satu in zip(z, y):
    print(satu)
    if satu == 6:
        break
print("6 ditemukan, " + "dan hentikan loop")