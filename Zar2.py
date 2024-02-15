import random

def vot():
    vote = random.randint(1, 6)
    print(vote)


a = 1
seçim = int(input("Zarı kaç kez atmak istiyorsunuz?: "))
while a <= seçim:
    print(f"{a}. atılan zarın sonucu: ")
    vot()
    a += 1

