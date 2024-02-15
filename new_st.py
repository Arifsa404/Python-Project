hafta = int(input("Kaç hafta dahili derse girdiniz?: "))
toplam = 0
for i in range(1,hafta + 1):
    saat = int(input(f"{i}.Haftada kaç saat?: "))
    toplam = toplam + saat

seçim = input("Toplamı Ögrenmek İçin 'T', Ortalamayı Ögrenmek İçin 'O' Yazın: ")

if seçim == "T":
    print(toplam)
elif seçim == "O":
    ort = (toplam / hafta)
    print(ort)