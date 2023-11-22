#capstone modul 1
# Nama : Aura Latifa
# Menggunakan data karyawan
# Poin yang dinilai : video penjelasan, Fitur Create, Fitur Read, Fitur Update, Fitur Delete, integrasi sistem dan efisiensi kode


dataKaryawan = [
    {
        'NIP': 200502122,
        'Nama': 'Muhammad Bara',
        'Jabatan': 'Direktur',
        'Divisi': 'Keuangan',
        'Masa Kerja': '10 Tahun'
    },
    {
        'NIP': 200702122,
        'Nama' : 'Farrel Abdullah',
        'Jabatan' : 'Manager',
        'Divisi' : 'Pemasaran',
        'Masa Kerja' : '7 Tahun'  
    },
    {
        'NIP': 200802122,
        'Nama' : 'Ajeng Putri',
        'Jabatan' : 'Staff',
        'Divisi' : 'Produksi',
        'Masa Kerja' : '3 Tahun'  
    },
    {
        'NIP': 200922122,
        'Nama' : 'Devi Aryani',
        'Jabatan' : 'Staff',
        'Divisi' : 'Produksi',
        'Masa Kerja' : '2 Tahun'  
    },
    {
        'NIP': 201422122,
        'Nama' : 'Putri Anjani',
        'Jabatan' : 'Staff',
        'Divisi' : 'Pemasaran',
        'Masa Kerja' : '2 Tahun'
    }
]

# Pilihan untuk menampilkan semua data karyawan
def daftarKaryawan():
    print('\n\t\t===========================================================================================')
    text = ('\t\tData Karyawan PT. NUSA DUA')
    print(text.center(91))
    print('\t\t===========================================================================================')
    print('\t\t-------------------------------------------------------------------------------------------')
    print('\t\t| No  |    NIP   |        Nama        |   Jabatan    |      Divisi    |     Masa Kerja    |')
    print('\t\t+-----+----------+--------------------+--------------+----------------+-------------------+')
    for i in range(len(dataKaryawan)):
        print('\t\t|{:^5}|{:^10}|{:^20}|{:^14}|{:^16}|{:^19}|'.format(i+1,dataKaryawan[i]['NIP'],dataKaryawan[i]['Nama'],dataKaryawan[i]['Jabatan'],dataKaryawan[i]['Divisi'],dataKaryawan[i]['Masa Kerja']))
        print("\t\t+-----+----------+--------------------+--------------+----------------+-------------------+")


# Pilihan untuk no.1  read menu dari report data karyawan
def reportKaryawan():
    while True:
        reportMenu = input('''
+=========================================+
|        Menu Report Data Karyawan        |
+=========================================+
|                                         |
|   1. Menampilkan semua data karyawan    |
|   2. Menampilkan data karyawan tertentu |
|   3. Kembali ke menu utama              |
+-----------------------------------------+
Silahkan pilih daftar diatas [1-3] : ''')
        # reportMenu = int(input('''Silahkan pilih daftar diatas [1-3] : '''))
        if reportMenu == '1' :
            daftarKaryawan()
        elif reportMenu == '2' :
            dataTertentu()
        elif reportMenu == '3':
            menuAwal()
        else:
            print('*** Anda memasukan pilihan yang salah *** \nMohon masukkan pilihan sesuai dengan menu di atas [1-3] ')
            continue

# Menampilkan pilihan no 2 pada fitur menu report (data tertentu)
def dataTertentu():
        while True:
            inputNip1 = (input('''Masukkan Nomer Induk Pegawai (NIP) : '''))
            if inputNip1.isnumeric()== True:
                inputNip = int(inputNip1)
                for i in range (len(dataKaryawan)):
                    if inputNip == dataKaryawan[i]['NIP']:
                        print('\n\t\t===========================================================================================')
                        text = ('\t\tData Karyawan PT. NUSA DUA')
                        print(text.center(91))
                        print('\t\t===========================================================================================')
                        print("\t\t-------------------------------------------------------------------------------------------")
                        print("\t\t| No  |    NIP   |        Nama        |   Jabatan    |      Divisi    |     Masa Kerja    |")
                        print("\t\t+-----+----------+--------------------+--------------+----------------+-------------------+")
                        print(f'''\t\t|{i+1:^5}|{dataKaryawan[i]['NIP']:^10}|{dataKaryawan[i]['Nama']:^20}|{dataKaryawan[i]['Jabatan']:^14}|{dataKaryawan[i]['Divisi']:^16}|{dataKaryawan[i]['Masa Kerja']:^19}|''')
                        print("\t\t+-----+----------+--------------------+--------------+----------------+-------------------+")
                        reportKaryawan()
                        break
                    elif (i == len(dataKaryawan)-1) and (inputNip != dataKaryawan[i]['NIP']):
                         print('''
                            \n***Data Karyawan tidak ditemukan***\n''')
            else:
                print("\n***NIP harus berupa angka, silahkan ketikkan NIP yang benar***\n")

