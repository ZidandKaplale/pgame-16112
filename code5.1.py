# latihan code 5.1 : List (lanjutan)

#  buah=["Durian","Mangga","Rambutan] 
buah=("Durian","Mangga","Rambutan") 

print(buah)
print(type(buah)) 

buah=("Durian","Mangga","Rambutan",("Nangka","Apel"))
print("tuple didalam tuple : ", buah)
x_buah=list(buah)	
x_buah[0]="Melon"	
buah = tuple(x_buah)	
print("Buah setelah diubah element [0] : ", buah)