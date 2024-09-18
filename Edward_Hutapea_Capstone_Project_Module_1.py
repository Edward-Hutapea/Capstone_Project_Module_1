from tabulate import tabulate

headers = ['No', 'No. Registrasi', 'Nama Pasien', 'Umur', 'Jenis Kelamin', 'Dokter', 'Poli']
data = {
    'No. Registrasi' : [101, 102],
    'Nama' : ['Chandra', 'Nova'],
    'Umur' : [25, 7], 
    'Jenis Kelamin' : ['Laki-laki', 'Perempuan'], 
    'Poli' : ['Mata', 'Anak'],
    'Dokter' : ['Ponco', 'Umar']
}


## MAIN MENU ## MAIN MENU ## MAIN MENU ## MAIN MENU ## MAIN MENU ## MAIN MENU ## MAIN MENU ##
## MAIN MENU ## MAIN MENU ## MAIN MENU ## MAIN MENU ## MAIN MENU ## MAIN MENU ## MAIN MENU ##


def MAIN_MENU():
    print()
    print("== DAFTAR MENU LAYANAN DATA PASIEN DI RUMAH SAKIT PURWADHIKA ==")
    headers = ['No', 'Menu']
    MENU_utama = [
        ['1','Melihat data pasien'],
        ['2','Menambah data pasien'],
        ['3','Merubah data pasien'],
        ['4','Menghapus data pasien'],
        ['5','Exit']
    ]
    print(tabulate(MENU_utama, headers, tablefmt='fancy_grid'))
    global MENU_utama_input
    MENU_utama_input = input("Masukkan nomor menu [1-5] : ")

## MAIN MENU ## INPUT DATA INVALID (Bukan angka 1, 2 atau 3)

def MAIN_MENU_invalid():
    print("Nomor menu salah. Silahkan ulang kembali.")
    MAIN_MENU()


## READ MENU ## READ MENU ## READ MENU ## READ MENU ## READ MENU ## READ MENU ## READ MENU ## 
## READ MENU ## READ MENU ## READ MENU ## READ MENU ## READ MENU ## READ MENU ## READ MENU ## 