#Tambah data karyawan
def addKaryawan ():
    while True:
        inputNewkaryawan = input('''
+=============================+
|  Menu Tambah Data Karyawan  |         
+=============================+
|                             |
| 1. Tambah data karyawan     |
| 2. Kembali ke menu utama    |
+-----------------------------+    
Silahkan pilih daftar di atas [1-2] : ''')
        if inputNewkaryawan == '1':
            daftarKaryawan()
            while True:
                inputNip1 = (input("\n Masukkan Nomer Induk Pegawai (NIP) : "))
                if inputNip1.isnumeric() == True:
                    inputNip = int(inputNip1)
                    for i in range(len(dataKaryawan)):
                        if inputNip == dataKaryawan [i]['NIP']:
                            print('''
                                 *** Data yang anda tambahkan sudah terdaftar ***\n
                                     Silahkan masukkan data yang lain
                                     --------------------------------- ''')
                            addKaryawan()
                        elif (i == len(dataKaryawan)-1) and (i != dataKaryawan[i]['NIP']):
                            namaKaryawan = input(' Nama : ').title()
                            jabatanKaryawan = input(' Jabatan : ').title()
                            divisiKaryawan = input(' Divisi : ').title()
                            masaKerja = input(' Masa Kerja = ').title()
                            break
                    while True:
                        newData = input('''
                            Apakah data yang anda masukkan sudah benar(Y/T) :  ''').upper()
                        if newData == 'Y':
                            dataKaryawan.append({
                                'NIP' : inputNip,
                                'Nama' : namaKaryawan,
                                'Jabatan' : jabatanKaryawan,
                                'Divisi' : divisiKaryawan,
                                'Masa Kerja' : masaKerja
                                })
                            daftarKaryawan()
                            print('\n\t\t\t         ---- Data Karyawan telah berhasil ditambahkan ----')
                            addKaryawan()
                            continue
                        elif newData == 'T':
                            print('\n\t\t\t         *** Tidak jadi menambahkan data karyawan ***')
                            addKaryawan()
                        else :
                            print('''\n
                            *** Pilihan yang anda masukkan salah *** \n
                            ------------------------------------------                     
                            Silahkan masukkan pilihan (Y/T) \n''')
                else:
                    print("\n***NIP harus berupa angka, silahkan ketikkan NIP yang benar***\n")
        elif inputNewkaryawan == '2':
            menuAwal()
        else:
            print('\n*** Pilihan yang anda masukan salah *** \nMohon masukkan pilihan sesuai dengan menu di atas [1-2] \n')

# update data karyawan
def changeKaryawan():
    while True:
        updateData = input('''
+==============================+
| Menu Perubahan Data Karyawan |
+==============================+
|                              |
| 1. Update data karyawan      |
| 2. Kembali ke menu utama     |
-------------------------------- 
Silahkan pilih daftar di atas [1-2] : ''')  
        if updateData == '1':
            daftarKaryawan()
            while True :
                inputNip1 = (input('\nMasukkan Nomor Induk Pegawai (NIP) : '))
                if inputNip1.isnumeric()== True:
                    inputNip = int(inputNip1)
                    for i in range(len(dataKaryawan)):
                        if inputNip == dataKaryawan[i]['NIP']:
                            print("\t\t-------------------------------------------------------------------------------------------")
                            print("\t\t| No  |    NIP   |        Nama        |   Jabatan    |      Divisi    |     Masa Kerja    |")
                            print("\t\t+-----+----------+--------------------+--------------+----------------+-------------------+")
                            print(f'''\t\t|{i+1:^5}|{dataKaryawan[i]['NIP']:^10}|{dataKaryawan[i]['Nama']:^20}|{dataKaryawan[i]['Jabatan']:^14}|{dataKaryawan[i]['Divisi']:^16}|{dataKaryawan[i]['Masa Kerja']:^19}|''')
                            print("\t\t+-----+----------+--------------------+--------------+----------------+-------------------+")
                            while True:
                                newData = input('Apakah data yang anda masukkan sudah benar(Y/T) :  ').upper()
                                if newData == 'Y':
                                    while True:
                                        ubahData = (input('\n1.NIP\n\2.Nama\n3.Jabatan\n4.Divisi\n5.Masa Kerja\nPilih kategori yang ingin di ubah : '))
                                        if ubahData.isnumeric() == True:
                                            if ubahData == '1' :
                                                ubahData = 'NIP'
                                            elif ubahData =='2':
                                                ubahData = 'Nama'
                                            elif ubahData == '3':
                                                ubahData = 'Jabatan'
                                            elif ubahData == '4':
                                                ubahData = 'Divisi'
                                            else:
                                                ubahData = 'Masa Kerja'
                                            ubahData1 = input(f'Masukkan {ubahData} baru : ').title()
                                            while True:
                                                newData = input('''
                                            Apakah data yang anda masukkan sudah benar (Y/T) : ''').upper()
                                                if newData == 'Y':
                                                    dataKaryawan[i][ubahData]= ubahData1
                                                    daftarKaryawan()
                                                    print('\n\t\t\t         ---- Data baru anda sudah tersimpan ----')
                                                    changeKaryawan()
                                                elif newData == 'T':
                                                    print('\n\t\t\t                    ***Anda tidak jadi menambahkan data***')
                                                    changeKaryawan()
                                                else:
                                                    print(''' \n
                                                    *** Pilihan yang anda masukkan salah *** \n
                                                    ------------------------------------------                     
                                                    Silahkan masukkan pilihan (Y/T) \n''')

                                        else:
                                            print("\n*** Anda memasukan pilihan yang salah ***")
                                elif newData =='T':
                                    changeKaryawan()
                                else:
                                    print(''' \n
                                     *** Pilihan yang anda masukkan salah *** \n
                                    ------------------------------------------                     
                                    Silahkan masukkan pilihan (Y/T) \n''')
                                
                        elif (i == len(dataKaryawan)-1) and (i != dataKaryawan[i]['NIP']):
                            print('\n *** Maaf NIP yang anda masukkan salah***')
                else: 
                    print("\n***NIP harus berupa angka, silahkan ketikkan NIP yang benar***\n")           
        elif updateData == '2':
            menuAwal()
        else:
            print(' *** Pilihan yang anda masukan salah *** \nMohon masukkan pilihan sesuai dengan menu di atas [1-2] ')

