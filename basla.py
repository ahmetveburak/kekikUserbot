# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Userbot import kekikUserbot, baslangic, tum_eklentiler, onemli, bilgi

baslangic() # Bot'u Aç Kapa

eklentiler = ""
j = 1
for i in tum_eklentiler:
    if j == 3:
        eklentiler += "| {:<18} |\n".format(i) if len(tum_eklentiler) != 3 else "| {:<18} |".format(i)
        j = 0
    else:
        eklentiler += "| {:<18}".format(i)
    j += 1

onemli("+===============================================================+")
onemli("|                       Eklentilerim                            |")
onemli("+===============+===============+===============+===============+")
bilgi(f"{eklentiler}")
onemli("+===============+===============+===============+===============+\n")

if __name__ == "__main__":
    kekikUserbot.run()