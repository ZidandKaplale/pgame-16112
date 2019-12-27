# latihan code 5.3 : Dictionary

# variabel dan nilai elemen 
dc = { "Kampus":"UMMU", "Prodi":"Info", "Lokasi":"Ternate",   
	"Tahun":2019 } 
print(dc["Tahun"])
print(dc.get("Tahun"))
dc["Tahun"]= 2020 
dc["Lokasi"] = "Sasa"
print("Dictionary :", dc)