def READ():

    ## READ MENU ## MENAMPILKAN SUB MENU READ

    def READ_data():
        print("== MELIHAT DATA PASIEN ==")
        headers = ['No', 'Opsi']
        READ_menu = [
            ['1','Melihat data seluruh pasien'],
            ['2','Melihat data pasien tertentu'],
            ['3','Kembali ke menu utama'],
        ]
        print(tabulate(READ_menu, headers, tablefmt='fancy_grid'))
        global READ_input
        READ_input = input("Silakan Pilih Sub Menu Lihat Data [1-3] : ")

    ## READ MENU ## UNTUK BACA SEMUA DATA

    def READ_data_semua():
        print()
        print("== DATA PASIEN DI RUMAH SAKIT PURWADHIKA ==")
        print(tabulate(data, headers=data.keys(), tablefmt='fancy_grid'))
        print()

    ## READ MENU ## UNTUK BACA DATA PILIHAN BERDASARKAN NOMOR REGISTRASI

    def READ_input_noreg():
        print()
        global READ_noreg
        READ_noreg = int(input("Masukkan nomor registrasi pasien : "))

    ## READ MENU ## UNTUK BACA DATA PILIHAN BERDASARKAN NAMA

    def READ_input_nama():
        print()
        global READ_nama
        READ_nama = input("Masukkan nama pasien : ")

    ## READ MENU ## TANYA INFORMASI (KEY PARAMATER) YANG DIMILIKI

    def READ_tanya_parameter():
        print()
        print("INPUT DATA PASIEN")
        headers = ['No', 'Data Pasien']
        READ_parameter = [
            ['1','Nomor registrasi pasien'],
            ['2','Nama pasien'],
        ]
        print(tabulate(READ_parameter, headers, tablefmt='fancy_grid'))
        global READ_parameter_cek
        READ_parameter_cek = input("Silakan pilih informasi data pasien yang anda punya [1-2] : ")

    ## READ MENU ## JIKA INPUT NOMOR REGISTRASI TIDAK TERSEDIA

    def READ_noreg_invalid():
        print("Data tidak ada. Silahkan pilih nomor registrasi di bawah ini :")
        for c in data['No. Registrasi']:
            print(c, end=", ")
        print()
        READ_input_noreg()

    ## READ MENU ## JIKA INPUT NAMA TIDAK TERSEDIA

    def READ_nama_invalid():
        print("Data tidak ada. Silahkan pilih nama di bawah ini :")
        for f in data['Nama']:
            print(f, end=", ")
        print()
        READ_input_nama()

    ## READ MENU ## TAMPILKAN DATA YANG DIPILIH BERDASARKAN NOMOR REGISTRASI

    def READ_pilihan_noreg():
        READ_dibaca_noreg = {
            'No. Registrasi' : [],
            'Nama' : [],
            'Umur' : [], 
            'Jenis Kelamin' : [], 
            'Poli' : [],
            'Dokter' : []
            }
    
        READ_dibaca_noreg['No. Registrasi'].append(data['No. Registrasi'][b])
        READ_dibaca_noreg['Nama'].append(data['Nama'][b])
        READ_dibaca_noreg['Umur'].append(data['Umur'][b])
        READ_dibaca_noreg['Jenis Kelamin'].append(data['Jenis Kelamin'][b])
        READ_dibaca_noreg['Poli'].append(data['Poli'][b])
        READ_dibaca_noreg['Dokter'].append(data['Dokter'][b])
    
        print()
        print("DATA PASIEN YANG DIPILIH")
        print(tabulate(READ_dibaca_noreg, headers=data.keys(), tablefmt='fancy_grid'))

    ## READ MENU ## TAMPILKAN DATA YANG DIPILIH BERDASARKAN NAMA

    def READ_pilihan_nama():
        READ_dibaca_nama = {
            'No. Registrasi' : [],
            'Nama' : [],
            'Umur' : [], 
            'Jenis Kelamin' : [], 
            'Poli' : [],
            'Dokter' : []
            }
    
        READ_dibaca_nama['No. Registrasi'].append(data['No. Registrasi'][d])
        READ_dibaca_nama['Nama'].append(data['Nama'][d])
        READ_dibaca_nama['Umur'].append(data['Umur'][d])
        READ_dibaca_nama['Jenis Kelamin'].append(data['Jenis Kelamin'][d])
        READ_dibaca_nama['Poli'].append(data['Poli'][d])
        READ_dibaca_nama['Dokter'].append(data['Dokter'][d])
    
        print()
        print("DATA PASIEN YANG DIPILIH")
        print(tabulate(READ_dibaca_nama, headers=data.keys(), tablefmt='fancy_grid'))

    ## READ MENU ## JIKA INPUT NOMOR REGISTRASI TERSEDIA

    def READ_noreg_valid():
        global a
        global b
        for a in data['No. Registrasi']:
            if a == READ_noreg:
                b = data['No. Registrasi'].index(a)
                READ_pilihan_noreg()

    ## READ MENU ## JIKA INPUT NAMA TERSEDIA

    def READ_nama_valid():
        global c
        global d
        for c in data['Nama']:
            if c == READ_nama.title():
                d = data['Nama'].index(c)
                READ_pilihan_nama()

    ## READ MENU ## MEMILIH MEMBACA DATA

    def READ_dipilih():
        READ_data()
                
        while not READ_input.isdigit():
            print()
            READ_data()

        while int(READ_input) not in range(1,4):
            print()
            READ_data()
            
            while not READ_input.isdigit():
                print()
                READ_data()
        
        if int(READ_input) == 3:
            MAIN_MENU()

        while int(READ_input) != 3:

            if len(data['Nama']) == 0:
                print("Tidak ada data siapapun di dalam Database Pasien. Kembali ke sub menu baca data")
                print()
                READ_data()
            
            else:
                if  int(READ_input) == 1:
                    READ_data_semua()
            
                if  int(READ_input) == 2:
                    READ_tanya_parameter()
                    
                    while not READ_parameter_cek.isdigit():
                        READ_tanya_parameter()
                    
                    while int(READ_parameter_cek) not in range(1,3):
                        READ_tanya_parameter()
                        
                        while not READ_parameter_cek.isdigit():
                            READ_tanya_parameter()

                    if int(READ_parameter_cek) == 1:
                        READ_input_noreg()
                        while READ_noreg not in data['No. Registrasi']:
                            READ_noreg_invalid()
                        if READ_noreg in data['No. Registrasi']:
                            READ_noreg_valid()
                    if int(READ_parameter_cek) == 2:
                        READ_input_nama()
                        while READ_nama.title() not in data['Nama']:
                            READ_nama_invalid()
                        if READ_nama.title() in data['Nama']:
                            READ_nama_valid()

                    print()
                READ_data()
    
            while not READ_input.isdigit():
                print()
                READ_data()

            while int(READ_input) not in range(1,4):
                print()
                READ_data()
            
                while not READ_input.isdigit():
                    print()
                    READ_data()
            
            if int(READ_input) == 3:
                MAIN_MENU()

    READ_dipilih()

