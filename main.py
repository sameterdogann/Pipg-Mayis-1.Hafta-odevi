#Görev 1: Kullanıcıdan iki sayı alıp, aşağıdaki işlemleri yaparak ekrana yazdıran bir Python programı yazın:
sayi1 = float(input("İlk Sayıyı giriniz: "))
sayi2 = float(input("İkinci Sayıyı giriniz: "))
print("Sayıların Toplamı",sayi1+sayi2)
print("Sayıların Çıkarılması",sayi1-sayi2)
print("Sayıların Çarpma",sayi1*sayi2)
print("Sayıların Bölme",sayi1/sayi2)
print("Sayıların Mod Alma",sayi1%sayi2)
print("Sayıların Üssü nü alma",sayi1**sayi2)

#Görev 2: Kullanıcıdan bir sayı alarak 1’den o sayıya kadar olan sayıların toplamını hesaplayan bir Python programı yazın.
sayi3 = int(input("Lütfen Sayı Giriniz: "))
toplam = 0
for i in range(sayi3 + 1):
    toplam += i
print(toplam)

#Görev 3: 1 ile 100 arasındaki çift sayıları ekrana yazdıran bir Python programı yazın.
for i in range(1,100):
    if i%2 == 0:
        print(i)
#Görev 4: Kullanıcıdan alınan bir metni ters çeviren ve ekrana yazdıran bir Python programı yazın. (Döngü kullanarak yapın.)
