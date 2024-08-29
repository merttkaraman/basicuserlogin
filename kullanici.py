import tkinter as tk

##ARAYÜZ
arayuz = tk.Tk()
arayuz.title("Kullanıcı Girişi")
arayuz.geometry("300x200")
arayuz.configure(bg="lightblue")

##KULLANICI SATIRI
kullanici = tk.Label(text="Kullanıcı Adı:", bg="lightblue")
kullanici.place(x=10, y=10)

x = tk.StringVar()
kullanici_kutusu = tk.Entry(textvariable=x)
kullanici_kutusu.place(x=110, y= 10)

#ŞİFRE SATIRI
sifre = tk.Label(text="Şifre:", bg="lightblue")
sifre.place(x=10, y=35)

y = tk.StringVar()
sifre_kutusu = tk.Entry(textvariable=y, show="*")
sifre_kutusu.place(x=110, y= 35)

##GİRİŞ BUTONU
a1 = "mert"
a2 = "12345"

def giris_komut():
    kul = x.get()
    sif = y.get()
    print(kul,sif)
    if kul == a1 and sif == a2:
        print("Giriş Başarılı.")
        dogru_yanlis.config(text="Giriş Başarılı.",fg="Green")
    else:
        print("Kullanıcı Adı veya Şifre Yanlış.")
        dogru_yanlis.config(text="Giriş Başarısız.", fg="red")

giris = tk.Button(text="Giriş Yap",command=giris_komut)
giris.place(x=177, y=55)

##LABEL
dogru_yanlis = tk.Label(font="Verdana 20 bold",bg="lightblue")
dogru_yanlis.place(x=20,y=100)



arayuz.mainloop()
