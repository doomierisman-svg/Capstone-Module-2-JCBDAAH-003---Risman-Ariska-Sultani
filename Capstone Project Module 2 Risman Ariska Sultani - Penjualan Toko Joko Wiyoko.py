# Capstone Project Module 2 Purwadhika: Penjualan Toko Joko Wiyoko



# List of Dictionary penjualan 

sales = [
    {"sale_id": "S001", "date": "2025-08-25", "total": 12500},                      #data penjualan per transaksi
    {"sale_id": "S002", "date": "2025-08-26", "total": 32000},
    {"sale_id": "S003", "date": "2025-08-26", "total": 9500},
    {"sale_id": "S004", "date": "2025-08-27", "total": 29000},
    {"sale_id": "S005", "date": "2025-08-27", "total": 15500}
]

# List of Dictionary Barang (Terdiri dari Sale ID, Produk id, harga produk, stok)

sale_items = [                                                                                      #detail setiap transaksi
    # Transaksi S001
    {"sale_id": "S001", "product_id": "101", "qty": 5, "price": 500, "subtotal": 2500},
    {"sale_id": "S001", "product_id": "201", "qty": 3, "price": 1500, "subtotal": 4500},
    {"sale_id": "S001", "product_id": "301", "qty": 2, "price": 1000, "subtotal": 2000},
    {"sale_id": "S001", "product_id": "401", "qty": 1, "price": 2500, "subtotal": 2500},
    {"sale_id": "S001", "product_id": "105", "qty": 1, "price": 1000, "subtotal": 1000},

    # Transaksi S002
    {"sale_id": "S002", "product_id": "502", "qty": 2, "price": 12000, "subtotal": 24000},
    {"sale_id": "S002", "product_id": "402", "qty": 2, "price": 3000, "subtotal": 6000},
    {"sale_id": "S002", "product_id": "301", "qty": 2, "price": 1000, "subtotal": 2000},

    # Transaksi S003
    {"sale_id": "S003", "product_id": "105", "qty": 3, "price": 1000, "subtotal": 3000},
    {"sale_id": "S003", "product_id": "205", "qty": 2, "price": 2000, "subtotal": 4000},
    {"sale_id": "S003", "product_id": "401", "qty": 1, "price": 2500, "subtotal": 2500},

    # Transaksi S004
    {"sale_id": "S004", "product_id": "503", "qty": 2, "price": 8000, "subtotal": 16000},
    {"sale_id": "S004", "product_id": "104", "qty": 3, "price": 2000, "subtotal": 6000},
    {"sale_id": "S004", "product_id": "304", "qty": 2, "price": 2000, "subtotal": 4000},
    {"sale_id": "S004", "product_id": "404", "qty": 1, "price": 3000, "subtotal": 3000},

    # Transaksi S005
    {"sale_id": "S005", "product_id": "305", "qty": 2, "price": 2000, "subtotal": 4000},
    {"sale_id": "S005", "product_id": "203", "qty": 3, "price": 1500, "subtotal": 4500},
    {"sale_id": "S005", "product_id": "103", "qty": 2, "price": 2000, "subtotal": 4000},
    {"sale_id": "S005", "product_id": "405", "qty": 1, "price": 3000, "subtotal": 3000}
]


# Menu Utama                                        #def untuk memanggil fungsi
def display_menu():                                     
    print("\nMenu Penjualan Toko Joko Wiyoko:")
    print("1. Lihat data penjualan")
    print("2. Tambah data Penjualan")
    print("3. Hapus data Penjualan")
    print("4. Ubah harga Penjualan")



# soal1. Lihat data penjualan, 

def lihat_data():
    print("\nRead Menu (View Data)")
    print("1. Lihat data transaksi Keseluruhan")
    print("2. Lihat Detail Transaksi")
    print("0. Kembali ke Menu Utama")

    pilihan = input("Pilih menu (1/2/0): ")

    if pilihan == "1":
        # 1.1 tampilkan semua transaksi (sale_id)
        if len(sales) > 0:          #untuk tahu ada transaksi atau tidak
            print("\n=== Semua Data Transaksi ===")
            for sale in sales:
                print(f"Sale ID: {sale['sale_id']} | date: {sale['date']} | Total: {sale['total']}")
        else:
            print("Data Tidak ada")

    elif pilihan == "2":
        # 1.2 lihat detail transaksi berdasarkan sale_id
        sale_id = input("Masukkan Sale ID : ").upper()

        detail_items = [i for i in sale_items if i["sale_id"] == sale_id]  #list comprehension

        if detail_items:
            # tampilkan detail transaksi
            print(f"\n=== Detail Transaksi {sale_id} ===")
            for item in detail_items:
                print(f"Produk ID: {item['product_id']} | Qty: {item['qty']} | "  
                      f"Harga: {item['price']} | Subtotal: {item['subtotal']}")
            
            # ambil total dari sales
            total = 0           #default number
            for s in sales:                 
             if s['sale_id'] == sale_id:            
                 total = s['total']
                 break

            print(f"Total Transaksi: {total}")

        else:
            print(f" Data untuk Sale ID {sale_id} tidak ada (kembali ke menu utama)")

    elif pilihan == "0":
        return  # balik ke menu utama

    else:
        print("Pilihan tidak valid, kembali ke menu utama")



