class Biodata :
    def __init__(self, nama, kelas, usia):
        self.nama = nama
        self.kelas = kelas
        self.usia = usia
    
    def identitas(self):
        print("Hello, saya" + self.nama + self.kelas + self.usia ) 

    def perkenalan(self):
        print(f"{self.nama} umur {self.usia}")


p1 = Biodata("brigita", "3 SMA", 17)
p2 = Biodata("nabila", "1 SMA", 15)
p3 = Biodata("bella", "2 SMA", 16)

print(p1.nama)
print(p1.kelas)
print(p1.usia)


    