## CREATE MENU ## CREATE MENU ## CREATE MENU ## CREATE MENU ## CREATE MENU ## CREATE MENU ## 
## CREATE MENU ## CREATE MENU ## CREATE MENU ## CREATE MENU ## CREATE MENU ## CREATE MENU ## 

def CREATE():

    ## CREATE MENU ## APAKAH MAU TAMBAH DATA ?

    def CREATE_data():

        print("== MENAMBAH DATA PASIEN ==")
        headers = ['No', 'Sub Menu']
        CREATE_menu = [
            ['1','Tambah data pasien'],
            ['2','Kembali ke menu utama']
        ]
        print(tabulate(CREATE_menu, headers, tablefmt='fancy_grid'))

        global CREATE_input
        CREATE_input = input("Silakan Pilih Sub Menu Tambah Data [1-2] : ")

    ## CREATE MENU ## INPUT DATA TAMBAHAN

    def CREATE_input_data():
        # global CREATE_noreg
        global CREATE_nama
        global CREATE_umur
        global CREATE_jeniskelamin
        global CREATE_poli
        global CREATE_dokter
    
    ## CREATE_noreg = input("Masukkan nomor registrasi pasien: ")
        CREATE_nama = input("Masukkan nama pasien : ")
        CREATE_umur = input("Masukkan umur pasien: ")
        CREATE_jeniskelamin = input("Masukkan jenis kelamin pasien [ketik L untuk Laki-laki atau ketik P untuk perempuan]: ")
        CREATE_poli = input("Masukkan nama poli : ")
        CREATE_dokter = input("Masukkan nama dokter : ")

    ## CREATE MENU ## DRAFT DATA TAMBAHAN 

    def CREATE_cek_data():
        CREATE_draft_data = {
            'No. Registrasi' : [],
            'Nama' : [],
            'Umur' : [], 
            'Jenis Kelamin' : [], 
            'Poli' : [],
            'Dokter' : []
            }
    
        CREATE_draft_data['No. Registrasi'].extend([CREATE_noreg])
        CREATE_draft_data['Nama'].extend([CREATE_nama.title()])
        CREATE_draft_data['Umur'].extend([CREATE_umur])
        if CREATE_jeniskelamin.upper() == "L":
            CREATE_draft_data['Jenis Kelamin'].extend(["Laki-laki"])
        if CREATE_jeniskelamin.upper() == "P":
            CREATE_draft_data['Jenis Kelamin'].extend(["Perempuan"])
        CREATE_draft_data['Poli'].extend([CREATE_poli.title()])
        CREATE_draft_data['Dokter'].extend([CREATE_dokter.title()])
    
        print()
        print("Data yang telah anda tambahkan : ")
        print(tabulate(CREATE_draft_data, headers=data.keys(), tablefmt='fancy_grid'))

    ## CREATE MENU ## MASUKKAN DATA TAMBAHAN KE EXISTING DATA 

    def CREATE_simpan_data():
        data['No. Registrasi'].extend([CREATE_noreg])
        data['Nama'].extend([CREATE_nama.title()])
        data['Umur'].extend([CREATE_umur])
        if CREATE_jeniskelamin.upper() == "L":
            data['Jenis Kelamin'].extend(["Laki-laki"])
        if CREATE_jeniskelamin.upper() == "P":
            data['Jenis Kelamin'].extend(["Perempuan"])
        data['Poli'].extend([CREATE_poli.title()])
        data['Dokter'].extend([CREATE_dokter.title()])
    
        print("Data tambahan telah disimpan.")
        print()
        print("DATA PASIEN TERKINI")
        print(tabulate(data, headers=data.keys(), tablefmt='fancy_grid'))

    ## CREATE MENU ## TAMBAH DATA

    def CREATE_input_noreg():
        global CREATE_noreg
        print()
        CREATE_noreg = int(input("Masukkan nomor registrasi pasien : "))

    ## CREATE MENU ## SEANDAINYA DUPLICATE NOMOR REGISTRASI

    def CREATE_data_invalid():
        print("Data sudah ada. Silahkan ketik selain nomor registrasi di bawah ini :")
        for k in data['No. Registrasi']:
            print(k, end=", ")
        print()
        CREATE_input_noreg()

    ## CREATE MENU ## MEMILIH MENAMBAH DATA

    def CREATE_dipilih():
        CREATE_data()
                
        while not CREATE_input.isdigit():
            print()
            CREATE_data()

        if int(CREATE_input) == 2:
            MAIN_MENU()

        while int(CREATE_input) == 1:
            CREATE_input_noreg()

            while CREATE_noreg in data['No. Registrasi']:
                CREATE_data_invalid()
            if CREATE_noreg not in data['No. Registrasi']:
                CREATE_input_data()
    
            CREATE_cek_data()
            CREATE_konfirmasi = input("Apakah data tambahan akan anda simpan? [Y/N] : ")
    
            if CREATE_konfirmasi.upper() == 'Y':
                CREATE_simpan_data()
            else:
                print("Data tidak disimpan. Kembali ke sub menu tambah data")
    
            print()
            CREATE_data()

            while not CREATE_input.isdigit():
                print()
                CREATE_data()

            if int(CREATE_input) == 2:
                MAIN_MENU()

    CREATE_dipilih()

