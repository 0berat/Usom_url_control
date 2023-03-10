from tkinter import * #Tkinter, Python için bir arayüz geliştirme modülüdür.
import datetime       #Sorgulunan urlleri loglamak icin datetime modulunu import ediyoruz.
def kontrol_et():
    print("test")
    dosya=open("usom.txt","r")
    icerik=dosya.read()
    dosya.close()
    ip=entry1.get() #kutucuklardan cekilen url degeri ip degiskenine ataniyor.
    bugun=datetime.datetime.now() #tarih bilgisi bugun degerine ataniyor.
   #if else yapisinda url hem kontrol ediliyor hemde loglaniyor.
    if str(ip) in icerik:
        dosya=open("log.txt","a")
        yazi= str(ip)+"zararli\nTarih"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("ip zararlidir")
    else:
        dosya=open("log.txt","a")
        yazi= str(ip)+"zararli degil\nTarih"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("ip zararli degildir")

#Bu kisimda arayuz tasarlaniyor.
top=Tk()
top.geometry("500x200")
top.title("USOM IP kontrol")
#islevi yapicak butonumuz.
B=Button(top,text="kontrol et",command=kontrol_et,font=('Arial', 15))
B.place()
B.pack()
#Bilgilendirici yazimiz.
label1=Label(top,text="Kontrol edilcek ip adresini giriniz.",font=('Arial', 15))
label1.place()
label1.pack()
#entry1 a url girilicek.
entry1=Entry(top,width=40,font=('Arial', 15))
entry1.pack()
v=StringVar()
#sonucun cikacagi alan
entry2=Entry(top,width=40,textvariable=v,font=('Arial', 15))
entry2.pack()
top.mainloop()