def delKaryawan():
    while True:
        delData = input('''
 +======================================+
 |       Menu Hapus Data Karyawan       |
 +======================================+
 |                                      |
 | 1. Hapus data karyawan               | 
 | 2. Kembali ke menu utama             |
 +--------------------------------------+   
Silahkan pilih daftar di atas [1-2] : ''')
        if delData == '1':
            daftarKaryawan()
            inputNip1 = (input('\nMasukkan Nomor Induk Pegawai (NIP) : '))
            if inputNip1.isnumeric()== True:
                inputNip =int(inputNip1)
                for i in range(len(dataKaryawan)):
                    if inputNip == dataKaryawan[i]['NIP']:
                        print("\t\t-------------------------------------------------------------------------------------------")
                        print("\t\t| No  |    NIP   |        Nama        |   Jabatan    |      Divisi    |     Masa Kerja    |")
                        print("\t\t+-----+----------+--------------------+--------------+----------------+-------------------+")
                        print(f'''\t\t{i+1:^5}|{dataKaryawan[i]['NIP']:^10}| {dataKaryawan[i]['Nama']:20}|{dataKaryawan[i]['Jabatan']:14}|{dataKaryawan[i]['Divisi']:16}|{dataKaryawan[i]['Masa Kerja']:19}''')
                        print("\t\t|-----+----------+--------------------+--------------+----------------+-------------------|")
                        while True :
                            newData = input('''Apakah data yang anda masukkan sudah benar(Y/T) :  ''').capitalize()
                            if newData == 'Y':
                                del dataKaryawan[i]
                                daftarKaryawan()
                                print('         \t\t\t----Data karyawan berhasil di hapus ----')
                                delKaryawan()
                            elif newData == 'T':
                                delKaryawan()
                            else:
                                print('''\n
                                    *** Pilihan yang anda masukkan salah *** \n
                                    ------------------------------------------                     
                                    Silahkan masukkan pilihan benar (Y/T) \n''')
                    elif (i==len(dataKaryawan)-1) and (inputNip != dataKaryawan[i]['NIP']) :
                        print('\n*** Data yang anda masukkan tidak tedaftar ***')
                        delKaryawan()
            else:
                print("\n***NIP harus berupa angka, silahkan ketikkan NIP yang benar***\n")
        elif delData == '2' :
            menuAwal()
        else: 
            print(' \n*** Pilihan yang anda masukkan salah ***\nMohon masukkan pilihan sesuai dengan menu di atas [1-2] ')

# Menampilkan Menu Awal 

def menuAwal():
    print('''
 +=================================================+
 |           Data Karyawan PT.Nusa Dua             |
 +=================================================+           
 
 Berikut daftar pilihan menu yang dapat anda gunakan
 ----------------------------------------------------
    1. Melihat Daftar Karyawan
    2. Menambahkan Data Karyawan
    3. Mengubah Data Karyawan
    4. Menghapus Data Karyawan
    5. Keluar dari program''')

    while True:
        daftarMenu = input('\n Silahkan pilih daftar yang diatas [1-5] : ')
        if daftarMenu == '1':
            reportKaryawan()
        elif daftarMenu == '2':
            addKaryawan()
        elif daftarMenu == '3':
            changeKaryawan()
        elif daftarMenu == '4':
            delKaryawan()
        elif daftarMenu == '5':
            print('''\n--- Terima kasih telah menggunakan program data karyawan PT.Nusa Dua ---\n\n''')
            exit()
        else:
            print("\n*** Maaf yang anda masukkan salah, mohon masukkan sesuai dengan menu diatas [1-5] ***")
menuAwal()
