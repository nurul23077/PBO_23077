# program_kalkulator.py

# Mengimpor fungsi dari modul_kalkulator
from modul_kalkulator import tambah, kurang, kali, bagi

def main():
    print("Selamat datang di program kalkulator!")
    
    while True:
        # Menampilkan menu
        print("\nPilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        
        # Meminta pilihan dari pengguna
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        
        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
            break
        
        # Meminta input angka dari pengguna
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka.")
            continue
        
        # Memproses pilihan operasi
        if pilihan == '1':
            hasil = tambah(num1, num2)
            print(f"Hasil penjumlahan: {hasil}")
        elif pilihan == '2':
            hasil = kurang(num1, num2)
            print(f"Hasil pengurangan: {hasil}")
        elif pilihan == '3':
            hasil = kali(num1, num2)
            print(f"Hasil perkalian: {hasil}")
        elif pilihan == '4':
            hasil = bagi(num1, num2)
            print(f"Hasil pembagian: {hasil}")
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")

if __name__ == "__main__":
    main()