#soal2. Tambah data Penjualan 

def tambah_data():
    while True:
        print("\nCreate Menu (Tambah Data)")
        print("1. Tambah Data Penjualan")
        print("0. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1/0): ")

        if pilihan == "1":
            print("\n=== Tambah Data Penjualan ===")
            sale_id = input("Masukkan Sale ID: ").upper()

            # cari apakah sale_id sudah ada di data
            sale = None
            for s in sales:
                if s["sale_id"] == sale_id:
                    sale = s
                    break
              
            if not sale:  # apabila transaksi belum ada
                date = input("Masukkan Tanggal (YYYY-MM-DD): ")
                sale = {"sale_id": sale_id, "date": date, "total": 0}
                sales.append(sale)

            product_id = input("Masukkan Product ID: ")

            # cek duplikat pada sale_items
            for item in sale_items:
                if item["sale_id"] == sale_id and item["product_id"] == product_id:
                    print(f"Produk sudah ada di transaksi ini -> {product_id}")
                    return  # hentikan tambah_data

            qty = int(input("Masukkan Quantity: "))
            price = int(input("Masukkan Harga Produk: "))
            subtotal = qty * price

            # preview sebelum simpan
            print("\n=== Preview Data Sebelum Disimpan ===")
            print(f"Sale ID : {sale_id}")
            print(f"Produk  : {product_id}")
            print(f"Qty     : {qty}")
            print(f"Harga   : {price}")
            print(f"Subtotal: {subtotal}")

            # konfirmasi sebelum simpan
            konfirmasitambah = input("Simpan data? (y/n): ").lower()
            if konfirmasitambah == "y":
                sale_items.append({
                    "sale_id": sale_id,
                    "product_id": product_id,
                    "qty": qty,
                    "price": price,
                    "subtotal": subtotal
                })
                sale["total"] = sum(i["subtotal"] for i in sale_items if i["sale_id"] == sale_id)
                print("Data tersimpan")
                print(f"Total baru transaksi {sale_id}: {sale['total']}")
            else:
                print("Data tidak disimpan, kembali ke menu utama.")

        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

    

#soal3. Hapus Data Penjualan
def hapus_data():
    print("\nDelete Menu (Hapus Data)")
    print("1. Hapus Transaksi")
    print("2. Hapus Item di satu Transaksi")
    print("0. Kembali ke Menu Utama")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        # Hapus seluruh transaksi
        sale_id = input("Masukkan Sale ID: ").upper()

        transaksi = None  # default 
        for s in sales:
            if s["sale_id"] == sale_id:
                transaksi = s
                break

        if not transaksi:
            print("Data tidak ada")
            return

        # tampilkan detail transaksi
        print(f"\n=== Detail Transaksi {sale_id} ===")
        for item in [i for i in sale_items if i["sale_id"] == sale_id]: #comprehension list
            print(f" Product ID: {item['product_id']} | Qty: {item['qty']} | "
                 f"Harga: {item['price']} | Subtotal: {item['subtotal']}")
        print(f"Total: {transaksi['total']}")

        konfirmasi = input("Apakah anda yakin ingin menghapus transaksi ini? (y/n): ").lower()
        if konfirmasi == "y":
            # hapus data
            sales.remove(transaksi) #fungsi menghapus
            sale_items[:] = [i for i in sale_items if i["sale_id"] != sale_id] #fungsinya untuk mengganti seluruh isi list, tanpa mengubah reference (dictionary) SN
            print("Transaksi berhasil dihapus") #notif
        else:
            print("Penghapusan dibatalkan")

    elif pilihan == "2":
        # Hapus item di transaksi 
        sale_id = input("Masukkan Sale ID: ")
        
        transaksi = None  # default kalau tidak ketemu

        for s in sales:
            if s["sale_id"] == sale_id:
                transaksi = s
                break 

        if not transaksi:
            print("Data tidak ada")
            return

        # tampilkan semua item
        print(f"\n=== Detail Transaksi {sale_id} ===")
        for item in [i for i in sale_items if i["sale_id"] == sale_id]:
           print(f" Product ID: {item['product_id']} | Qty: {item['qty']} | "
                 f"Harga: {item['price']} | Subtotal: {item['subtotal']}")
        print(f"Total: {transaksi['total']}")

        product_id = input("Masukkan Product ID yang ingin dihapus: ")

        item = None
        for i in sale_items:
            if i["sale_id"] == sale_id and i["product_id"] == product_id:
                item = i
                break


        if not item:
            print("Produk tidak ada dalam transaksi")
            return

        qty_hapus = int(input(f"Masukkan Quantity yang ingin dihapus (Qty sekarang {item['qty']}): "))

        #konfirmasi sebelum hapus
        if qty_hapus >= item["qty"]:
            konfirmasi = input(f"Apakah anda yakin ingin menghapus {product_id} sepenuhnya? (y/n): ").lower() #noitifkasi konfirmasi
            if konfirmasi == "y":
                sale_items.remove(item) #fungsi menghapus
                print("Item berhasil dihapus")
            else:
                print("Penghapusan dibatalkan")
        else:
            konfirmasi = input(f"Apakah anda yakin ingin menghapus {qty_hapus} dari {item['qty']} {product_id}? (y/n): ").lower()
            if konfirmasi == "y":
                item["qty"] -= qty_hapus
                item["subtotal"] = item["qty"] * item["price"]
                print("Item berhasil dikurangi")
            else:
                print("Penghapusan dibatalkan")

        # update total transaksi
        transaksi["total"] = sum(i["subtotal"] for i in sale_items if i["sale_id"] == sale_id) 
        print(f"Total baru transaksi {sale_id}: {transaksi['total']}")

    elif pilihan == "0":
        print("Kembali ke Menu Utama")
        return #balek
    else:
        print("Pilihan tidak valid, kembali ke menu utama")
    