## UPDATE MENU ## UPDATE MENU ## UPDATE MENU ## UPDATE MENU ## UPDATE MENU ## UPDATE MENU ##
## UPDATE MENU ## UPDATE MENU ## UPDATE MENU ## UPDATE MENU ## UPDATE MENU ## UPDATE MENU ##

def UPDATE():

    ## UPDATE MENU # APAKAH MAU UDPADE DATA

    def UPDATE_data():

        print("== MENGUBAH DATA PASIEN ==")
        headers = ['No', 'Sub Menu']
        UPDATE_menu = [
            ['1','Ubah data pasien'],
            ['2','Kembali ke menu utama']
        ]
        print(tabulate(UPDATE_menu, headers, tablefmt='fancy_grid'))

        global UPDATE_input
        UPDATE_input = input("Silakan Pilih Sub Menu Ubah Data [1-2] : ")

    ## UPDATE MENU # HAPUS DATA PILIHAN

    def UPDATE_input_data():
        global UPDATE_noreg
        print()
        UPDATE_noreg = int(input("Masukkan nomor registrasi pasien : "))

    ## UPDATE MENU ## DRAFT DATA YANG MAU DIHAPUS 

    def UPDATE_pilihan_data():
        UPDATE_pilihan = {
            'No. Registrasi' : [],
            'Nama' : [],
            'Umur' : [], 
            'Jenis Kelamin' : [], 
            'Poli' : [],
            'Dokter' : []
            }
    
        UPDATE_pilihan['No. Registrasi'].append(data['No. Registrasi'][y])
        UPDATE_pilihan['Nama'].append(data['Nama'][y])
        UPDATE_pilihan['Umur'].append(data['Umur'][y])
        UPDATE_pilihan['Jenis Kelamin'].append(data['Jenis Kelamin'][y])
        UPDATE_pilihan['Poli'].append(data['Poli'][y])
        UPDATE_pilihan['Dokter'].append(data['Dokter'][y])
    
        print()
        print("DATA YANG INGIN DIUBAH:")
        print(tabulate(UPDATE_pilihan, headers=data.keys(), tablefmt='fancy_grid'))

    ## UPDATE MENU ## KONFIRMASI SEBELUM UPDATE

    def UPDATE_cek_data():
        global x
        global y
        for x in data['No. Registrasi']:
            if x == UPDATE_noreg:
                y = data['No. Registrasi'].index(x)
                UPDATE_pilihan_data()

    ## UPDATE MENU ## PILIH UBAH KOLOM NAMA

    def UPDATE_draft_data_nama():
        UPDATE_nama = input("Masukkan nama baru : ")
        UPDATE_nama_konfirmasi = input("Apakah data akan diubah? [Y/N] : ")
        if UPDATE_nama_konfirmasi.upper() == 'Y':
            data['Nama'][y] = UPDATE_nama.title()
        else:
            print("Data tidak jadi dirubah. Kembali ke sub menu udah data")

    ## UPDATE MENU ## PILIH UBAH KOLOM UMUR

    def UPDATE_draft_data_umur():
        UPDATE_umur = input("Masukkan umur baru : ")
        UPDATE_umur_konfirmasi = input("Apakah data akan diubah? [Y/N] : ")
        if UPDATE_umur_konfirmasi.upper() == 'Y':
            data['Umur'][y] = UPDATE_umur
        else:
            print("Data tidak jadi dirubah. Kembali ke sub menu udah data")

    ## UPDATE MENU ## PILIH UBAH KOLOM JENIS KELAMIN

    def UPDATE_draft_data_kelamin():
        UPDATE_kelamin = input("Masukkan jenis kelamin baru [ketik L untuk Laki-laki atau ketik P untuk perempuan]: ")
        UPDATE_kelamin_konfirmasi = input("Apakah data akan diubah? [Y/N] : ")
        if UPDATE_kelamin_konfirmasi.upper() == 'Y':
            if UPDATE_kelamin.upper() == "L":
                data['Jenis Kelamin'][y] = "Laki-laki"
            elif UPDATE_kelamin.upper() == "P":
                data['Jenis Kelamin'][y] = "Perempuan"
        else:
            print("Data tidak jadi dirubah. Kembali ke sub menu udah data")

    ## UPDATE MENU ## PILIH UBAH KOLOM POLI

    def UPDATE_draft_data_poli():
        UPDATE_poli = input("Masukkan poli baru : ")
        UPDATE_poli_konfirmasi = input("Apakah data akan diubah? [Y/N] : ")
        if UPDATE_poli_konfirmasi.upper() == 'Y':
            data['Poli'][y] = UPDATE_poli.title()
        else:
            print("Data tidak jadi dirubah. Kembali ke sub menu udah data")

    ## UPDATE MENU ## PILIH UBAH KOLOM DOKTER

    def UPDATE_draft_data_dokter():
        UPDATE_dokter = input("Masukkan dokter baru : ")
        UPDATE_dokter_konfirmasi = input("Apakah data akan diubah? [Y/N] : ")
        if UPDATE_dokter_konfirmasi.upper() == 'Y':
            data['Dokter'][y] = UPDATE_dokter.title()
        else:
            print("Data tidak jadi dirubah. Kembali ke sub menu udah data")

    ## UPDATE MENU ## JADI UPDATE DATA

    def UPDATE_data_pilihan():

        print("DATA APA YANG MAU DIUBAH?")
        headers = ['No', 'Data Pasien']
        UPDATE_opsi = [
            ['1','Nama'],
            ['2','Umur'],
            ['3','Jenis Kelamin'],
            ['4','Poli'],
            ['5','Dokter']
        ]
        print(tabulate(UPDATE_opsi, headers, tablefmt='fancy_grid'))
        global input_update
        input_update = input("Silakan pilih keterangan yag mau diubah [1-5] : ")

    ## UPDATE MENU ## PILIH KOLOM/KETERANGAN YANG MAU DIUBAH

    def UPDATE_draft_data():
        if int(input_update) == 1:
            UPDATE_draft_data_nama()
        elif int(input_update) == 2:
            UPDATE_draft_data_umur()
        elif int(input_update) == 3:
            UPDATE_draft_data_kelamin()
        elif int(input_update) == 4:
            UPDATE_draft_data_poli()
        elif int(input_update) == 5:
            UPDATE_draft_data_dokter()

    ## UPDATE MENU ## JIKA DUPLIKAT NOMOR REGISTRASI

    def UPDATE_data_duplikasi():
        print("Data tidak ada. Silahkan pilih nomor registrasi di bawah ini :")
        for k in data['No. Registrasi']:
            print(k, end=", ")
        print()
        UPDATE_input_data()

    ## UPDATE MENU ## MEMILIH MERUBAH DATA

    def UPDATE_dipilih():
        UPDATE_data()
        
        while not UPDATE_input.isdigit():
            print()
            UPDATE_data()
    
        if int(UPDATE_input) == 2:
            MAIN_MENU()

        while int(UPDATE_input) == 1:
    
            if len(data['Nama']) == 0:
                print("Tidak ada data siapapun di dalam Database Pasien. Kembali ke sub menu ubah data")
                print()
                UPDATE_data()
            
            else:
                UPDATE_input_data()

                while UPDATE_noreg not in data['No. Registrasi']:
                    UPDATE_data_duplikasi()
                if UPDATE_noreg in data['No. Registrasi']:
                    UPDATE_cek_data()

                UPDATE_lanjut = input("Tekan Y jika ingin lanjut merubah data atau tekan N jika batal merubah data [Y/N] : ")
                print()

                if UPDATE_lanjut.upper() == 'Y':
                    UPDATE_data_pilihan()

                    while not input_update.isdigit():
                        print()
                        UPDATE_data_pilihan()

                    while int(input_update) not in range(1,6):
                        print()
                        UPDATE_data_pilihan()

                        while not input_update.isdigit():
                            print()
                            UPDATE_data_pilihan()

                    UPDATE_draft_data()
                    print()
                    print("DATA PASIEN TERKINI")
                    print(tabulate(data, headers=data.keys(), tablefmt='fancy_grid'))
                else:
                    print("Data batal dirubah. Kembali ke sub menu udah data")
    
                print()
                UPDATE_data()

            while not UPDATE_input.isdigit():
                print()
                UPDATE_data()

            if int(UPDATE_input) == 2:
                MAIN_MENU()

    UPDATE_dipilih()

