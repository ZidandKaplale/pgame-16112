# latihan code 5.2 : Tuple 

# variabel dan elemen 
buah=('Durian', 'Mangga', 'Rambutan', 'Mangga')
print("Jumlah Element :", len(buah))
print("Jumlah Buah Mangga:", buah.count("Mangga"))
buah=('Durian', 'Mangga', 'Rambutan', 'Mangga','Salak', 
('Nangka', 'Apel'))
print("Bauah [-1][0] :", buah[-1][0])
x_buah = list(buah) 
x_buah[0] = "Melon" 
Buah = tuple(x_buah)
print("Tuple :", buah)