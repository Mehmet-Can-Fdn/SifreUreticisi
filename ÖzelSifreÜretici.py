import random
import string

def sifre_uret(uzunluk, buyuk_harf, kucuk_harf, rakam, ozel_karakter):
    karakterler = ""
    
    if buyuk_harf:
        karakterler += string.ascii_uppercase  # Büyük harfler (A-Z)
    if kucuk_harf:
        karakterler += string.ascii_lowercase  # Küçük harfler (a-z)
    if rakam:
        karakterler += string.digits  # Rakamlar (0-9)
    if ozel_karakter:
        karakterler += string.punctuation  # Özel karakterler (!@# etc.)

    if not karakterler:
        print("Hata: En az bir karakter türü seçmelisiniz!")
        return None

    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

# Kullanıcıdan giriş al
try:
    uzunluk = int(input("Şifre uzunluğunu girin: "))
    if uzunluk < 4:
        print("Şifre en az 4 karakter uzunluğunda olmalıdır.")
    else:
        buyuk_harf = input("Büyük harf kullanılsın mı? (E/H): ").strip().lower() == "e"
        kucuk_harf = input("Küçük harf kullanılsın mı? (E/H): ").strip().lower() == "e"
        rakam = input("Rakam kullanılsın mı? (E/H): ").strip().lower() == "e"
        ozel_karakter = input("Özel karakterler kullanılsın mı? (E/H): ").strip().lower() == "e"

        sifre = sifre_uret(uzunluk, buyuk_harf, kucuk_harf, rakam, ozel_karakter)
        if sifre:
            print("Oluşturulan Şifre:", sifre)

except ValueError:
    print("Lütfen geçerli bir sayı girin!")