## DELETE MENU ## DELETE MENU ## DELETE MENU ## DELETE MENU ## DELETE MENU ## DELETE MENU ##
## DELETE MENU ## DELETE MENU ## DELETE MENU ## DELETE MENU ## DELETE MENU ## DELETE MENU ##

def DELETE():
    
    ## DELETE MENU ## APAKAH MAU DELETE DATA

    def DELETE_data():

        print("== MENGHAPUS DATA PASIEN ==")
        headers = ['No', 'Sub Menu']
        DELETE_menu = [
            ['1','Hapus data pasien'],
            ['2','Kembali ke menu utama']
        ]
        print(tabulate(DELETE_menu, headers, tablefmt='fancy_grid'))

        global DELETE_input
        DELETE_input = input("Silakan Pilih Sub Menu Hapus Data [1-2] : ")

    ## DELETE MENU ## HAPUS DATA PILIHAN

    def DELETE_input_data():
        global DELETE_noreg
        print()
        DELETE_noreg = int(input("Masukkan nomor registrasi pasien : "))

    ## SEANDAINYA INPUT NOMOR REGISTRASI TIDAK TERSEDIA

    def DELETE_data_invalid():
        print("Data tidak ada. Silahkan pilih nomor registrasi di bawah ini :")
        for k in data['No. Registrasi']:
            print(k, end=", ")
        print()
        DELETE_input_data()

    ## DELETE MENU ## DRAFT DATA YANG MAU DIHAPUS 

    def DELETE_draft_data():
        DELETE_draft = {
            'No. Registrasi' : [],
            'Nama' : [],
            'Umur' : [], 
            'Jenis Kelamin' : [], 
            'Poli' : [],
            'Dokter' : []
            }
    
        DELETE_draft['No. Registrasi'].append(data['No. Registrasi'][j])
        DELETE_draft['Nama'].append(data['Nama'][j])
        DELETE_draft['Umur'].append(data['Umur'][j])
        DELETE_draft['Jenis Kelamin'].append(data['Jenis Kelamin'][j])
        DELETE_draft['Poli'].append(data['Poli'][j])
        DELETE_draft['Dokter'].append(data['Dokter'][j])
    
        print()
        print("DATA YANG INGIN DIHAPUS:")
        print(tabulate(DELETE_draft, headers=data.keys(), tablefmt='fancy_grid'))

    ## DELETE MENU ## KONFIRMASI SEBELUM DELETE

    def DELETE_cek_data():
        global i
        global j
        for i in data['No. Registrasi']:
            if i == DELETE_noreg:
                j = data['No. Registrasi'].index(i)
                DELETE_draft_data()

    ## DELETE MENU ## HAPUS PILIHAN DATA EXISTING 

    def DELETE_data_pilihan():
        del data['No. Registrasi'][j]
        del data['Nama'][j]
        del data['Umur'][j]
        del data['Jenis Kelamin'][j]
        del data['Poli'][j]
        del data['Dokter'][j]
    
        print("Data pilihan telah dihapus.")
        print()
        print("DATA PASIEN TERKINI:")
        print(tabulate(data, headers=data.keys(), tablefmt='fancy_grid'))

    ## DELETE MENU ## MEMILIH MENGHAPUS DATA

    def DELETE_dipilih():
        DELETE_data()

        while not DELETE_input.isdigit():
            print()
            DELETE_data()
    
        if int(DELETE_input) == 2:
            MAIN_MENU()

        while int(DELETE_input) == 1:

            if len(data['Nama']) == 0:
                print("Tidak ada data siapapun di dalam Database Pasien. Kembali ke sub menu hapus data")
                print()
                DELETE_data()

            else:
                DELETE_input_data()

                while DELETE_noreg not in data['No. Registrasi']:
                    DELETE_data_invalid()
                if DELETE_noreg in data['No. Registrasi']:
                    DELETE_cek_data()
    
                DELETE_konfirmasi = input("Apakah data ini akan dihapus? [Y/N] : ")
                print()
                if DELETE_konfirmasi.upper() == 'Y':
                    DELETE_data_pilihan()
                else:
                    print("data tidak dihapus")
    
                print()
                DELETE_data()

            while not DELETE_input.isdigit():
                print()
                DELETE_data()
    
            if int(DELETE_input) == 2:
                MAIN_MENU()

    DELETE_dipilih()

