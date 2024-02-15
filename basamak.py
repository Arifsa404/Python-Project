def basamak_sayisi(sayi):
    basamaklar = 0
    while sayi != 0:
        sayi //= 10
        basamaklar += 1
    return basamaklar

girilen_sayi = int(input("Bir sayı girin: "))
basamak_sayisi = basamak_sayisi(girilen_sayi)
print("Girilen sayı", basamak_sayisi, "basamaklıdır.")
