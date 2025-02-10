import random
import string

def sifre_uret(uzunluk):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

# Kullanıcıdan uzunluk al
try:
    uzunluk = int(input("Şifre uzunluğunu girin: "))
    if uzunluk < 4:
        print("Şifre en az 4 karakter uzunluğunda olmalıdır.")
    else:
        print("Oluşturulan Şifre:", sifre_uret(uzunluk))
except ValueError:
    print("Lütfen geçerli bir sayı girin!")
