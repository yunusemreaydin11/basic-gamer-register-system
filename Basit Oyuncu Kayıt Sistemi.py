print("OYUNCU KAYIT")
kullanici_adi = input('Kullanıcı adı giriniz: ')
sifre = input('Şifre belirleyiniz: ')
yas = input('Yaşınızı giriniz: ')

bilgiler = [kullanici_adi, sifre, yas]

print("Bilgileriniz İşleniyor...")
print("Kullanıcı Adı: {}\nŞifre: {}\nYaş: {}\n".format(bilgiler[0], bilgiler[1], bilgiler[2]))

print("Bilgileriniz Başarılı Bir Şekilde Kaydedildi")