# Simpan dengan nama : code61.py
# Pemrograman Game Praktikum 6
# latihan code 6 : Kondisional


myvar=input("Masukkan Numerik atau String : ")

if myvar.isnumeric():
	print("C1: Ya, Variable myvar Numerik : ", myvar)
else:
	pass
	
print('*'*25)

if not myvar.isnumeric():
	print("C2: Variable myvar BUKAN Numerik ! ")
elif myvar.isnumeric():
	print("C2: myvar : %s, adalah Numerik " % myvar) 
	print("C2: myvar : "+ myvar + ", adalah Numerik")
	print("C2: myvar Numerik : ", myvar) 