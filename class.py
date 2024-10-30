class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f'Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm'

def main():
    while True:
        try:
            panjang = float(input("Masukkan panjang persegi panjang (cm): "))
            lebar = float(input("Masukkan lebar persegi panjang (cm): "))

            
            if panjang <= 0 or lebar <= 0:
                print("Panjang dan lebar harus lebih besar dari nol. Silakan coba lagi.")
                continue

           
            persegi_panjang = PersegiPanjang(panjang, lebar)

            
            print(persegi_panjang)
            print(f'Keliling: {persegi_panjang.hitung_keliling()} cm')
            print(f'Luas: {persegi_panjang.hitung_luas()} cm²')
            break  

        except ValueError:
            print("Input tidak valid. masukkan angka yang benar.")

if __name__ == "__main__":
    main()