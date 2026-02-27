#custon exception
class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f"Nama terlalu pendek! Minimal 3 karakter.")

class UmurError(Exception) :
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f"Umur tidak memenuhi syarat (17-60 tahun).")

class EmailError(Exception) :
    def __init__(self, email):
        self.email = email
        super().__init__(f"Email tidak valid! Harus mengandung '@'.")

class NoHpError(Exception) :
    def __init__(self, no_hp):
        self.no_hp = no_hp
        super().__init__(f"No HP tidak valid! Harus 10-13 digit angka.")

#Fungsi falidasi
def validasi_nama(nama_input):
    if len(nama_input) < 3:
        raise NamaError(nama_input)
    
def validasi_umur(umur_input):   
    if umur_input < 17 or umur_input > 60:
        raise UmurError(umur_input)

def validasi_email(email_input):
    if "@" not in email_input:
        raise EmailError(email_input)

def validasi_no_hp(no_hp_input):
    if not no_hp_input.isdigit() or len(no_hp_input) < 10 or len(no_hp_input) > 13:
        raise NoHpError(no_hp_input)

# proses input dan try-except
print('=== REGISTRASI PESERTA SEMINAR ===')
#input nama
while True:
    try:
        nama = input("Nama Lengkap : ")
        validasi_nama(nama)
        break
    except NamaError as e:
        print(f" [ERROR] {e}")
    else:
        break
#input umur
while True:
    try:
        umur = int(input("Umur : "))
        validasi_umur(umur)
        break
    except ValueError:
        print("[ERROR] Umur harus berupa angka.")
    except UmurError as e:
        print("[ERROR]", e)
    else:
        break
    
#input email
while True:
    try:
        email = input("Email: ")
        validasi_email(email)
        break
    except EmailError as e:
        print("[ERROR]", e)
    else:
        break

#input no hp
while True:
    try:
        no_hp = input("No HP: ")
        validasi_no_hp(no_hp)
        break
    except NoHpError as e:
        print("[ERROR]", e)
    finally:
        print("Selesai")

# output
print("=== DATA PESERTA ===")
print("Nama   :", nama)
print("Umur   :", umur, "tahun")
print("Email  :", email)
print("No HP  :", no_hp)
print("Status : TERDAFTAR")



