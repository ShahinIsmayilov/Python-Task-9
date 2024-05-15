with open("giris.txt", "r", encoding="utf-8") as f:
    giris_cümle = f.readline().strip()

cixis_cümle = giris_cümle.upper()

with open("cixis.txt", "w", encoding="utf-8") as f:
    f.write(cixis_cümle)
