angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

try:
    nilai_1 = float(input('masukkan angka pertama : '))
    nilai_2 = float(input('masukkan angka kedua : '))

    hasil = nilai_1 / nilai_2

    print('hasil pembagian:', hasil)

except ValueError:
    print('Harus berupa angka bulat!')

except IndexError:
    print('Index di luar jangkauan!')

finally:
    print('Selesai.')