## RUNNING PROGRAM ## RUNNING PROGRAM ## RUNNING PROGRAM ## RUNNING PROGRAM ## RUNNING PROGRAM ## 
## RUNNING PROGRAM ## RUNNING PROGRAM ## RUNNING PROGRAM ## RUNNING PROGRAM ## RUNNING PROGRAM ## 


MAIN_MENU()

while not MENU_utama_input.isdigit():
    MAIN_MENU_invalid()

while int(MENU_utama_input) not in range(1,6):
    MAIN_MENU_invalid()

    while not MENU_utama_input.isdigit():
        MAIN_MENU_invalid()

while int(MENU_utama_input) in range(1,5):
    if int(MENU_utama_input) == 1:
        print()
        READ()
    elif  int(MENU_utama_input) == 2:
        print()
        CREATE()
    elif  int(MENU_utama_input) == 3:
        print()
        UPDATE()
    elif  int(MENU_utama_input) == 4:
        print()
        DELETE()
    
    while not MENU_utama_input.isdigit():
        MAIN_MENU_invalid()
    
    while int(MENU_utama_input) not in range(1,6):
        MAIN_MENU_invalid()

        while not MENU_utama_input.isdigit():
            MAIN_MENU_invalid()

if int(MENU_utama_input) == 5:
    print("Terimakasih sudah mengakses layanan kami. Sampai jumpa!")