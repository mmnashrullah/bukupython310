#menambah ke file

try: #buka file sebelum ditambah
    objFile = open("pohon taman.txt", "r")
    bacaAwal = objFile.read() #inisiasi file.read()
    # Baca dan cetak seluruh file
    print("=== Isi File Sebelum Ditulis ===")
    print(bacaAwal)
except BaseException as be:
    print('Error: ', be)
finally:
    objFile.close()

try: #buka file untuk ditambah
    objFile = open("pohon taman.txt", "w+")
    dataWrite = "\nKemuning     Murraya paniculata"
    objFile.write(dataAppend)
    objFile.close()
except BaseException as be:
    print('Error: ', be)
else: #tampilkan isi file hasil tambahan bila tidak error
    objFile = open("pohon taman.txt", "r")
    bacaHasilTambah = objFile.read() #inisiasi file.read()
    # Baca dan cetak seluruh file
    print("=== Isi File Sesudah Ditulis ===")
    print(bacaHasilTambah)
finally:
    objFile.close()
