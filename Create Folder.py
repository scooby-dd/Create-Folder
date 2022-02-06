import os, time
import pyfiglet
banner=pyfiglet.figlet_format("Create Folder")
print(banner)
print("PROGRAM AÇILDI.")
time.sleep(0.5)
deger=input("devam edelimmi (yes/no): ")
if deger == "yes":
    print("Ozaman Klasör Oluşturma İşine Başlayalım.")
    time.sleep(0.1)
    change = input("Yer Belirleyin: ")
    os.chdir(change)
    yol = input("Dosya Yolu Belirleyiniz: ")
    open(yol,"w")
    os.listdir(change)
    os.startfile(os.curdir)
    os.chdir(change)
    os.startfile(yol)
elif deger == "no":
    print("Görüşürüz.")
