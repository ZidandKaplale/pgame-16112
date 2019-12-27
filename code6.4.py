# Simpan dengan nama : code64.py
# Pemrograman Game Praktikum 6
# latihan code 6.4 : Perulangan (Loop) for
batas='*'*30


loyang = ["Apel", "Pisang", "Durian", "Melon"]
for buah in loyang:
	print(buah)


print(batas)
for x in range(5):
	print("Hallo Anak Info")


print(batas)
jumlah = 5
teks = "Informatika "
for x in range(jumlah):
	print(teks, end=',')


print(batas)
for buah in loyang:
	print(buah)
	if buah == "Pisang":
		break

print(batas)

for x in range(10,0,-1):
	print(x)

print(batas)

for x in range(10,0,-2):
	print(x)