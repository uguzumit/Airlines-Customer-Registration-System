# Airlines-Customer-Registration-System
# A backend project written in Python, open the devolopment.

import random

print("    <----- HAVA YOLLARI SISTEMI ----->  \n")

wu = int(input("Tanımlanacak Uçak Sayısı: "))
wy = int(input("Tanımlanan Uçaktaki Yolcu Sayısı: "))
print("----------------------------------------")

o = 0
u = 0 
while u < wu:
    u = u+1
    ucak_u = f"ucak_{u}"
    
    if u < 10:
        uno = f"{o}{u}"
    else:
        uno = f"{u}"

    class ucak():
        def __init__(self, firmaAdi, kalkisNoktasi, inisNoktasi, ucusNo, pistNo):
            self.firma_adi=firmaAdi
            self.kalkis_noktasi=kalkisNoktasi
            self.inis_noktasi=inisNoktasi
            self.ucus_numarası=ucusNo
            self.pist_numarasi=pistNo
            self.kalkis_noktasi_r=self.kalkis_noktasi.replace("ç","c").replace("ğ","g").replace("ö","o").replace("ş","s").replace("ü","u")
            self.inis_noktasi_r=self.inis_noktasi.replace("ç","c").replace("ğ","g").replace("ö","o").replace("ş","s").replace("ü","u")

        def ucak_bilgi(self):
            print("----------------------------------------")
            print(f"          UCAK {uno} BILGI SISTEMI          ")
            print("----------------------------------------")
            print("Uçuş Firması:",self.firma_adi)
            print("Kalkış Noktası:",self.kalkis_noktasi_r.upper()+" HAVALIMANI")
            print("İniş Noktası:",self.inis_noktasi_r.upper()+" HAVALIMANI")
            print("Kalkış Saati:",f"{i_k_s}:00")
            print("İniş Saati:",f"{i_i_s}:15")
            print("Uçuş Numarası:",self.ucus_numarası)
            print("Pist Numarası:",self.pist_numarasi)
            print("----------------------------------------")
    
    f_a = "TURK HAVA YOLLARI" 
    k_n = input("Kalkış Noktası: ")
    i_n = input("İniş Noktası: ")
    u_n = str(random.randrange(000000, 999999))
    p_n = int(random.randrange(110, 150))
    k_s = int(input("Kalkış Saati: "))
    
    if -1 < k_s < 25:
        if k_s == 24:
            k_s = 0
            i_k_s = f"{o}{k_s}"
        else:
            if k_s < 10:
                i_k_s = f"{o}{k_s}"
            else:
                i_k_s = f"{k_s}"
        i_s = k_s+1
        if i_s == 24:
            i_s = 0
            i_k_s = f"{0}{i_s}"
        else:
            if i_k_s == 00:
                i_i_s = f"{o}{i_s}"
            else:
                if i_s < 10:
                    i_i_s = f"{o}{i_s}"
                else:
                    i_i_s = f"{i_s}"
        if k_s == 23:
            i_k_s = f"{k_s}"
            i_i_s = f"{o}{o}"
    else:
        print("Lütfen 0 İle 24 Arasında Bir Sayı Giriniz!")

    ucak_u = ucak(f_a, k_n, i_n, u_n, p_n)
    ucak_u.ucak_bilgi()

    y = 0
    while y < wy:
        y = y+1
        yolcu_y = f"yolcu_{y}"

        if y < 10:
            yno = f"{o}{y}"
        else:
            yno = f"{y}"

        class yolcu(ucak):
            def __init__(self, yolcuAdi, yolcuSoyadi, firmaAdi, kalkisNoktasi, inisNoktasi, ucusNo, pistNo):
                super().__init__(firmaAdi, kalkisNoktasi, inisNoktasi, ucusNo, pistNo)
                self.yolcu_adi=yolcuAdi
                self.yolcu_soyadi=yolcuSoyadi
                self.yolcu_adi_r=self.yolcu_adi.replace("ç","c").replace("ğ","g").replace("ö","o").replace("ş","s").replace("ü","u")
                self.yolcu_soyadi_r=self.yolcu_soyadi.replace("ç","c").replace("ğ","g").replace("ö","o").replace("ş","s").replace("ü","u")

            def yolcu_bilgi(self):
                print("----------------------------------------")
                print(f"          YOLCU {yno} BILGI SISTEMI          ")
                print("----------------------------------------")
                print("Uçuş Firması:",self.firma_adi)
                print("Uçuş Numarası:","THY"+f"{u}{yno}"+k_n[0].upper()+i_n[0].upper())
                print("Koltuk Numarası:",yno)
                print("Yolcu Adı:",self.yolcu_adi_r.upper())
                print("Yolcu Soyadı:",self.yolcu_soyadi_r.upper())
                print("Kalkış Noktası:",self.kalkis_noktasi_r.upper()+" HAVALIMANI")
                print("İniş Noktası:",self.inis_noktasi_r.upper()+" HAVALIMANI")
                print("Kalkış Saati:",f"{i_k_s}:00")
                print("İniş Saati:",f"{i_i_s}:15")
                print("----------------------------------------")

        y_a = input("Yolcu Adı: ")
        y_s = input("Yolcu Soyadı: ")
        yolcu_y = yolcu(y_a, y_s, f_a, k_n, i_n, u_n, p_n)
        yolcu_y.yolcu_bilgi()

        class bilet(yolcu):
            def __init__(self, yolcuAdi, yolcuSoyadi, firmaAdi, kalkisNoktasi, inisNoktasi, ucusNo, pistNo):
                super().__init__(yolcuAdi, yolcuSoyadi, firmaAdi, kalkisNoktasi, inisNoktasi, ucusNo, pistNo)

            def bilet_bilgi(self):
                print("----------------------------------------")
                print(f"          BILET {yno} BILGI SISTEMI          ")
                print("----------------------------------------")
                print(f"    THY {self.ucus_numarası} {self.kalkis_noktasi_r[0:3].upper()} {i_k_s}:00 - {self.inis_noktasi_r[0:3].upper()} {i_i_s}:15\n")
                print("   |GATE|    |BOARDING TIME|   |SEAT|")
                print(f"   | 0{u} |    |    {i_k_s}:00    |   | {yno} |\n")
                print(f"    FLIGHT NO {uno}{u_y_n}{yno} - {self.yolcu_adi_r.upper()} {self.yolcu_soyadi_r.upper()}")
                print("----------------------------------------")

        u_y_n = u_n[0:4]

        bilet_y = bilet(y_a, y_s, f_a, k_n, i_n, u_n, p_n)
        bilet_y.bilet_bilgi()

        class bavul(yolcu):
            def __init__(self, yolcuAdi, yolcuSoyadi, firmaAdi, kalkisNoktasi, inisNoktasi, ucusNo, pistNo):
                super().__init__(yolcuAdi, yolcuSoyadi, firmaAdi, kalkisNoktasi, inisNoktasi, ucusNo, pistNo)

            def bavul_bilgi(self):
                print("----------------------------------------")
                print(f"          BAVUL {yno} BILGI SISTEMI          ")
                print("----------------------------------------")
                print(f"    THY {self.ucus_numarası} {self.kalkis_noktasi_r[0:3].upper()} {i_k_s}:00 - {self.inis_noktasi_r[0:3].upper()} {i_i_s}:15")
                print(f"    Flıght No {uno}{u_y_n}{yno} - {self.yolcu_adi_r.upper()} {self.yolcu_soyadi_r.upper()}")
                print(f"    Baggage Handling System No {u}")
                print(f"    Baggage Handling Start Time {i_i_s}:30")
                print("----------------------------------------")

        bavul_y = bavul(y_a, y_s, f_a, k_n, i_n, u_n, p_n)
        bavul_y.bavul_bilgi()

    if wy == 0:
        print("----------------------------------------")
        print(f"Uçağın Doluluk Oranı: 0.0% | {y} Yolcu")
        print("----------------------------------------\n")
    
    elif wy > 0:
        class doluluk_oranı():
            def __init__(self,yolcuSayisi):
                self.yolcuSayisi=yolcuSayisi 
            
            def __pow__(self,kapasite):
                d_o = (self.yolcuSayisi/kapasite)*100
                return d_o   
        
        doluluk_oranı_y = doluluk_oranı(y)
        y_d_o = doluluk_oranı.__pow__(doluluk_oranı_y,220)  
        
        print("----------------------------------------")
        print(f"Uçağın Doluluk Oranı: {y_d_o:.1f}% | {y} Yolcu")
        print("----------------------------------------")
        print("\n")
    else:
        print("Tanımlanan Uçaktaki Yolcu Sayısı Tanımsız!")

input("Programı Kapatmak İçin Herhangi Bir Tuşa Basın: ")
