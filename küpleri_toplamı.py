def basamak_kupleri_toplami(sayi):
    basamaklar = [int(digit) for digit in str(sayi)]
    kupler_toplami = sum([basamak ** 3 for basamak in basamaklar])
    return kupler_toplami

girilen_sayi = int(input("3 basamaklı bir sayı girin: "))

if girilen_sayi < 100 or girilen_sayi > 999:
    print("Geçersiz giriş! Lütfen 3 basamaklı bir sayı girin.")
else:
    kupler_toplami = basamak_kupleri_toplami(girilen_sayi)
    if kupler_toplami == girilen_sayi:
        print("Girilen sayı, basamaklarının küpleri toplamına eşittir.")
    else:
        print("Girilen sayı, basamaklarının küpleri toplamına eşit değildir.")