#soal4. Ubah Data Penjualan
def update_transaksi():
    print("\nUpdate Menu (Ubah Data)")
    print("1. Ubah Data Penjualan")
    print("0. Kembali ke Menu Utama")

    pilihan = input("Pilih menu1/0: ")

    if pilihan == "1":
        sale_id = input("Masukkan Sale ID: ").upper() 
       
        transaksi = None
        for s in sales:
            if s["sale_id"] == sale_id:
                transaksi = s
                break

        if not transaksi:
            print(" Data tidak ada")
            return

        #  detail transaksi
        print(f"\n=== Detail Transaksi {sale_id} ===")
        items = [i for i in sale_items if i["sale_id"] == sale_id]          #comprehension list
        for item in items:
            print(f" Product ID: {item['product_id']} | Qty: {item['qty']} |"
                 f"Harga: {item['price']} | Subtotal: {item['subtotal']}")
        print(f"Total: {transaksi['total']}")

        product_id = input("Masukkan Product ID yang ingin diubah: ")

        item = None
        for i in sale_items:
            if i["sale_id"] == sale_id and i["product_id"] == product_id:
                item = i
                break

        if not item:
            print("Produk tidak ada dalam transaksi")
            return

        qty_baru = int(input(f"Masukkan Quantity baru (Qty lama {item['qty']}): "))
        
        subtotal_baru = qty_baru * item["price"]
        
        # preview sebelum simpan
        print("\n=== Preview Data Setelah Perubahan ===")
        print(f"Produk : {product_id}")
        print(f"Qty Lama : {item['qty']} -> Qty Baru : {qty_baru}")
        print(f"Harga : {item['price']}")
        print(f"Subtotal Lama : {item['subtotal']} -> Subtotal Baru : {subtotal_baru}")

        #konfirmasi sebelum ubah
        konfirmasi = input("Apakah anda yakin ingin mengubah data ini? (y/n): ").lower()        #notifikasi konfirmasi
        if konfirmasi == "y":
            item["qty"] = qty_baru
            item["subtotal"] = subtotal_baru

            # update total transaksi
            transaksi["total"] = sum(i["subtotal"] for i in sale_items if i["sale_id"] == sale_id) #generator expression 
            print("Data berhasil diubah")
            print(f"Total baru transaksi {sale_id}: {transaksi['total']}")
        else:
            print("Perubahan dibatalkan")

    elif pilihan == "0":
        print("Kembali ke Menu Utama")
        return 
    else:
        print("Pilihan tidak valid, kembali ke menu utama")

     
def menuutama():
    while True:                                 #loop terus selama program digunakan user
        display_menu()        
        pilihan =input("Pilih Menu 1-4: ")
        
        if pilihan == "1":
            lihat_data()
                  
        elif pilihan == "2":
            tambah_data()
        
        elif pilihan == "3":
            hapus_data()
        
        elif pilihan == "4":
            update_transaksi()
            
        else:
            print("Pilihan tidak valid, mohon memilih angka 1-4")

menuutama()

#######################################################################################################################################################################################################################